import os


def run():
    config_filename = os.getcwd() + "/day2"
    file = open(config_filename, 'r').read()
    arr = file.splitlines();
    horisontal = 0
    depth = 0
    aim = 0
    for item in arr:
        tuple = item.split(" ")
        direction = tuple[0]
        size = int(tuple[1])
        if(direction == "down"):
            aim +=size
        if(direction == "forward"):
            horisontal += size
            depth +=size*aim
        if(direction == "up"):
            aim -=size
    print('h ', horisontal)
    print('d ', depth)
    print(horisontal*depth)

if __name__ == '__main__':
    run()