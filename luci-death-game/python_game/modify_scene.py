import random
import winsound
import json

script_file = "luci-death-game/data/game_script.json"
progression_file = "luci-death-game/data/game_progression.json"
groupchat_file = "luci-death-game/python_game/groupchat.py"

input_msg = "Please input a number > "

pen_names = {
    "b": "MrBlueSky",
    "w": "\u2727\u22C6WELCOME TO THE BLACK PARADE\u22C6\u2727",
    "y": "goodbyeyellowbrickroad",
    "r": "girl in red"
    }

irl_names = {
    "r:": "Roulx:"
}

remember_id = ""
script = []
progress = {}

#reset progress at the start of every game
def reset():
  global script, progress
  with open(script_file, "r") as f1:
    script = json.load(f1)
  with open(progression_file, "r") as f2:
    progress = json.load(f2)
  return script, progress


def option_check(scene):
    counter = 1
    for option in scene["options"]:
        future_id = ""
        if "pop" in option:
            continue
        if "jumpto" in option:
            if isinstance(option["jumpto"], str):
                future_id = option["jumpto"]
        else:
            future_id = allocate(scene["id"], counter)
        if future_id not in ("", "remember_id", "#") and search_new_scene(future_id, "", False) == None:
            option["option"] += " (OPTION NOT ADDED)"
        counter += 1


def allocate(original_id, ans):
    if original_id == '0':
        return str(ans)
    else:
        return str(original_id) + str(ans)


def search_new_scene(id, remember_id, end_game):
    if id == "#" and end_game:
        exit()
    if id == "remember_id":
        id = remember_id
    for index in range(len(script)):
        if id == script[index]["id"]:
            return index
    return None


def cycle_progress(lst):
    for key in progress.keys():
        if key in lst:
            progress[key] = lst[key]
            print(key + " set to " + str(progress[key]))


def abbreviate2(shorthand, msg, divider):
    for key in shorthand.keys():
        if msg.startswith(key):
            return shorthand[key] + divider + msg[len(key):]
    return msg
        

def abbreviate(shorthand, scene, divider):
    if isinstance(scene["msg"], list):
        for counter, msg in enumerate(scene["msg"]):
            scene["msg"][counter] = abbreviate2(shorthand, msg, divider)
    else:
        scene["msg"] = abbreviate2(shorthand, scene["msg"], divider)


def hitlist(scene, label):
    for counter, option in reversed(list(enumerate(scene["options"]))):
        if label in option:
            del scene["options"][counter]


def update_progress(scene):
    cycle_progress(scene)

    if progress["mode"] == "chat":
        abbreviate(pen_names, scene, ":")
    else:
        abbreviate(irl_names, scene, "")

    match scene["id"]:
        case "2(2)222":
            if progress["time_passage"]:
                scene["msg"] = (["[You enter the mall in hurried steps, to find that, indeed, Roulx is still in the mall.]",
                                 "", "", "[Phew.]", "", "", scene["msg"]])
        case "2(2)222211":
            if progress["location"] == "mall1":
                hitlist(scene, "flagged")
                scene["options"].extend([{"option": "[Peer into the shop they're at.]", "jumpto": "2(2)2222112", "flagged": True},
                                        {"option": "[Go talk to them after all.]", "jumpto": "2(1)31", "feign_surprise": True, "flagged": True}
                                        ])
        case "2(2)2222112":
            if progress["location"] == "mall2":
                scene["options"][0]["jumpto"] = "2(2)22221121(2)"
            else:
                scene["options"][1]["roll_special"] = {"type": "advantage", "reason": "being downstairs"}
        case "2(1)31":
            if progress["feign_surprise"]:
                scene["msg"].insert(0, "[You approach them with a look of surprise.]")
        case "2(1)33(1)1(2)2(2)111111":
            if progress["snow"]:
                scene["msg"].extend(["[You wonder even why you need to kill.]"])
        case "01" | "03":
            if progress["painkillers"] > 0:
                scene["msg"].extend(["",
                    "And now you just have painkillers in your pocket that you don't need! (you know who you bought it for don't you)"
                    ])
        case "411111":
            if progress["friend"]:
                del scene["msg"][:2]
        case "2(2)22221122":
            match progress["alter_next"]:
                case 0:
                    scene["msg"].append("1")
                case 1:
                    scene["msg"][3] = "\"      May       what            is?\""
                    scene["msg"][4] = "\"It's a       . But         need         its           .\""
                    scene["msg"][5] = "\"    where might                    \""
                    scene["msg"][7] = "\"             \""
                    scene["msg"][8] = "\"That's              can le            and    you                          information,               done                    \""
                    del scene["msg"][6]
                    del scene["msg"][2]
                case 2:
                    scene["msg"].append("3")
                case 3:
                    scene["msg"].append("4")

    if progress["chased"]:
        for counter, option in reversed(list(enumerate(scene["options"]))):
            if "chased_option" in option:
                if option["chased_option"] == None:
                    del scene["options"][counter]
                else:
                    option["option"] = option["chased_option"]
        match scene["id"]:
            case "311132":
                scene["msg"] = [scene["msg"][5], "",
                                "\"Um, so,,, yeah.\" [You ask the waiter for two seats inside, gesturing Roulx to follow.] \"Here would be nice. ...\""
                                ]


    if progress["replace_all"]:
        scene["msg"] = progress["replace_all"]
        progress["replace_all"] = ""


    if progress["replace"] != {}:
        for key in progress["replace"]:
            scene["msg"][int(key)] = progress["replace"][key]
        progress["replace"] = {}

    
    if progress["insert"] != {}:
        for key in progress["insert"]:
            scene["msg"].insert(int(key), progress["insert"][key])
        progress["insert"] = {}


    if progress["del"] != []:
        for key in reversed(progress["del"]):
            del scene["msg"][key]
        progress["del"] = {}


    for counter, option in reversed(list(enumerate(scene["options"]))):
        if "prereq" in option:
            for key in option["prereq"]:
                if option["prereq"][key] != progress[key]:
                    del scene["options"][counter]
        

    # check if option is added
    option_check(scene)