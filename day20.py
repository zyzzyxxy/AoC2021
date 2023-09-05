def convert_to_decimal(str_nbr):
    nbr = int(str_nbr, 2)
    return nbr


def expand_image(input_image, extra):
    row_len = input_image.__len__()
    col_len = input_image[0].__len__()
    image = [["." for i in range(col_len + 2*extra)] for j in range(row_len + 2*extra) ]
    for i in range(row_len):
        for j in range(col_len):
            image[i+extra][j+extra] = input_image[i][j]
    return image



def process_inputimage(input_image, iealgo, extra):
    input_image = expand_image(input_image,extra)
    # for line in input_image:
    #     print(line)
    row_len = input_image.__len__()
    col_len = input_image[0].__len__()
    output_image = [["" for i in range(col_len)] for j in range(row_len) ]
    for row in range(row_len-2):
        row += 1
        for col in range(col_len-2):
            str_nbr = ""
            got_value = False
            col +=1
            for i in range(3):
                for j in range(3):
                    r = row + i - 1
                    c = col + j - 1
                    if r >=1 and r < row_len-1 and c >= 1  and c < col_len-1:
                        got_value = True
                        sign = input_image[r][c]
                        if sign == "#":
                            str_nbr +="1"
                        else:
                            str_nbr += "0"
                    # else:
                    #     str_nbr +="0"
            if got_value:
                nbr = convert_to_decimal(str_nbr)
                #print(nbr)
                sign = iealgo[nbr]
                output_image[row][col] = str(sign)
    return output_image

def process_inputimage2(input_image, iealgo):
    input_image = expand_image(input_image,5)
    # for line in input_image:
    #     print(line)
    row_len = input_image.__len__()
    col_len = input_image[0].__len__()
    output_image = [["" for i in range(col_len)] for j in range(row_len) ]
    for row in range(row_len):
        for col in range(col_len):
            str_nbr = ""
            for i in range(3):
                for j in range(3):

                    r = row + i - 1
                    c = col + j - 1
                    if r >=0 and r < row_len and c >= 0  and c < col_len:
                        sign = input_image[r][c]
                        if sign == "#":
                            str_nbr +="1"
                        else:
                            str_nbr += "0"
                    else:
                        str_nbr +="0"
            nbr = convert_to_decimal(str_nbr)
            #print(nbr)
            sign = iealgo[nbr]
            output_image[row][col] = str(sign)
    return output_image


def calc_chars(output_image, param):
    result = 0
    for line in output_image:
        for char in line:
            if char == param:
                result +=1
    return result


def strip_image(output_image, strip_size):
    row_len = output_image.__len__()
    col_len = output_image[0].__len__()
    image = [["." for i in range(col_len)] for j in range(row_len )]
    for i in range(output_image.__len__() - strip_size * 2):
        for j in range(output_image[0].__len__() - strip_size * 2):
            image[i][j] = output_image[i+strip_size][j+strip_size]
    return image




def run():
    file = open("day20")
    iealgo, input_image = file.read().split("\n\n")
    input_image = input_image.splitlines()
    output_image = process_inputimage2(input_image, iealgo)
    output_image = process_inputimage2(output_image, iealgo)
    output_image = strip_image(output_image, 6)
    result = calc_chars(output_image, "#")
    print(result)
    for i in range(24):
        print(i)
        output_image = process_inputimage2(output_image, iealgo)
        output_image = process_inputimage2(output_image, iealgo)
        output_image = strip_image(output_image, 6)
    #
    for line in output_image:
        print(line)
    #ddres_image = strip_image(output_image, 6)
    result = calc_chars(output_image, "#")
    print(result)


run()


#6214 too high
#5826 too high
#5406 wrong
#5380 wrong
#4962 too low


#right 5218

# toot high 129185

