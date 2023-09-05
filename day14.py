rule_dict = {}
element_dict = {}
from pandas import DataFrame

global_pairs = {}

def calc_elements(value):
    global element_dict
    for i in range(value.__len__()):
        char = value[i]
        element_dict[char] +=1


def calc_elements_from_dict():
    first_key = list(global_pairs.keys())
    first_key = first_key[0]
    val = global_pairs[first_key]

    element_dict[first_key[0]] += val

    for key in global_pairs.keys():
        val = global_pairs[key]
        element_dict[key[1]] += val
        print (element_dict)


def fill_global_dict(lines):
    global element_dict
    global global_pairs
    values = []
    for key in rule_dict.keys():
        c1 = key[0]
        c2 = key[1]
        global_pairs[c1+c2]=1



def run():
    global rule_dict
    global element_dict
    global global_pairs
    file = open("day14")
    lines = file.read().splitlines()
    start_value = lines[0]
    for i in range(start_value.__len__()):
        element_dict[start_value[i]] = 0

    for line in lines[2:]:
        key, value = line.split(" -> ")
        rule_dict[key] = value
        element_dict[key[0]] = 0
        element_dict[key[1]] = 0

    print(element_dict)
    print(rule_dict)

    value = start_value
    first_char = value[0]
    #fill_global_dict(lines)
    pairs = []
    for j in range(value.__len__() - 1):
        pairs.append([value[j], value[j + 1]])
    for pair in pairs:
        if pair[0] + pair[1] not in global_pairs.keys():
            global_pairs[pair[0] + pair[1]] = 1
        else:
            global_pairs[pair[0] + pair[1]] += 1
    for i in range(value.__len__()):
        val = value[i]
        element_dict[val]+=1

    print (element_dict)
    for i in range(40):
        temp_dict = global_pairs.copy()
        for key in global_pairs.keys():
            x=element_dict
            multiplier = global_pairs[key]
            if multiplier>0:
                insert_val = rule_dict[key]
                if key[0] + insert_val not in temp_dict.keys():
                    temp_dict[key[0] + insert_val] = 0
                if insert_val + key[1] not in temp_dict.keys():
                    temp_dict[insert_val + key[1]] = 0
                first_char = key[0]
                second_char = key[1]
                temp_dict[first_char + insert_val] += multiplier
                temp_dict[insert_val + second_char] += multiplier
                temp_dict[key] -= multiplier
                element_dict[insert_val] += multiplier

        global_pairs = temp_dict.copy()
        #value = result
    #calc_elements(value)
    #calc_elements_from_dict()
    print(element_dict)
    print(value.__len__())
    for key in element_dict.keys():
        print(key, element_dict[key])
    end_val = max(element_dict.values()) - min(element_dict.values())
    print(end_val)
    ##2489051461161 too low
    ##2589051461161 too low
    ##4978002883718 too High



run()