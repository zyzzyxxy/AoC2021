
class Scanner():
    offset_x = 0
    offset_y = 0
    offset_z = 0
    offset_x_to_zero = 0
    offset_y_to_zero = 0
    offset_z_to_zero = 0
    good_position = 0
    good_rotation = 0
    have_zero_info = False
    enough_to_include = False
    position = 0
    rotation_z = 0
    x_map = "x"
    y_map = "y"
    z_map = "z"

    def remap_to_self(self):
        self.re_map(self.x_map, self.y_map, self.z_map)

    def re_map(self,x_map, y_map, z_map):
        self.x_map = x_map
        self.y_map = y_map
        self.z_map = z_map
        #Map x
        if x_map == "-x":
            for beacon in self.beacon_list:
                beacon.x = -beacon.x_org
        if x_map == "y":
            for beacon in self.beacon_list:
                beacon.x = beacon.y_org
        if x_map == "-y":
            for beacon in self.beacon_list:
                beacon.x = -beacon.y_org
        if x_map == "z":
            for beacon in self.beacon_list:
                beacon.x = beacon.z_org
        if x_map == "-z":
            for beacon in self.beacon_list:
                beacon.x = -beacon.z_org

        #Map y
        if y_map == "x":
            for beacon in self.beacon_list:
                beacon.y = beacon.x_org
        if y_map == "-x":
            for beacon in self.beacon_list:
                beacon.y = -beacon.x_org
        if y_map == "y":
            for beacon in self.beacon_list:
                beacon.y = beacon.y_org
        if y_map == "-y":
            for beacon in self.beacon_list:
                beacon.y = -beacon.y_org
        if y_map == "z":
            for beacon in self.beacon_list:
                beacon.y = beacon.z_org
        if y_map == "-z":
            for beacon in self.beacon_list:
                beacon.y = -beacon.z_org

        #Map z
        if z_map == "x":
            for beacon in self.beacon_list:
                beacon.z = beacon.x_org
        if z_map == "-x":
            for beacon in self.beacon_list:
                beacon.z = -beacon.x_org
        if z_map == "y":
            for beacon in self.beacon_list:
                beacon.z = beacon.y_org
        if z_map == "-y":
            for beacon in self.beacon_list:
                beacon.z = -beacon.y_org
        if z_map == "z":
            for beacon in self.beacon_list:
                beacon.z = beacon.z_org
        if z_map == "-z":
            for beacon in self.beacon_list:
                beacon.z = -beacon.z_org

    def get_axis_list(self, axis):
        if axis == 'x':
            result_list = [b.x for b in self.beacon_list]
            return result_list
        if axis == 'y':
            result_list = [b.y for b in self.beacon_list]
            return result_list
        if axis == 'z':
            result_list = [b.z for b in self.beacon_list]
            return result_list

    def __init__(self, name, beacon_list=[]):
        self.name = name
        self.beacon_list = beacon_list

    def align_zero(self):
        #self.change_orientation_too_good()
        self.reset()
        self.remap_to_self()
        self.offset(self.offset_x_to_zero, self.offset_y_to_zero, self.offset_z_to_zero)
        self.isAligned = True

    def change_all_too_good(self):
        self.reset()
        self.change_position(self.good_position)
        self.rotate_z_times(self.good_rotation)
        self.offset(self.offset_x, self.offset_y, self.offset_z)

    def change_orientation_too_good(self):
        self.reset()
        self.change_position(self.good_position)
        self.position = self.good_position
        self.rotate_z_times(self.good_rotation)
        self.rotation_z = self.good_rotation

    def add_beacon(self, beacon):
        self.beacon_list.append(beacon)

    def change_position(self, nbr):
        if nbr == 0:
            pass
        if nbr == 1:
            self.rotate_90_x()
        if nbr == 2:
            self.rotate_90_x()
            self.rotate_90_x()
        if nbr == 3:
            self.rotate_90_x()
            self.rotate_90_x()
            self.rotate_90_x()
        if nbr == 4:
            self.rotate_90_y()
        if nbr == 5:
            self.rotate_90_y()
            self.rotate_90_y()

    def rotate_90_x(self):
        for beacon in self.beacon_list:
            beacon.rotate_90_x()

    def rotate_90_y(self):
        for beacon in self.beacon_list:
            beacon.rotate_90_y()

    def rotate_90_z(self):
        for beacon in self.beacon_list:
            beacon.rotate_90_z()


    def rotate_z_times(self, nbr):
        for i in range(nbr):
            self.rotate_90_z()

    def reset(self):
        for beacon in self.beacon_list:
            beacon.reset_to_original()

    def offset(self, x, y, z):
        for beacon in self.beacon_list:
            beacon.x += x
            beacon.y += y
            beacon.z += z

    def print_beacons(self):
        print(f"{self.name}")
        for beacon in self.beacon_list:
            print(f"{beacon.x},{beacon.y},{beacon.z}")

