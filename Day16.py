from datetime import datetime


value_dict = {
"0": [0,0,0,0],
"1": [0,0,0,1],
"2": [0,0,1,0],
"3": [0,0,1,1],
"4": [0,1,0,0],
"5": [0,1,0,1],
"6": [0,1,1,0],
"7": [0,1,1,1],
"8": [1,0,0,0],
"9": [1,0,0,1],
"A": [1,0,1,0],
"B": [1,0,1,1],
"C": [1,1,0,0],
"D": [1,1,0,1],
"E": [1,1,1,0],
"F": [1,1,1,1]
}


arr_int_values = {}
packet_count = 0

global_bit_arr = []
header = 0

global_versions = []
global_types = []
global_values = []
global_values_v2 = []

global_temp_values = []


def get_bit_arr(unformatted_string):
    global value_dict
    result = []
    for i in range(unformatted_string.__len__()):
        mini_arr = value_dict[unformatted_string[i]]
        result.extend(mini_arr)
    return result


def bit_arr_to_int(arr):
    global arr_int_values
    print("arr len: ", arr.__len__())
    arr_key = "".join(str(arr))
    if arr_key in arr_int_values.keys():
        return arr_int_values[arr_key]
    result = 0
    reverse_arr = arr[::-1]
    for i in range(reverse_arr.__len__()):
        if reverse_arr[i] == 1:
            result+= 2**(i)
    arr_int_values[arr_key] = result
    return result


def unpack_bits(bit_arr):
    #bit_arr = global_bit_arr
    versions = []
    types = []
    values = []
    values_read = 0
    version = bit_arr_to_int(bit_arr[:3])
    type = bit_arr_to_int(bit_arr[3:6])
    print("header: ", header)

    values_read = 6
    value_arr = bit_arr.copy()[6:]
    versions.append(version)
    types.append(type)


    if type == 4:
        more_exists = True
        counter = 0
        literal_value = []
        while more_exists:
            try:
                more_exists = value_arr[counter] == 1
            except:
                more_exists=False
            payload = value_arr[counter +1:counter +5]
            literal_value.extend(payload)
            counter +=5
        values.append(bit_arr_to_int(literal_value))
        values_read +=counter
    else:
        len_id = value_arr[0]
        values_read+=1
        if len_id == 0:
            len_packets = bit_arr_to_int(value_arr[1:16])
            values_read += 15

            counter = 0
            value_arr = value_arr.copy()[16:]
            tot_values_read = 0
            while counter < len_packets:
                new_versions, new_types, new_values, new_values_read = unpack_bits(value_arr[counter:len_packets])
                counter += new_values_read
                versions.extend(new_versions)
                types.extend(types)
                values.extend(new_values)
                values_read += new_values_read

        elif len_id == 1:
            nbr_of_sub_packets = bit_arr_to_int(value_arr[1:12])
            values_read += 11

            counter = 0
            packets = 0
            value_arr = value_arr.copy()[12:]
            while packets < nbr_of_sub_packets:
                new_versions, new_types, new_values, new_values_read = unpack_bits(value_arr.copy()[counter:])
                counter += new_values_read
                packets+=1
                versions.extend(new_versions)
                types.extend(types)
                values.extend(new_values)
                values_read += new_values_read

        else:
            print("something gone terrible wrong")

    return versions, types, values, values_read


def unpack_arrays(new_packets):
    result = []
    print(type(new_packets))
    for n in new_packets:
        print(type(n))

        if type(n) != int:
            result.extend(unpack_arrays(n))
        else:
            result.append(n)
    return result


