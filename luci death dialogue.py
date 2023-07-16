def error(options):
    if (options != 1):
        print(f"... There are only {options}.")
    else:
        print("... There is literally only one option.")

def allocate(dialogue, ans):
    if dialogue == 0:
        if ans == 3:
            return 1
        else:
            print("Answer doesn't exist yet :P.")
            return 0
    elif dialogue == 1:
        if ans == 1:
            return 2
        else:
            print("Answer doesn't exist yet :P.")
            return 0
    elif dialogue == 2:
        if ans == 1:
            return 3
    elif dialogue == 3:
        if ans == 1:
            return 4
    elif dialogue == 4:
        if ans == 2:
            return 5
    elif dialogue == 5:
        if ans == 1:
            return 6
    elif dialogue == 6:
        if ans == 1:
            return 7
    elif dialogue == 7:
        if ans == 2:
            return 8
    elif dialogue == 8:
        if ans == 3:
            return 9
    elif dialogue == 9:
        if ans == 2:
            return 10
    elif dialogue == 10:
        if ans == 1:
            return 11
    elif dialogue == 11:
        if ans == 2:
            return 12
    else:
        print("Answer doesn't exist yet :P.")
        return 0
    
#3-1-1-1-2-1-2-3-2-1-1

input_msg = "Please input a number --> "
end_game = False
chat_count = 0

