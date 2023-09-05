
class Entry:
    def __init__(self, signal_patterns, output_value):
        self.signal_patterns = signal_patterns.split(" ")
        self.output_value = output_value.split(" ")
        self.signal_dict = dict()
        self.nbr_to_signal = dict()
        self.output_value_nbrs = ""


def get_nbr_from_dict(val, signal_dict):

    for keypair in signal_dict.items():
        lenght = len(val)
        if len(keypair[0]) == len(val):
            if(string_in_string(val, keypair[0]) == lenght):
                return keypair[1]
    return -1


def calc_output(e):
    e.output_value_nbrs = ""
    for val in e.output_value:
        string = str(get_nbr_from_dict(val, e.signal_dict))
        e.output_value_nbrs += string


def update_nbr_dict(e):
    e.nbr_to_signal = {v: k for k, v in e.signal_dict.items()}


def string_in_string(chars, val):
    sum = 0
    for char in chars:
        if char in val:
            sum += 1
    return sum

def calc_signal_dictl(e):
    #calc 1, 7, 4, 8
    for val in e.signal_patterns:
        if len(val) == 2:
            e.signal_dict[val] = 1
        elif len(val) == 3:
            e.signal_dict[val] = 7
        elif len(val) == 4:
            e.signal_dict[val] = 4
        elif len(val) == 7:
            e.signal_dict[val] = 8

    update_nbr_dict(e)
    for val in e.signal_patterns:
        # calc 5nbrs 2,3,5

        if len(val) == 5:
            #check for 3
            if(string_in_string(e.nbr_to_signal[1], val) == 2):
                e.signal_dict[val] = 3
            elif(string_in_string(e.nbr_to_signal[4],val) == 2):
                e.signal_dict[val] = 2
            elif(string_in_string(e.nbr_to_signal[4], val) == 3):
                e.signal_dict[val] = 5
        #0, 6, 9
        if len(val) == 6:
            if(string_in_string(e.nbr_to_signal[4], val) == 4):
                e.signal_dict[val] = 9
            elif(string_in_string(e.nbr_to_signal[1], val) == 2):
                e.signal_dict[val] = 0
            elif(string_in_string(e.nbr_to_signal[1], val) == 1):
                e.signal_dict[val] = 6

        if len(val) == 7:
            e.signal_dict[val] = 8

    update_nbr_dict(e)







def run():
    lines = open("day8").read().splitlines()
    print (lines)

    entries = list(map(lambda x: (Entry( x.split("|")[0].strip(), x.split("|")[1].strip() ) ),lines))
    print(entries)
    longstring = ""
    sum = 0
    for e in entries:
        calc_signal_dictl(e)
        calc_output(e)
        sum += int(e.output_value_nbrs)
        longstring += e.output_value_nbrs
        print(e.output_value_nbrs)

    nbrs_count = longstring.count('1') +longstring.count('4')+longstring.count('7')+longstring.count('8')
    print(longstring.count('1'))
    print(longstring.count('4'))
    print(longstring.count('7'))
    print(longstring.count('8'))
    print(nbrs_count)
    print(sum)



run()