def unpack_bits2():
    global global_bit_arr
    global header
    global global_versions
    global global_types
    global global_values
    global global_temp_values
    global global_values_v2

    bit_arr = global_bit_arr
    h_check = header

    values = []
    version = bit_arr_to_int(bit_arr[header:header+3])
    header+=3
    type = bit_arr_to_int(bit_arr[header:header+3])
    header+=3
    print("header: ", header)
    print("bit_arr: ", len(bit_arr))

    global_versions.append(version)
    global_types.append(type)
    values_read = 6


    if type == 4:
        more_exists = True
        counter = 0
        literal_value = []
        while more_exists:
            try:
                more_exists = bit_arr[header] == 1
                header +=1
                counter +=1
            except:
                more_exists=False
            payload = bit_arr[header:header +4]
            literal_value.extend(payload)
            header += 4
            counter += 4
        end_val = bit_arr_to_int(literal_value)
        values.append(end_val)
        values_read += counter
    else:
        len_id = bit_arr[header]
        header+=1
        values_read +=1
        if len_id == 0:
            len_packets = bit_arr_to_int(bit_arr[header:header+15])
            header += 15
            values_read += 15
            header_value_before = header
            delta_header = 0
            packets = 0

            while delta_header < len_packets:
                #new_versions, new_types, new_values, new_values_read = unpack_bits(bit_arr[header:header+len_packets-counter])
                unpack_bits2()
                delta_header = header - header_value_before
                packets+=1
            new_packets = global_temp_values[-packets:]
            global_temp_values = global_temp_values[:-packets]
            new_arr = unpack_arrays(new_packets)
            global_temp_values.append(new_arr)

        elif len_id == 1:
            nbr_of_sub_packets = bit_arr_to_int(bit_arr[header:header+11])
            header+=11
            values_read += 11
            counter = 0
            packets = 0
            while packets < nbr_of_sub_packets:
                unpack_bits2()
                packets+=1
            new_packets = global_temp_values[-packets:]
            global_temp_values = global_temp_values[:-packets]
            new_arr = unpack_arrays(new_packets)
            global_temp_values.append(new_arr)
        else:
            print("something gone terrible wrong")

        ##Id checking
        #Sum
        if type!=4:
            g=global_temp_values
            #temp_values = global_temp_values[-1]
            #global_temp_values = global_temp_values[:global_temp_values.__len__()-1]
            g=global_temp_values
            if type == 0:
                arr = global_temp_values[-1]
                packet_sum = sum(global_temp_values[-1])
                del global_temp_values[-1]
                g = global_temp_values

            #product
            elif type == 1:
                packet_sum = 1
                for n in global_temp_values[-1]:
                    packet_sum*=n
                del global_temp_values[-1]

            #minimum
            elif type == 2:
                packet_sum = min(global_temp_values[-1])
                del global_temp_values[-1]

            #max
            elif type == 3:
                packet_sum = max(global_temp_values[-1])
                del global_temp_values[-1]

            #Greater than
            elif type == 5:
                packet_sum = 0
                if global_temp_values[-1][0]>global_temp_values[-1][1]:
                    packet_sum = 1
                del global_temp_values[-1]

            #less than
            elif type == 6:
                packet_sum = 0
                if global_temp_values[-1][0] < global_temp_values[-1][1]:
                    packet_sum = 1
                del global_temp_values[-1]
            #Equal
            elif type == 7:
                packet_sum = 0
                g=global_temp_values
                if global_temp_values[-1][0]==global_temp_values[-1][1]:
                    packet_sum = 1
                del global_temp_values[-1]



            global_values_v2.append(packet_sum)
            values.append(packet_sum)


    global_temp_values.append(values)
    global_values.append(values)
    #return versions, types, values

class Package():
    def __init__(self, version, type, payload):
        self.version = version
        self.type = type
        self.payload = payload

    def get_size(self):
        return self.payload.__len__()


def run():
    global global_bit_arr
    start_time = datetime.now().time()  # time object

    file = open("day16")
    unformatted_string = file.read()
    print(unformatted_string)
    char = unformatted_string[0]

    bit_arr = get_bit_arr(unformatted_string)
    global_bit_arr = bit_arr
    print(bit_arr.__len__())
    #versions, types, values, values_read = unpack_bits(bit_arr)
    unpack_bits2()
    print(global_versions)
    print(global_types)
    print(global_values)
    print(sum(global_versions))
    print("sum_v2_temp: ", global_temp_values)
    print("sum_v2: ", sum(global_values_v2))

    end_time = datetime.now().time()  # time object
    delta_seconds = end_time.microsecond - start_time.microsecond
    print(delta_seconds)
    #Should do class packet with payload... Then take the class and payload to generate new package and continue... No ram eating




run()