chat = [
['''greetings
[Roulx stands in front of you, distant, familiar, close. It has been some years after, since it all happened... The people, the scheming, the lights. Isn't it all more than a memory?]
[They stand there in front of you, seemingly stunned as the tapping of their fingers stands frozen mid-action.]''',
    '[Pretend not to notice.]',
    '[Begin to walk away.]',
    '"... Roulx?"'],

['''Ki seemed to shiver at that. Barely noticeable, but you've known kime for long enough.]
Roulx: "Olive? You're here!"
[They smile, relieved as they comprehend your presence.]''',
    '[Smile back.]',
    '[Leave. This was a bad idea.]',
    '"..."'],

['''[You smile back at them. They are your friend. Smiling is the polite thing to do.]
Roulx: "How have you been?"
[It stands, the two its hands gloved, clasped in front of itself idly.]
"..."''',
    '"...Roulx. I\'m not Olive."'],

['''[Their smile lowers, but doesn't disappear as they tilt their head.]
Roulx: "What do you mean? ... You look just like him?"
"Autumn. My name is Autumn. You must have confused me for someone else."
Roulx: "Autumn? You're Autumn?.. Do you,, well you don't but... Do you know of someone by the name Olive Stanford?"''',
    '"No. I do not."'],

['''Roulx: "...Alright..."
[It shifts in its stance. Looking down to the side... It wears the same white suit and outfit from the very before, yellow bow tie sitting in the exact same.] 
Roulx: "Well, nice to meet you Autumn, though you already know my name." 
[Roulx reaches out a gloved right hand, to shake in polite greeting.]
[You shake hands. It is a familiar feeling, a warm feeling. Having an ally on your side.]
"Nice to meet you too, Roulx."''',
    '"How are you?"',
    '"Why are you here?"',
    '"Could we talk somewhere else? I\'m not a big fan of crowded areas."'],

['''[They look around, the store seems spacious, Roulx themself have new earrings and a shoulder tote bag of books and trinkets.] 
Roulx: "I'm only here to buy things for my Hugo. We're stopping near by for sightseeing and business." 
[They shrug. A swing and there some badges and trinkets clink against each other on the surface of their bag.]''',
    '"I like your earrings."',
    '"Those badges look lovely. They suit you."',
    '"Hugo? Are they your partner?"',
    '"Looks like you\'ve bought quite a bit. Are you looking for anything else?"'],

['''Roulx: "Thanks! These are new, my partner gave me them for our anniversary last year."
 [Gold in material, the left one is a delicate replication of a moon. Simple, small and sways side to side as it tilts in its expressiveness. The right one, much more complicated, rings engraved with patterns and fancy symbols that are too small to read, rings layering on top of eachother, but which all idly spins in momentum with Roulx's movements.]''',
    '"Do you like the moon?"',
    '"What do those engravings say?"',
    '"Wow, those must have been expensive."',
    '"Your partner\'s got taste."',
    '"Hugo, right? Congratulations."'],

['''Roulx: "The moon!! Yes, of course." 
[They look to Autumn with excitement!]
Roulx: "I well, have it as an earring because me and Hugo were married on the moon! It's rather romantic,.. But also yes, I do quite like the moon for all its beauty in the night sky." 
[A left hand touches the earring fondly. Gayass.]''',
    '"How did you manage that???"',
    '"That\'s cute. Congratulations!"'],

['''["I didn't know you two were—"]

"That's cute. Congratulations!" [You say with a grin.]
[Ki smiles, lulling kir bag over kir shoulders again.] 
Roulx: "How have you been? It's been a long time since we'd last talked."
"It certainly has."''',
    '"There\'ve been a lot of changes, but recently it\'s been peaceful. I\'m doing alright."',
    '"I couldn\'t have asked for much more."',
    '"Actually... Could we talk somewhere else? I\'m not a big fan of crowded areas."'],

['''Roulx: "Sure of course. It's been sometime since we properly talked. I don't enjoy crowded places either."
[It looks around, glancing at the structures and the low hanging lights overhead.]
Roulx: "you lead the way."
“Alright.”''',
    '[You head to a park.]',
    '[You head to a local cafe.]',
    '[You head to a library in the mall.]'],

['''“..How do you feel about birds, Roulx?”
Roulx: “I like them. But am otherwise neutral to their existence. Why do you ask?” 
[Ki strolls slightly to your right, only a step behind.]
“Nice. I think you wouldn’t mind it there then. Come with me.”

[It’s about a 8 minute walk from where you are until you reach a slightly less populated suburban area, where a stylish cafe stands with a raised wooden deck and circular white tables and parasols on its outside. The name “Haven’s Parrot” is written in a chocolatey brown font on its front in cursive. There are some people at this time of day but it is not entirely packed, and there’s plenty of polished wooden tables and orange cushions to sit at on the inside.]

“I quite like this cafe,” [you says after greeting a waiter, asking for two seats inside.] “It’s usually pretty quiet, but the people I do meet here are incredibly kind. They also renovated recently, that’s why the outside looks so new.”
[Roulx curiously peers its head around the space,] 
Roulx: “it does look cosy.” 
[It does, it does. It heads to take a seat, one that’s orange against the wall.]
[You sit down opposite of Roulx. It's soft. You've always liked sitting at cushioned benches at restaurants.]''',
    '"Do you want to order anything? The drinks here are nice."',
    '"It is. I come here sometimes just for some fresh air, listen to an audiobook or something. Or to meet up with people on occasion."',
    '"Yeah. So, what were we talking about before?"'],

['''Roulx: “I don’t think I’ll have anything. A cup of water, maybe.”
[Its bag remains on its shoulder, the back of its hand visible on the wooden table. Its politeness still unchanged.]''',
    '"Alright. Maybe I\'ll just have that too."',
    '"I\'ll get a latte. Tends to be the usual choice."',
    '[Smile.] "Please make yourself comfortable."'],

['''[You call up the waiter again and ask for some water, as well as your usual selection of cinnamon iced latte. They make good coffee here.]
Roulx: “Alrighty.”
[Ki leans, tapping a hand on the table mindlessly.]
[You take a sip of the latte, served to you atop of a small black plate and along with a ceramic teaspoon.
Mmm. Cold. There's just something inexplicably satisfying about having a cold drink in the middle of winter.]''',
    "Are you sure you don't want anything else?",
    "How is Hugo doing?",
    "Yeah. So, what were we talking about before?"]
]

while not end_game:
    #print interaction
    print("\n" + chat[chat_count][0] + "\n")

    #list options
    num = len(chat[chat_count])
    for i in range(1, num):
        print(str(i) + ". " + chat[chat_count][i])
    print("")
    
    #request input from user
    ans = input(input_msg)
    while not (1 <= int(ans) < num):
        error(num - 1)
        ans = int(input(input_msg))
    
    #print selected response
    print("\n" + str(ans) + ". " + chat[chat_count][int(ans)])
    
    #find next piece of interaction
    chat_count = allocate(chat_count, int(ans))