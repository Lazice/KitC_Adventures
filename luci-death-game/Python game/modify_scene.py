import random
import winsound
import json

script_file = "data/game_script.json"
progression_file = "data/game_progression.json"

input_msg = "Please input a number > "
up_choice1 = ['[Creep back downstairs.]', '2(2)2222113']
up_choice2 = ['[Crane your head over the railing to get a better look.]', '2(2)2222112']
stalk1 = "[Roulx has moved from their previous position, but as you peer around for even the tint of white, you spot them. They've gone strolling down the corridor, gazing pensively over the glass fronts of luxury items.]"
stalk2 = "[Their bright figure is distinctive in the scarcely visited workshop. Peering, they take only short glances of the complicated parts and charts and diagrams on the walls. But an item they take out of their decorated tote bag catches your attention. A gloved hand, holding up a small, grey, staff-like item, conducting quiet chatter with the facilitator from the desk - which you cannot tell what they're talking about from your position, as their back is turned towards you.]"
cafe_description = "[It’s about an 8 minute walk from where you are until you reach a slightly less populated suburban area, where a stylish cafe stands with a raised wooden deck and circular white tables and parasols on its outside. The name “Haven’s Parrot” is written in a chocolatey brown font on its front in cursive. There are some people at this time of day but it is not entirely packed, and there’s plenty of polished wooden tables and orange cushions to sit at on the inside.]"


#reset progress at the start of every game
def reset():
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


def search_new_scene(id, script):
    if id == "#":
        exit()
    for index in range(len(script)):
        if id == script[index]["id"]:
            return index
    return 0


def update_progress(scene, progress, script):
    for key in progress.keys():
        if key in scene:
            progress[key] == scene[key]
            print(key + " set to " + progress[key])

    # check if option is added
    counter = 1
    for option in scene["options"]:
        future_id = ""
        if "jumpto" in option:
            if isinstance(option["jumpto"], str):
                future_id = option["jumpto"]
        else:
            future_id = allocate(scene["id"], counter)
        if future_id and search_new_scene(future_id, script) == 0:
            option["option"] += " (OPTION NOT ADDED)"
        counter += 1

    if progress["location"] == "mall2":
        match scene["id"]:
            case "2(2)222211":
                scene["options"][1] = up_choice1
                scene["options"][2] = up_choice2
            case "2(2)2222111":
                scene["options"] = up_choice1, up_choice2
            case "2(2)2222112":
                scene["msg"] = "[You crane your head over the railings, they feel cold under your hands.]\n" + stalk2
                scene["options"].append({"option": up_choice1})
            case "2(2)2222113":
                progress["location"] = "mall"

    match scene["id"]:
        case "2(2)2222112":
            scene["msg"] = stalk2
            if {"option": up_choice1} in scene["options"]:
                scene["options"].remove({"option": up_choice1})
        case "311132":
            if progress['chase'] == True:
                scene["msg"] == f'''{cafe_description}
            “Um, so,,, yeah." [You ask the waiter for two seats inside, gesturing Roulx to follow.] "Here would be nice. ..."'''
        case "2(2)22222":
            progress["location"] = "mall2"
            scene_pos = search_new_scene("2(2)22221")
            script[scene_pos]["msg"] = f'''[You make your way up the escalator.]
        {stalk1}'''
        # case "311131":
        #     progress['location'] = 'park'
        # case "311133":
        #     progress['location'] = 'library'