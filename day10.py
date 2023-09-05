

'''

): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.

'''

brackets = {
    "{":"}",
    "[":"]",
    "(":")",
    "<":">"
}
bracket_points = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}
bracket_points_2 = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
}
class Line():
    def __init__(self):
        self.line = ""
        self.opening_brackets = []
        self.closing_brackets = []
        self.first_invalid = ""
        self.corrupted = False
        self.incomplete = False

    def get_score(self):
        if self.first_invalid !="":
            return bracket_points[self.first_invalid]

    def get_atutocomplete_score(self):
        for i in range(len(self.opening_brackets)):
            self.closing_brackets.append(brackets[self.opening_brackets[-i-1]])
        print (self.closing_brackets.__len__(), self.opening_brackets.__len__())
        sum = 0
        for b in self.closing_brackets:
            sum *=5
            sum+=bracket_points_2[b]
        return sum


def calc_line(line):
    length = line.closing_brackets.__len__()
    for i in range(length):
        ob = line.opening_brackets[-i -1]
        cb = line.closing_brackets[i]
        if brackets[ob] != cb:
            line.corrupted = True
            line.first_invalid = cb
            break




def get_corrupted_lines(lines):
    corrupted_lines = []
    incomplete_lines = []
    processed_lines = []
    for l in lines:
        line = Line()
        line.line = l
        keys = brackets.keys()
        vals = brackets.values()
        for i in range(l.__len__()):
            if l[i] in keys:
                line.opening_brackets.append(l[i])
            elif l[i] in vals:
                cb = l[i]
                ob = line.opening_brackets.pop()
                expected = brackets[ob]
                if cb != expected:
                    line.first_invalid = l[i]
                    line.corrupted = True
                    break
                #line.closing_brackets.append(l[i])
        processed_lines.append(line)

    for l in processed_lines:
        #calc_line(l)
        print(l.opening_brackets.__len__() - l.closing_brackets.__len__() )

    sum = 0
    scores = []
    for l in processed_lines:
        if(l.corrupted):
            sum += l.get_score()
        else:
            scores.append(l.get_atutocomplete_score())
    print (sum)
    scores.sort()
    print(scores)
    print(scores.__len__())
    print(scores[scores.__len__()//2])

def run():
    file = open("day10")
    lines = file.read().splitlines()
    print(lines)

    corrupted_lines = get_corrupted_lines(lines)




run()

#379830 too high

#195831 too low


# 2
#336274154469 too high