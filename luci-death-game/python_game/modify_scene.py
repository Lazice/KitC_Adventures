import random
import winsound
import json

script_file = "luci-death-game/data/game_script.json"
progression_file = "luci-death-game/data/game_progression.json"
groupchat_file = "luci-death-game/python_game/groupchat.py"

input_msg = "Please input a number > "
chat_fade = "-----------------------"
creep_down = {"option": "[Creep back downstairs.]", "creeping": True, "location": "mall1"}
idle = {"option": "[Idly wonder what they are buying.]", "jumpto": "2(2)222211", "idle_wonder": True}
creep_down_msg = ["[You creep back downstairs.]", "",
                  "[The shadows of the layer above you, masked by overhead lights, casting a warm glow over the tiled floorings. Dark metallic steel door frames, make contrast with the glass and signage of the other storefronts around, by their signage made of metal. They're right there. You can't see them. But. *They're there*.]"
                    ]
shop_observe = ["[You ponder what they might be buying, staying in spot. Roulx is inside the tools repair workshop.]",
                "[Roulx... Usually utilises tools that are more ordinary for their work. It's rather peculiar to see them ponder items that,, by what you know, seldom in their standard.]"
                ]

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


def update_progress(scene):
    cycle_progress(scene)

    match scene["id"]:
        case "2(2)222":
            if progress["time_passage"]:
                original = scene["msg"]
                scene["msg"] = (["[You enter the mall in hurried steps, to find that, indeed, Roulx is still in the mall.]",
                                 "", "", "[Phew.]", "", "", original])
        case "2(2)22221":
            if progress["location"] == "mall2":
                scene["msg"][0] = "[You make your way up the escalator.]"
        case "2(2)222211":
            scene["options"] = [
                {"option": "[Idly wonder what they are buying.]", "jumpto": scene["id"], "idle_wonder": True},
                {"option": "[Peer into the shop they're at.]", "jumpto": "2(2)2222112"},
                {"option": "[Go talk to them after all.]", "jumpto": "2(1)31", "feign_surprise": True}
                ]
            if progress["location"] == "mall2":
                scene["options"][1] = creep_down
                scene["options"][1]["jumpto"] = "2(2)222211"
                scene["options"][2] = {"option": "[Crane your head over the railing to get a better look.]", "jumpto": "2(2)2222112"}
            if progress["idle_wonder"]:
                scene["msg"] = shop_observe
                scene["options"].remove(idle)
            if progress["creeping"]:
                scene["msg"] = creep_down_msg
                progress["creeping"] = False
        case "2(2)2222112":
            if progress["location"] == "mall2":
                scene["msg"].insert(0, "[You crane your head over the railings, they feel cold under your hands.]")
                scene["msg"].insert(1, "")
                scene["options"].insert(2, creep_down)
                scene["options"][2]["jumpto"] = "2(2)2222112"
                scene["options"][0]["jumpto"] = "2(2)22221121(2)"
            else:
                if progress["creeping"]:
                    scene["msg"] = creep_down_msg
                    progress["creeping"] = False
                    scene["options"].pop(2)
        case "2(1)31":
            if progress["feign_surprise"]:
                scene["msg"].insert(0, "[You approach them with a look of surprise.]")
        case "2(1)33(1)1(2)11":
            if progress["lost"] == False:
                scene["msg"][0] = "[You have retraced your steps.]"
            elif progress["bus"] == True:
                scene["msg"] = scene["msg"][2]
        case "51":
            if progress["finance_theory"]:
                scene["msg"] = "[If you'd like to think that way. Everything looks the same when they're in that category of way too modern offices, just for the sake of efficiency.]"
        case "2(1)33(1)1(2)1122":
            if progress["groupchat"]:
                scene["msg"] = chat_fade
                progress["groupchat"] = False
        case "2(1)33(1)1(2)2(1)11":
            if progress["snow"]:
                if progress["voice_in_head"]:
                    scene["options"][0]["jumpto"] = "2(1)33(1)1(2)2(1)1112"
                else:
                    scene["options"][0]["jumpto"] = "2(1)33(1)1(2)2(1)111"

    if progress["chased"]:
        mark = []
        for counter, option in enumerate(scene["options"]):
            if "chased_option" in option:
                if option["chased_option"] == None:
                    mark.append(counter)
                else:
                    option["option"] = option["chased_option"]
        for counter in mark:
            del scene["options"][counter]
        match scene["id"]:
            case "311132":
                scene["msg"] = [scene["msg"][5], "",
                                "\"Um, so,,, yeah.\" [You ask the waiter for two seats inside, gesturing Roulx to follow.] \"Here would be nice. ...\""
                                ]

    # check if option is added
    counter = 1
    for option in scene["options"]:
        future_id = ""
        if "jumpto" in option:
            if isinstance(option["jumpto"], str):
                future_id = option["jumpto"]
        else:
            future_id = allocate(scene["id"], counter)
        if future_id not in ("", "remember_id", "#") and search_new_scene(future_id, "", False) == None:
            option["option"] += " (OPTION NOT ADDED)"
        counter += 1