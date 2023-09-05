counter = 0
g_universes = 0

possible_moves = []
move_dict = {}

class determenistic_die():
    rolls = 0
    nbr = 0
    def roll(self):
        self.rolls +=1
        self.nbr +=1
        if self.nbr == 101:
            self.nbr = 1
        return self.nbr

class Player():
    score = 0
    position = 0


    def __init__(self,name, starting_pos):
        self.name = name
        self.starting_pos = starting_pos
        self.position = starting_pos

    def move(self, amount):
        self.position +=amount
        while self.position>10:
            self.position -= 10
        self.score += self.position

def get_position(position, moves):
    position += moves
    if position> 10:
        position -=10
    return position

def get_dict(score, position, string, turns):
    global counter
    counter +=1
    dict = {}
    turns +=1

    values = move_dict.keys()
    for value in values:
        if score + value >= 21:
            dict[string + str(value)] = turns
        else:
            new_pos = get_position(position, value)
            new_dict = get_dict(score + new_pos, new_pos, string + str(value), turns)
            dict = {**dict, **new_dict}

    return dict

def make_move_dict(starting_nbr):
    score = 0
    position = starting_nbr
    return get_dict(score, position, "", 0)


def game(p1_pos, p1_score, p2_pos, p2_score, p1s_turn):
    p1s_turn = not p1s_turn
    global p1_wins
    global p2_wins
    global possible_moves
    if p1_score >=21:
        p1_wins +=1
        print(p1_wins)
    elif p2_score >=21:
        p2_wins+=1
    else:
        if p1s_turn:
            for p in possible_moves:
                pos = get_position(p1_pos,p)
                game(pos, p1_score+pos,p2_pos, p2_score, p1s_turn)

        else:
            pos_1 = get_position(p2_pos,1)
            pos_2 = get_position(p2_pos,2)
            pos_3 = get_position(p2_pos,3)
            game(p1_pos, p1_score, pos_1, p2_score + pos_1, p1s_turn, )
            game(p1_pos, p1_score, pos_2, p2_score + pos_2, p1s_turn, )
            game(p1_pos, p1_score, pos_3, p2_score + pos_3, p1s_turn, )



def run_games(p1_pos, p2_pos):
    game(p1_pos, 0, p2_pos, 0, True)
    pass


def populate_moves():
    global possible_moves
    for i in range(3):
        for j in range(3):
            for k in range(3):
                possible_moves.append(i+1+j+1+k+1)


def zip_dict(dict1):
    result_dict = {}
    multiplier_dict = {}
    for key, value in dict1.items():
        print(key, value)
        new_key = "".join(sorted(key))
        result_dict[new_key] = value
        if new_key in multiplier_dict:
            multiplier_dict[new_key] += 1
        else:
            multiplier_dict[new_key] = 1

    return result_dict, multiplier_dict


def get_val_from_key(key):
    global move_dict
    sum = 1
    for i in range(key.__len__()):
        char = int(key[i])
        sum *= move_dict[char]
    return sum


def run ():
    print("".join(sorted("312")))
    #file = open("day21")
    player1 = Player("p1", 2)
    player2 = Player("p2", 7)
    die = determenistic_die()

    game_over = False
    while not game_over:
        move = 0
        for i in range(3):
            move += die.roll()

        player1.move(move)
        if player1.score >= 1000:
            game_over = True
            break
        if not game_over:
            move = 0
            for i in range(3):
                move += die.roll()
            player2.move(move)
            if player2.score >= 1000:
                game_over = True
                break

    print("result = ", min(player1.score, player2.score)* die.rolls)
    populate_moves()
    global possible_moves
    global move_dict
    for move in possible_moves:
        if move in move_dict:
            move_dict[move] +=1
        else:
            move_dict[move] = 1
    print (move_dict)
    p1_win = {}
    p2_win = {}
    p1_lose = {}
    p2_lose = {}
    #Part 2
    dict1 = make_move_dict(4)
    dict2 = make_move_dict(8)
    dict1, new_dict1_multiplier = zip_dict(dict1)
    dict2, new_dict2_multiplier = zip_dict(dict2)
    counter = 1
    for key, value in dict1.items():
        counter +=1
        print(counter / 2500)
        #print(counter / 18253)
        for key2, value2 in dict2.items():
            if value2 < value:
               if key2 in p2_win:
                   p2_win[key2] += 1
               else:
                   p2_win[key2] = 1
               if key in p1_lose:
                   p1_lose[key] += 1
               else:
                   p1_lose[key] = 1
            else:
                if key in p1_win:
                    p1_win[key] += 1
                else:
                    p1_win[key] = 1
                if key2 in p2_lose:
                    p2_lose[key2] += 1
                else:
                    p2_lose[key2] = 1

    m = move_dict
    p1_wins = 1
    for key, value in p1_win.items():
        p1_wins += value * get_val_from_key(key) * new_dict1_multiplier[key]
    print(p1_wins)
    print(1171842459269*(3**6))
    print(117137064798*(3**6))
    print(444356092776315)


run()