class Beacon():

    visited = False

    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
        self.x_org = x
        self.y_org = y
        self.z_org = z


    #x and y "floor" plane and z height
    def rotate_90_x(self):
        temp_y = self.y
        self.y = -self.z
        self.z = temp_y

    def rotate_90_y(self):
        temp_z = self.z
        self.z = - self.x
        self.x = temp_z

    def rotate_90_z(self):
        temp_x = self.x
        self.x = -self.y
        self.y = temp_x

    def reset_to_original(self):
        self.x = self.x_org
        self.y = self.y_org
        self.z = self.z_org

def rotate_x(x,y,z):
    temp_y = y
    y = -z
    z = temp_y
    return x,y,z


def compare_coordinates(Scanner_1, Scanner_2):
    delta_dict = {}
    counter = 0
    for i in range(6):
        for j in range(4):
            counter += 1
            Scanner_2.reset()
            Scanner_2.change_position(i)
            Scanner_2.rotate_z_times(j)
            for beacon in Scanner_1.beacon_list:
                for beacon2 in Scanner_2.beacon_list:
                    delta_x = beacon.x - beacon2.x
                    delta_y = beacon.y - beacon2.y
                    delta_z = beacon.z - beacon2.z
                    key = f"{delta_x},{delta_y},{delta_z},{i},{j}"
                    if not key in delta_dict:
                        delta_dict[key] = 1
                    else:
                        delta_dict[key] += 1

    Scanner_2.reset()
    return delta_dict
def compare_single_cordinates(values1, values2, axis):
    diffs = {}
    for value in values1:
        for value2 in values2:
            diff = value - value2
            key = f"{diff}:{axis}"
            if not key in diffs:
                diffs[key] = 1
            else:
                diffs[key] += 1
            diff2 = value + value2
            key2 = f"{diff2}:-{axis}"
            if not key2 in diffs:
                diffs[key2] = 1
            else:
                diffs[key2] += 1
    max_key = max(diffs, key=diffs.get)
    return diffs, max_key, diffs[max_key]


def compare_coordinates2(Scanner_1, Scanner_2):
    coordinate_map = {}
    #compare x to x
    x_x_diffs, x_x_max_key, x_x = compare_single_cordinates(Scanner_1.get_axis_list('x'), Scanner_2.get_axis_list('x'), 'x')
    x_y_diffs, x_y_max_key, x_y = compare_single_cordinates(Scanner_1.get_axis_list('x'), Scanner_2.get_axis_list('y'), 'y')
    x_z_diffs, x_z_max_key, x_z = compare_single_cordinates(Scanner_1.get_axis_list('x'), Scanner_2.get_axis_list('z'), 'z')

    max_val = max([x_x, x_y, x_z])
    if max_val<12:
        return
    else:
        if x_x >= x_y and x_x >= x_z:
            coordinate_map['x'] = x_x_max_key
        elif x_y >= x_z:
            coordinate_map['x'] = x_y_max_key
        else:
            coordinate_map['x'] = x_z_max_key

    ##comapare to y
    y_x_diffs, y_x_max_key, y_x = compare_single_cordinates(Scanner_1.get_axis_list('y'), Scanner_2.get_axis_list('x'),'x')
    y_y_diffs, y_y_max_key, y_y = compare_single_cordinates(Scanner_1.get_axis_list('y'), Scanner_2.get_axis_list('y'),'y')
    y_z_diffs, y_z_max_key, y_z = compare_single_cordinates(Scanner_1.get_axis_list('y'), Scanner_2.get_axis_list('z'),'z')

    max_val = max([y_x, y_y, y_z])
    if max_val < 12:
        return
    else:
        if y_x >= y_y and y_x >= y_z:
            coordinate_map['y'] = y_x_max_key
        elif y_y >= y_z:
            coordinate_map['y'] = y_y_max_key
        else:
            coordinate_map['y'] = y_z_max_key

        ##comapare to z
    z_x_diffs, z_x_max_key, z_x = compare_single_cordinates(Scanner_1.get_axis_list('z'), Scanner_2.get_axis_list('x'),'x')
    z_y_diffs, z_y_max_key, z_y = compare_single_cordinates(Scanner_1.get_axis_list('z'), Scanner_2.get_axis_list('y'),'y')
    z_z_diffs, z_z_max_key, z_z = compare_single_cordinates(Scanner_1.get_axis_list('z'), Scanner_2.get_axis_list('z'),'z')



    max_val = max([z_x, z_y, z_z])
    if max_val < 12:
        return
    else:
        if z_x >= z_y and z_x >= z_z:
            coordinate_map['z'] = z_x_max_key
        elif z_y >= z_z:
            coordinate_map['z'] = z_y_max_key
        else:
            coordinate_map['z'] = z_z_max_key

    return coordinate_map



