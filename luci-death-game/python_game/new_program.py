from modify_scene import *

coin_sound = "luci-death-game/Media/coin-toss.wav"
dice_sound = "luci-death-game/Media/dice-roll.wav"


def scene_display(statements):
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


def option_effects(option, scene, option_index):
    global remember_id
    cycle_progress(chosen_option)
    if "pre_scene" in option:
        scene_display(option["pre_scene"])
    if "remember_id" in option:
        remember_id = scene["id"]
        print("id remembered: " + remember_id)
    if "pop" in option:
        del scene["options"][option_index]
        option["jumpto"] = scene["id"]
        scene["msg"] = option["pop"]
    if "jumpto" in option:
        if isinstance(option["jumpto"], list):
            return roll(option)
        elif option["jumpto"] == "01" and progress["snow"]:
            if progress["voice_in_head"]:
                return "0312"
            else:
                return "031"
        else: 
            return option["jumpto"]
    else:
        return allocate(scene["id"], option_index + 1)


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