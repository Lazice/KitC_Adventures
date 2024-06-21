import random
import winsound
import copy
from dialogue import *

def error(options):
    if (options != 1):
        print(f"... There are only {options}.")
    else:
        print("... There is literally only one option.")


def reset_memory():
    global chat
    chat = copy.deepcopy(game_chat)
    return original_memory


def modify_memory(id, count):
    global chat_count
    if memory['location'] == 'mall2':
        if id == '2(2)222211':
            chat[count][2] = up_choice1
            chat[count][3] = up_choice2
        elif id == '2(2)2222111':
            chat[count][1] = up_choice1
            chat[count][2] = up_choice2
        elif id == '2(2)2222112':
            chat[count][0] = "[You crane your head over the railings, they feel cold under your hands.]\n" + stalk2
            chat[count].insert(3, up_choice1)
        elif id == '2(2)2222113':
            memory['location'] = 'mall'

    elif id == '2(2)2222112':
        chat[count][0] = stalk2
        if chat[count][3] == up_choice1:
            chat[count].remove(up_choice1)
    elif id == '311131':
        memory['location'] = 'park'
    elif id == '311132':
        memory['location'] = 'cafe'
        if memory['chase'] == True:
            chat[count][0] == f'''{cafe_description}
            “Um, so,,, yeah." [You ask the waiter for two seats inside, gesturing Roulx to follow.] "Here would be nice. ..."'''
    elif id == '311133':
        memory['location'] = 'library'
    elif id == '3111211':
        memory['wedding'] = True
    elif id == '2(2)22222':
        memory['location'] = 'mall2'
        chat_count = search_for_id('2(2)22221')
        chat[chat_count][0] = f'''[You make your way up the escalator.]
{stalk1}'''


def allocate(original_id, ans):
    if original_id == '0':
        return str(ans)
    else:
        return str(original_id) + str(ans)


def roll(original_id):
    if len(original_id[1]) == 2:
        winsound.PlaySound("coin-toss.wav", winsound.SND_FILENAME)
        print("coin toss")
        return ''.join(random.choices(original_id[1], original_id[2]))
    else:
        winsound.PlaySound("dice-roll.wav", winsound.SND_FILENAME)
        dice_value = random.randint(1, 20)
        print("rolled dice: " + str(dice_value))
        dice_percentage = dice_value / 20
        counter = 0
        for value in original_id[2]:
            dice_percentage -= value
            if dice_percentage <= 0:
                return original_id[1][counter]
            counter += 1


def search_for_id(id):
    if id == "#":
        exit()
    for index in range(len(chat)):
        if id == chat[index][-1]:
            return index
    return 0

memory = reset_memory()
while not end_game:
    # print interaction
    print("\n" + chat[chat_count][0] + "\n")

    # list options
    num = len(chat[chat_count]) - 1
    for i in range(1, num):
        if len(chat[chat_count][i]) == 3 or len(chat[chat_count][i]) == 2:
            print(str(i) + ". " + chat[chat_count][i][0])
        else:
            print(str(i) + ". " + chat[chat_count][i])

    # request input from user. if dev_mode triggered, search for id.
    valid = False
    dev_mode = False
    print("")
    while not valid:
        ans = input(input_msg)
        if not dev_mode and not ans.isdigit():
            if ans == 'id':
                dev_mode = True
                id = input("Enter the id you'd like to search for ")
                valid = True
            else:
                print("That's... not a number. bruh =_=")
        elif 1 <= int(ans) < 4:
            valid = True
        else:
            error(num - 1)

    # print selected response
    if not dev_mode:
        if len(chat[chat_count][int(ans)]) == 3:
            print(str(ans) + ". " + chat[chat_count][int(ans)][0])
            id = roll(chat[chat_count][int(ans)])
        elif len(chat[chat_count][int(ans)]) == 2:
            print(str(ans) + ". " + chat[chat_count][int(ans)][0])
            id = chat[chat_count][int(ans)][1]
        else:
            print(str(ans) + ". " + chat[chat_count][int(ans)])
            id = allocate(chat[chat_count][-1], int(ans))

    print(id)
    chat_count = search_for_id(id)
    modify_memory(id, chat_count)
    if chat_count == 0:
        print("\nAnswer doesn't exist yet :P. Id number: " + id)
        memory = reset_memory()