def test():
    sum = 0
    for i in range(2000):
        print(i)
        for j in range(2000):
            for k in range(2000):
                sum +=1
    return sum


def get_coodinates_from_key(coordinate_dict):
    x = int(coordinate_dict['x'].split(":")[0])
    y = int(coordinate_dict['y'].split(":")[0])
    z = int(coordinate_dict['z'].split(":")[0])
    x_map = coordinate_dict['x'].split(":")[1]
    y_map = coordinate_dict['y'].split(":")[1]
    z_map = coordinate_dict['z'].split(":")[1]
    return x, y, z, x_map, y_map, z_map


def same_coordinates(beacon, beacon2):
    return beacon.x == beacon2.x \
            and beacon.y == beacon2.y \
            and beacon.z == beacon2.z


def get_same_beacons(Scanner1, Scanner2, x, y, z):
    beacon_list = []
    same = 0
    best = 0

    for i in range(6):
        for j in range(4):
            temp_list = []
            Scanner2.reset()
            Scanner2.change_position(i)
            Scanner2.rotate_z_times(j)
            Scanner2.offset(x, y, z)

            # for k in range(6):
            #     for l in range(4):
            #         Scanner2.change_position(i)
            #         Scanner2.rotate_90_z()
            for beacon in Scanner1.beacon_list:
                for beacon2 in Scanner2.beacon_list:
                    if same_coordinates(beacon, beacon2):
                        temp_list.append(beacon)
                        same += 1
            if same > best:
                best = same
                beacon_list = temp_list
                Scanner2.offset_x = x
                Scanner2.offset_y = y
                Scanner2.offset_z = z
                Scanner2.good_position = i
                Scanner2.good_rotation = j

    return beacon_list

def get_same_beacons_simple(Scanner1, Scanner2):
    beacon_list = []

    for beacon in Scanner1.beacon_list:
        for beacon2 in Scanner2.beacon_list:
            if same_coordinates(beacon, beacon2):
                beacon_list.append(beacon)
                beacon.visited = True
                beacon2.visited = True

    return beacon_list


def add_all_to_scanner(Ultra_Scanner, scanner):

    for beacon in scanner.beacon_list:
        new_beacon = Beacon(beacon.x,beacon.y,beacon.z)
        Ultra_Scanner.add_beacon(new_beacon)


def get_pos_rot(Scanner1, Scanner2, x, y, z):
    for i in range(6):
        for j in range(4):
            temp_list = []
            Scanner2.reset()
            Scanner2.change_position(i)
            Scanner2.rotate_z_times(j)
            Scanner2.offset(x, y, z)

            # for k in range(6):
            #     for l in range(4):
            #         Scanner2.change_position(i)
            #         Scanner2.rotate_90_z()
            for beacon in Scanner1.beacon_list:
                for beacon2 in Scanner2.beacon_list:
                    if same_coordinates(beacon, beacon2):
                        temp_list.append(beacon)


