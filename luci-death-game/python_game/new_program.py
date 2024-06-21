from modify_scene import *

coin_sound = "Media/coin-toss.wav"
dice_sound = "Media/dice-roll.wav"


def scene_display(statements):
    if isinstance(statements, list):
        msg = "\n".join(statements)
    else:
        msg = scene["msg"]
    print("\n" + msg + "\n")


def error(options):
    if (options != 1):
        print(f"... There are only {options}.")
    else:
        print("... Literally only one option. :|. just decide.")


def roll(option):
    if option["chance"] in ([0.5,0.5], "coin"):
        print("Coin tossed.")
        winsound.PlaySound(coin_sound, winsound.SND_FILENAME)
        outcome = ''.join(random.choices(["Heads", "Tails"]))
        print(outcome  + ".\n")
        if outcome == "Heads":
            return option["jumpto"][0]
        else:
            return option["jumpto"][1]
    else:
        print("Dice rolled.")
        winsound.PlaySound(dice_sound, winsound.SND_FILENAME)
        dice_value = random.randint(1, 20)
        print(str(dice_value) + "\n")
        dice_percentage = dice_value / 20
        counter = 0
        for value in option["chance"]:
            dice_percentage -= value
            if dice_percentage <= 0:
                return option["jumpto"][counter]
            counter += 1
        return option["jumpto"][counter-1]


end_game = False
scene_pos = 0

while not end_game:
    if scene_pos == 0:
        script, progress = reset()
    
    scene = script[scene_pos]
    option_counter = 0

    update_progress(scene)
    scene_display(scene["msg"])

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
            else:
                print("Ts ts ts... Thaat's not a number. yikes! :/")
        elif 1 <= int(ans) <= option_counter:
            chosen_option = scene["options"][int(ans) - 1]
            valid = True
        else:
            error(option_counter)

    # print selected response
    if not dev_mode:
        print(str(ans) + ". " + chosen_option["option"] + "\n")
        cycle_progress(chosen_option)
        if "pre_scene" in chosen_option:
            scene_display(chosen_option["pre_scene"])
        if "remember_id" in chosen_option:
            remember_id = scene["id"]
            print("id remembered: " + remember_id)
        if "jumpto" in chosen_option:
            if isinstance(chosen_option["jumpto"], list):
                id = roll(chosen_option)
            else: id = chosen_option["jumpto"]
        else:
            id = allocate(scene["id"], int(ans))

    print(id)
    scene_pos = search_new_scene(id, remember_id, True)
    if scene_pos == None:
        print("\nSooorry bud, this answer doesn't exist yet :P. Id number: " + id)
        scene_pos = 0