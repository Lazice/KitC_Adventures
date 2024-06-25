from dialogue import game_chat
import json

class Dialogue:
  def __init__(self, id, msg, options):
    self.id = id
    self.msg = msg
    new_options = []
    for option in options:
      if len(option) == 3:
        new_options.append({"option": option[0], "jumpto": option[1], "chance": option[2]})
      elif len(option) == 2:
        new_options.append({"option": option[0], "jumpto": option[1]})
      else:
        new_options.append({"option": option})
    self.options = new_options

with open("game_script.json", "w") as f:
  scenes = []
  for i in range(len(game_chat)):
    chat = Dialogue(game_chat[i][-1], game_chat[i][0], game_chat[i][1:-1])
    scenes.append(chat.__dict__)
  print(scenes)
  json.dump(scenes, f, indent=4)