def Calculate_unique(beacon_list):
    result = []
    for beacon in beacon_list:
        val = (beacon.x, beacon.y, beacon.z)
        if val not in result:
            result.append(val)

    return result


def add_visited_to_scanner(Ultra_Scanner, scanner):
    for beacon in scanner.beacon_list:
        if beacon.visited:
            new_beacon = Beacon(beacon.x, beacon.y, beacon.z)
            Ultra_Scanner.add_beacon(new_beacon)


def calc_manhattan(Scanner1, Scanner2):
    result = 0
    a = abs(Scanner1.offset_x_to_zero - Scanner2.offset_x_to_zero)
    b = abs(Scanner1.offset_y_to_zero - Scanner2.offset_y_to_zero)
    c = abs(Scanner1.offset_z_to_zero - Scanner2.offset_z_to_zero)
    result = a + b + c
    return result


def run():
    Scanners = []
    file = open("day19")
    scanners = file.read().split("\n\n")
    for counter, s in enumerate(scanners):
        name = s.splitlines()[0]
        beacons = s.splitlines()[1:]
        beacon_list = []
        for beacon in beacons:
            x, y, z = beacon.split(",")
            b = Beacon(int(x), int(y), int(z))
            beacon_list.append(b)
        # Scanners[counter] = scanner
        scanner = Scanner(name, beacon_list)
        Scanners.append(scanner)

    last_run = 0
    this_run = 20
    while last_run < this_run:
        last_run = this_run
        scanners_len = Scanners.__len__()
        Scanners[0].have_zero_info = True
        for i in range(scanners_len):
            for j in range(scanners_len-i):
                if(i+j != i):
                    Scanner1 = Scanners[i]
                    Scanner2 = Scanners[j+i]

                    if Scanner1.have_zero_info and Scanner2.have_zero_info:
                        pass
                        coordinate_dict = None
                    elif Scanner1.have_zero_info:
                        coordinate_dict = compare_coordinates2(Scanner1, Scanner2)
                    elif Scanner2.have_zero_info:
                        temp_scanner = Scanner2
                        Scanner2 = Scanner1
                        Scanner1 = temp_scanner
                        coordinate_dict = compare_coordinates2(Scanner1, Scanner2)
                    if coordinate_dict:
                        x, y, z, x_map, y_map, z_map = get_coodinates_from_key(coordinate_dict)
                        Scanner2.offset_x_to_zero = x
                        Scanner2.offset_y_to_zero = y
                        Scanner2.offset_z_to_zero = z
                        Scanner2.have_zero_info = True

                        Scanner2.re_map(x_map, y_map, z_map)
                        Scanner2.align_zero()

                        try:
                            Scanner1.align_zero()
                        except:
                            pass
                        try:
                            Scanner2.align_zero()
                        except:
                            pass


        Ultra_Scanner = Scanner("ultra_scanner")
        #Ultra_Scanner.beacon_list = []
        add_all_to_scanner(Ultra_Scanner, Scanners[0])

        for scanner in Scanners[1:]:
             if scanner.have_zero_info:
                #scanner.remap_to_self()
                scanner.align_zero()
                add_all_to_scanner(Ultra_Scanner, scanner)
        #coordinate_dict = compare_coordinates2(Scanners[2], Ultra_Scanner)

        print("Ultra Scanner len: ", Ultra_Scanner.beacon_list.__len__())
        unique = Calculate_unique(Ultra_Scanner.beacon_list)
        this_run = unique.__len__()
        print ("Unique len: ", unique.__len__())
    
    largest = 0
    scanners_len = Scanners.__len__()
    for i in range(scanners_len):
        for j in range(scanners_len - i):
            if (i + j != i):
                Scanner1 = Scanners[i]
                Scanner2 = Scanners[j + i]
                manhattan = calc_manhattan(Scanner1, Scanner2)
                if manhattan > largest:
                    largest = manhattan
    
    print("Largest manhattan: ", largest)

#68 -1246 -43
#88,113,-1104

#-20,-1133,1061

run()


#126 too low
#269 too low

#933 not right

#2916 too high