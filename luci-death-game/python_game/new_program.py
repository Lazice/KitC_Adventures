from modify_scene import *
import time

coin_sound = "luci-death-game/Media/coin-toss.wav"
dice_sound = "luci-death-game/Media/dice-roll.wav"


def pause_words(statements):
    print("\n")
    for msg in statements:
        sleep_time = 0
        if msg.startswith("~"):
            sleep_time = int(msg[1])
        print(msg[2:])
        time.sleep(int(sleep_time))
    print("\n")


def scene_display(statements, bool):
    if bool:
        pause_words(statements)
        return
    if isinstance(statements, list):
        msg = "\n".join(statements)
    else:
        msg = statements
    print("\n" + msg + "\n")


def error(options):
    if (options != 1):
        print(f"... There are only {options}.")
    else:
        print("... Literally only one option. :|. just decide.")


def coin():
    winsound.PlaySound(coin_sound, winsound.SND_FILENAME)
    outcome = ''.join(random.choices(["Heads", "Tails"]))
    print(outcome)
    if outcome == "Heads":
        return 0
    else:
        return 1
    

def dice(option):
    winsound.PlaySound(dice_sound, winsound.SND_FILENAME)
    dice_value = random.randint(1, 20)
    print(str(dice_value))
    dice_percentage = dice_value / 20
    counter = 0
    for value in option["chance"]:
        dice_percentage -= value
        if dice_percentage <= 0:
            return counter
        counter += 1
    return counter-1


def roll(option):
    option_num = []
    count = 1
    special = None
    if option["chance"] in ([0.5,0.5], "coin"):
        base_msg = "Coin tossed"
    else:
        base_msg = "Dice rolled"
    if "roll_special" in option:
        special = option["roll_special"]
        count = 2
        print(base_msg + " with " + special["type"] + " due to " + special["reason"] + ".")
    else:
        print(base_msg + ".")
    
    for i in range(count):
        if option["chance"] in ([0.5,0.5], "coin"):
            option_num.append(coin())
        else:
            option_num.append(dice(option))
    print("")
    option_num.sort()
    if special and special["type"] == "advantage":
        return option_num[-1]
    return option_num[0]


def option_effects(option, scene, option_index):
    global remember_id
    cycle_progress(chosen_option)
    if "pre_scene" in option:
        scene_display(option["pre_scene"], False)
    if "remember_id" in option:
        remember_id = scene["id"]
        print("id remembered: " + remember_id)
    if "pop" in option:
        del scene["options"][option_index]
        option["jumpto"] = scene["id"]
        scene["msg"] = option["pop"]
    if "alter_next" in option:
        progress["alter_next"] = roll(option)
    if "jumpto" in option:
        if isinstance(option["jumpto"], list):
            id_index = roll(option)
            return option["jumpto"][id_index]
        if option["jumpto"] == "01" and progress["snow"]:
            if progress["voice_in_head"]:
                return "0312"
            return "031"
        return option["jumpto"]
    return allocate(scene["id"], option_index + 1)


end_game = False
scene_pos = 0

while not end_game:
    if scene_pos == 0:
        script, progress = reset()
    
    scene = script[scene_pos]
    option_counter = 0

    update_progress(scene)
    scene_display(scene["msg"], "snow" in scene)

    # list options
    for option in scene["options"]:
        option_counter += 1
        print(str(option_counter) + ". " + option["option"])
    
    print("")

    valid = False
    dev_mode = False
    # request input from user.
    while not valid:
        ans = input(input_msg)
        # if dev_mode triggered, search for id.
        if not dev_mode and not ans.isdigit():
            if ans == 'id':
                dev_mode = True
                id = input("pls enter the id you want to search for :3 ")
                valid = True
            elif ans == 'help':
                print("Easy! Just pick one of the numbers from the options above and follow along with the story, ya know? :3")
            elif ans in ['quit', 'exit', 'bye']:
                exit()
            else:
                print("Ts ts ts... Thaat's not a number. yikes! :/")
        elif 1 <= int(ans) <= option_counter:
            option_index = int(ans) - 1
            chosen_option = scene["options"][option_index]
            valid = True
        else:
            error(option_counter)

    # print selected response
    if not dev_mode:
        print(str(ans) + ". " + chosen_option["option"] + "\n")
        id = option_effects(chosen_option, scene, option_index)

    print(id)
    scene_pos = search_new_scene(id, remember_id, True)
    if scene_pos == None:
        print("\nSooorry bud, this answer doesn't exist yet :P. Id number: " + id)
        scene_pos = 0