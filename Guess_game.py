import random
import math

print("To Play The Game Type 'guess_game() Into The Terminal")
print("\t You may choose a difficulty from 1-3 inserting value in the bracket"
      + "(three being the easiest) '")


def list_setup():
    file = open("Leaderbaord.txt", "r")
    file_text = file.read()
    file.close()
    file_text = file_text[1:-1]
    file_list = []
    acc = 0
    if len(file_text) == 0:
        return []
    file_text = file_text.replace("'", "")
    for i in range(len(file_text)):
        sub = []
        rest = []
        if file_text[i] != "]":
            if file_text[i] == "[":
                p = file_text.find("]", i + 1)
                rest = file_text[i + 1: p]
                sub = rest.split(",")
                sub[0] = int(sub[0])
                sub[1] = int(sub[1])
                sub[3] = int(sub[3])
                acc += 1
                file_list.append(sub)
    leader_list = file_list
    leader_list.sort()
    return leader_list


leader_list = list_setup()


def guess_game(difficulty=0) -> None:
    if difficulty != 0:
        difficulty -= 1
    while difficulty not in range(0, 3):
        text = "Please enter a vaild difficult form 1-3 inclusive."
        difficulty = must_be_int(input(text))
    nums = get_low_high()
    low = nums[0]
    high = nums[1]
    num = random.randint(low, high)
    num_guesses = guesser(num, low, high, difficulty)
    leaderboard_text(low, high, num_guesses, difficulty)
    return None


def guesser(num: int, low: int, high: int, difficulty: int) -> int:
    guess = must_be_int(input("\nGuess the number between " + str(low) + " and "
                              + str(high)))
    old_guess = guess
    num_guesses = 1
    while guess != num:
        if guess == "Exit":
            break
        if guess not in range(low, high + 1):
            old_guess = guess
            guess = must_be_int(input(
                "\n Invalid Number, picked number must be from " + str(low)
                + ", " + str(high)))
        elif guess > num and difficulty == 1:
            old_guess = guess
            guess = must_be_int(input("Nope too high, try again"))
        elif guess < num and difficulty == 1:
            old_guess = guess
            guess = must_be_int(input("Nope too low, try again"))
        elif guess > num and difficulty == 2:
            if old_guess < guess:
                guess = must_be_int(
                    input("Nope too high, Warmer tho, try again"))
            elif old_guess > guess:
                old_guess = guess
                guess = must_be_int(input("Nope too high, Colder, try again"))
            else:
                old_guess = guess
                guess = must_be_int(input("Nope, try again"))
        elif guess < num and difficulty == 2:
            if old_guess > guess:
                old_guess = guess
                guess = must_be_int(
                    input("Nope too low, Warmer tho, try again"))
            elif old_guess < guess:
                old_guess = guess
                guess = must_be_int(input("Nope too low, Colder, try again"))
            else:
                old_guess = guess
                guess = must_be_int(input("Nope, try again"))
        else:
            old_guess = guess
            guess = must_be_int(input("Nope, try again"))
        num_guesses += 1
    return num_guesses


def get_low_high() -> list[int]:
    while True:
        low = 0
        high = 0
        a = input("Pick a range of numbers ex:1,5 or -10,10: ")
        a = a.replace(" ", "")
        if "," in a:
            if a[:a.find(",")].isnumeric() and a[a.find(",") + 1:].isnumeric():
                if int(a[:a.find(",")]) > int(a[a.find(",") + 1:]):
                    high = int(a[:a.find(",")])
                    low = int(a[a.find(",") + 1:])
                else:
                    low = int(a[:a.find(",")])
                    high = int(a[a.find(",") + 1:])
                break
            elif "-" in a:
                b = a.replace("-", "")
                if b[:b.find(",")].isnumeric() and b[
                                                   b.find(
                                                       ",") + 1:].isnumeric():
                    if int(a[:a.find(",")]) > int(a[a.find(",") + 1:]):
                        high = int(a[:a.find(",")])
                        low = int(a[a.find(",") + 1:])
                    else:
                        low = int(a[:a.find(",")])
                        high = int(a[a.find(",") + 1:])
                    break
        else:
            print("\n Error: Invalid Entery \n")
            continue
    return [low, high]


def must_be_int(s1: str) -> int:
    s2 = s1.replace("-", "")
    while not s2.isnumeric():
        s1 = input("\n Invalid Number, picked number must be a number")
        if s1 == "Exit":
            return "Exit"
        s2 = s1.replace("-", "")

    return int(s1)


def leaderboard_text(low: int, high: int, num_guesses: int,
                     difficulty: int) -> None:
    if num_guesses == 1:
        trys = "It only took " + str(num_guesses) + " try. WOW!!!"
    else:
        trys = "It only took " + str(num_guesses) + " trys"
    wining_text = "\n {:<10} \n {:<10}".format("Congrats!!!", trys)
    print(wining_text)
    name = input("name?")
    while "[" in name or "]" in name:
        name = input("No paranthesis, name?")
    length = len(range(low, high)) + 1
    leader_list.append([length, num_guesses, name, difficulty + 1])
    leader_list.sort()
    file = open("Leaderbaord.txt", "w")
    file.write(str(leader_list))
    file.close()
    leader = 1
    text = "WINNERS IN THE CATAGORY OF RANGE " + str(length)
    print(text + " AT DIFFICULTY " + str(difficulty + 1) + "\n")
    print("{:}{:^10}{:>5}".format("Rank:", "Name,", "Guesses"))
    for i in range(len(leader_list)):
        if length == leader_list[i][0] and difficulty + 1 == leader_list[i][3]:
            winner = "\t{:>5}, {:>8}".format(leader_list[i][2],
                                             leader_list[i][1])
            print(str(leader) + ": " + winner)
            leader += 1
    return None


def display_leaderboard():
    leaderboard = list_setup()
    leaderboard.sort()
    a = []
    for i in range(len(leaderboard)):
        for k in range(len(a) + 1):
            if (k != len(a) or len(a) == 0 or (a[k][0] != leaderboard[i][0] and
                                               a[k][3] != leaderboard[i][3])):
                text = "WINNERS IN THE CATAGORY OF RANGE " + str(
                    leaderboard[i][0])
                print("\n" + text + " AT DIFFICULTY " + str(
                    leaderboard[i][3] + 1) + "\n")
                print("{:}{:^10}{:>5}".format("Rank:", "Name,", "Guesses"))
                leader = 1
                for j in range(len(leaderboard)):
                    if (leaderboard[i][0] == leaderboard[j][0] and
                            leaderboard[i][3] == leaderboard[j][3]):
                        winner = "\t{:>5}, {:>8}".format(leader_list[j][2],
                                                         leader_list[j][1])
                        print(str(leader) + ": " + winner)
                        a.append(leaderboard[i])
                        leader += 1
            break
