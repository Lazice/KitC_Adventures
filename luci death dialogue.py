import random
import winsound

input_msg = "Please input a number --> "
end_game = False
chat_count = 0
cafe_description = "[It’s about an 8 minute walk from where you are until you reach a slightly less populated suburban area, where a stylish cafe stands with a raised wooden deck and circular white tables and parasols on its outside. The name “Haven’s Parrot” is written in a chocolatey brown font on its front in cursive. There are some people at this time of day but it is not entirely packed, and there’s plenty of polished wooden tables and orange cushions to sit at on the inside.]"

stalk1 = "[Roulx has moved from their previous position, but as you peer around for even the tint of white, you spot them. They've gone strolling down the corridor, gazing pensively over the glass fronts of luxury items.]"
stalk_downstairs = "[The shadows of the layer above you, masked by overhead lights, casting a warm glow over the tiled floorings. Dark metallic steel door frames, make contrast with the glass and signage of the other storefronts around, by their signage made of metal. They're right there. You can't see them. But. *They're there*.]"
feign_innocence = '''"Oh. ...Wait, Roulx? Is that you?"
Roulx: “… Yes? Olive, it’s me.” 
[The two their hands point to themself, leaning forward in a,, almost pleading gesture?]
"Heh... Sorry, I just didn't realise it was you! Well we,, we haven't seen each other in a while, have we?"
"...Wait."'''

down_choice1 = ['[Peer into the shop they\'re at.]', '2(2)2222112']
down_choice2 =['[Go talk to them after all.]', '2(2)2221']
up_choice1 = ['[Creep back downstairs.]', '2(2)2222113']
up_choice2 = ['[Crane your head over the railing to get a better look.]', '2(2)2222112']
wait = ['[Wait around.]', ('2(2)22221121(1)', '2(2)22221121(2)'), (0.5, 0.5)]
watch = ['[Watch Roulx.]', '2(2)22221121(2)1']

def error(options):
    if (options != 1):
        print(f"... There are only {options}.")
    else:
        print("... There is literally only one option.")

def reset_memory():
    return {'Hugo': 0, 'wedding': False, 'chase': False, 'location': 'mall'}

def modify_memory(id, count):
    global chat_count
    if memory['location'] == 'mall2':
        if id == '2(2)222211':
            chat[count][2] = up_choice1
            chat[count][3] = up_choice2
        if id == '2(2)2222111':
            chat[count][1] = up_choice1
            chat[count][2] = up_choice2
        if id == '2(2)2222112':
            chat[count][0] = "[You crane your head over the railings, they feel cold under your hands.]" + chat[count][0]
            chat[count].insert(3, up_choice1)
    
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
    elif id == '2(2)2222113':
        memory['location'] = 'mall'
        


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
        dice_percentage = dice_value/20
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
    print("\nAnswer doesn't exist yet :P. Id number: " + id)
    return 0

chat = [
['''"greetings"
[Roulx stands in front of you, distant, familiar, close. It has been some years after, since it all happened... The people, the scheming, the lights. Isn't it all more than a memory?]
[They stand there in front of you, seemingly stunned as the tapping of their fingers stands frozen mid-action.]''',
    '[Pretend not to notice.]',
    ['[Begin to walk away.]', ('2(1)', '2(2)'), (0.5, 0.5)],
    '"... Roulx?"',
    '0'],

['''[Ki seemed to shiver at that. Barely noticeable, but you've known kime for long enough.]
Roulx: "Olive? You're here!"
[They smile, relieved as they comprehend your presence.]''',
    '[Smile back.]',
    '[Leave. This was a bad idea.]',
    '"..."',
    '3'],

['''[You smile back at them. They are your friend. Smiling is the polite thing to do.]
Roulx: "How have you been?"
[It stands, the two its hands gloved, clasped in front of itself idly.]
"..."''',
    '"...Roulx. I\'m not Olive."',
    '31'],

['''[Their smile lowers, but doesn't disappear as they tilt their head.]
Roulx: "What do you mean? ... You look just like him?"
"Autumn. My name is Autumn. You must have confused me for someone else."
Roulx: "Autumn? You're Autumn?.. Do you,, well you don't but... Do you know of someone by the name Olive Stanford?"''',
    '"No. I do not."',
    '311'],

['''Roulx: "...Alright..."
[It shifts in its stance. Looking down to the side... It wears the same white suit and outfit from the very before, yellow bow tie sitting in the exact same.] 
Roulx: "Well, nice to meet you Autumn, though you already know my name." 
[Roulx reaches out a gloved right hand, to shake in polite greeting.]
[You shake hands. It is a familiar feeling, a warm feeling. Having an ally on your side.]
"Nice to meet you too, Roulx."''',
    '"How are you?"',
    '"Why are you here?"',
    '"Could we talk somewhere else? I\'m not a big fan of crowded areas."',
    '3111'],

['''[They look around, the store seems spacious, Roulx themself have new earrings and a shoulder tote bag of books and trinkets.] 
Roulx: "I'm only here to buy things for my Hugo. We're stopping near by for sightseeing and business." 
[They shrug. A swing and there some badges and trinkets clink against each other on the surface of their bag.]''',
    '"I like your earrings."',
    '"Those badges look lovely. They suit you."',
    '"Hugo? Are they your partner?"',
    '"Looks like you\'ve bought quite a bit. Are you looking for anything else?"',
    '31112'],

['''Roulx: "Thanks! These are new, my partner gave me them for our anniversary last year."
 [Gold in material, the left one is a delicate replication of a moon. Simple, small and sways side to side as it tilts in its expressiveness. The right one, much more complicated, rings engraved with patterns and fancy symbols that are too small to read, rings layering on top of eachother, but which all idly spins in momentum with Roulx's movements.]''',
    '"Do you like the moon?"',
    '"What do those engravings say?"',
    '"Wow, those must have been expensive."',
    '"Your partner\'s got taste."',
    '"Hugo, right? Congratulations."',
    '311121'],

['''Roulx: "The moon!! Yes, of course." 
[They look to Autumn with excitement!]
Roulx: "I well, have it as an earring because me and Hugo were married on the moon! It's rather romantic,.. But also yes, I do quite like the moon for all its beauty in the night sky." 
[A left hand touches the earring fondly. Gayass.]''',
    '"How did you manage that???"',
    '"That\'s cute. Congratulations!"',
    '3111211'],

['''["I didn't know you two were—"]

"That's cute. Congratulations!" [You say with a grin.]
[Ki smiles, lulling kir bag over kir shoulders again.] 
Roulx: "How have you been? It's been a long time since we'd last talked."
"It certainly has."''',
    '"There\'ve been a lot of changes, but recently it\'s been peaceful. I\'m doing alright."',
    '"I couldn\'t have asked for much more."',
    ['"Actually... Could we talk somewhere else? I\'m not a big fan of crowded areas."', '31113'],
    '31112112'],

['''Roulx: "Sure of course. It's been sometime since we properly talked. I don't enjoy crowded places either."
[It looks around, glancing at the structures and the low hanging lights overhead.]
Roulx: "you lead the way."
“Alright.”''',
    '[You head to a park.]',
    '[You head to a local cafe.]',
    '[You head to a library in the mall.]',
    '31113'],

[f'''“..How do you feel about birds, Roulx?”
Roulx: “I like them. But am otherwise neutral to their existence. Why do you ask?” 
[Ki strolls slightly to your right, only a step behind.]
“Nice. I think you wouldn’t mind it there then. Come with me.”

{cafe_description}

“I quite like this cafe,” [you say after greeting a waiter, asking for two seats inside.] “It’s usually pretty quiet, but the people I do meet here are incredibly kind. They also renovated recently, that’s why the outside looks so new.”
[Roulx curiously peers its head around the space,] 
Roulx: “it does look cosy.” 
[It does, it does. It heads to take a seat, one that’s orange against the wall.]
[You sit down opposite of Roulx. It's soft. You've always liked sitting at cushioned benches at restaurants.]''',
    '"Do you want to order anything? The drinks here are nice."',
    '"It is. I come here sometimes just for some fresh air, listen to an audiobook or something. Or to meet up with people on occasion."',
    '"Yeah. So, what were we talking about before?"',
    '311132'],

['''Roulx: “I don’t think I’ll have anything. A cup of water, maybe.”
[Its bag remains on its shoulder, the back of its hand visible on the wooden table. Its politeness still unchanged.]''',
    '"Alright. Maybe I\'ll just have that too."',
    '"I\'ll get a latte. Tends to be the usual choice."',
    '[Smile.] "Please make yourself comfortable."',
    '3111321'],

['''[You call up the waiter again and ask for some water, as well as your usual selection of cinnamon iced latte. They make good coffee here.]
Roulx: “Alrighty.”
[Ki leans, tapping a hand on the table mindlessly.]
[You take a sip of the latte, served to you atop a small black plate and along with a ceramic teaspoon.
Mmm. Cold. There's just something inexplicably satisfying about having a cold drink in the middle of winter.]''',
    "Are you sure you don't want anything else?",
    "How is Hugo doing?",
    "Yeah. So, what were we talking about before?",
    '31113212'],

['''Roulx: "He's been doing fine. It wouldn't've been a long time since he'd left. But I'll say that he's doing fine.",
[It takes its tastes of the water. Lukewarm.] 
Roulx: "What did you think of him?"''',
    "He certainly lightens the room with his presence. Charismatic, might be the word. They're a good fit for you, I think. Is he good to you?",
    "Honestly I don't think I know them as well as I could have, but they seemed like a good person. Friendly, easy to talk to. What do *you* think of him?",
    "He's a time traveller, right? We talked a few times, he told me about some of his journeys. There must be so much going on out there, I can't possibly imagine. Do you two travel often?",
    '311132122'],

['''Roulx: "Olive Stanford."
[They attempt to walk up to your side.]''',
    '[Freeze.]',
    '[Turn to them.]',
    ['[Keep walking. Deep breaths.]', ('2(1)3', '2(2)'), (1/3, 2/3)], 
    '2(1)'],

['''Roulx: "Hey!" 
[They call out for you again, catching up with a trot. Your sight greets the corners of a patch of white.]''',
    '[Give up.]',
    ['[Keep walking.]', ('2(1)32', '2(2)'), (2/3, 1/3)],
    ['[Break into a run. (Roll for running.)]', ('2(1)33(3)', '2(1)33(2)', '2(1)33(1)'), (1/4, 1/4, 1/2)],
    '2(1)3'],

['''[The person doesn't hesitate anymore, hopping in front of you directly blocking your path.] 
Roulx: "Hey."
[...]''',
    ['[Feign innocence.]', '2(1)31'],
    ['[Freeze.]', '2(1)1'],
    ['[Break into a run. (Roll for running.)]', ('2(1)33(3)', '2(1)33(2)', '2(1)33(1)'), (1/4, 1/4, 1/2)],
    '2(1)32'],

['''[They no longer follow. But you can still feel their gaze on you for a little longer, before the gaze fades.]''',
    '[Risk a glance back.]',
    '[Keep walking. You\'re almost out.]', 
    '2(2)'],

['''[You are out of the mall. Cars pass by on the road in front of you.
You should be safe now.]''',
    ['[Keep walking.]', '01'],
    '[..."Roulx was in there."]', 
    '2(2)2'],

['''Ending 1.  Strangers in the End.
Roulx thinks that they'd simply mistaken them for kir dear friend. A pity.''',
    ['Restart.', '0'],
    ['Revert to previous move.', '2(2)2'],
    '01'],

['''[Yes, this is true. Roulx, a former ally that you knew, is still in the mall. You have no idea what they are doing in there, nor how long they plan to stay.
...]''',
    ['[Walk away. Try to forget.]', '01'],
    '[Return to the mall.]',
    '2(2)22'],

['''[Great. Now what are you going to do?]''',
    '[Walk up to them. Greet them like any normal person.]',
    '[Observe their movements.]',
    '2(2)222'],

['''[They run after you. Though your crowded surroundings make obstacles for you.]
[After a while of running, you seem to have lost them. The streets run bare. The strange person is nowhere in your sense.]''',
    ['[Risk a glance back.]', ('2(1)33(1)1(1)', '2(1)33(1)1(2)'), (0.5, 0.5)],
    ['[Catch your breath.]', ('2(1)33(1)1(1)', '2(1)33(1)1(2)'), (0.5, 0.5)],
    '[Keep running. Don\'t look back.]',
    '2(1)33(1)'],

['''[Guess what mfer. Out of the lone sounds of the city noise, you hear in haste. Running.]''',
    '[Run.]',
    '[Just give up already. You can\'t hide.]',
    '2(1)33(1)1(1)'],

['''[Are you sure you're gonna keep on running? Buddy. Do you even know who you're running up against?... Well, you take off again. But they sound like they're catching up. Are you seriously gonna?]''',
    '[Give. Up.]',
    '[Keep. Running.]',
    '2(1)33(1)1(1)1'],

['''[... It's behind you. It's behind you. It's behind you. It's.]''',
    '[Run.]',
    '[Freeze.]',
    '2(1)33(1)1(1)12'],

['''Roulx: "hmph-" 
[Something, *someone* fell. The footsteps have stopped.]''',
    ['[Run.]', '02'],
    '[Turn.]',
    '2(1)33(1)1(1)121'],

['''Roulx: "..." 
[You keep on running. There's nothing making indication of them still chasing you.]''',
    '[Run.]',
    '02'],

['', '[Run.]', '021'],

['', '[Run.]', '0211'],

['', '[Run.]', '02111'],

['''[Pant, pant, pant.   '...  You can't... You can't keep doing this to yourself, Olive. ...']''',
    ['["Who\'s Olive?"]', "#"],
    '021111'],

['''[You seemed to have lost them... You find yourself upon the sidewalks of a street you don't recognise. Red brick walls censored with graffiti, cig buds lay trash to the exposed roots of trees.]
[Well damn how are you gonna get back now?...]''',
    '[Find current location on phone.]',
    '[Try to retrace steps back to the mall.]',
    '2(1)33(1)1(2)'],

['''[You open your map in search of your current location. You have, in miracle, ran as fast as you can all the way to further west of your suburb. Despite at least going out from time to time, you hadn't ever came around this far in this direction. Perhaps it's because of the lack of street lights around here, or the simply fewer people that'd even talked about.]
[... Luckily it's only a few minutes walk to get back to where you are more familiar. As you know where you are going.]''',

    '2(1)33(1)1(2)1'],

['''[Upon your vision, your dear friend falls collapsed on the cement. Not from being tripped, no, they're better than that.]''',
    '[Wait for a sign of movement.]',
    ['[Run away.]', '02'],
    "...I'm. Sorry. ...",
    '2(1)33(1)1(1)1212'],

['''[There are twitches in their shoulder. White hair splayed on the ground, they do eventually make to slowly sit up.]
[They simply...]
[Look at you.]
[You can't tell their expression. Is it confusion? Is it coldness? Is it frustration?]''',
    '[Hold your silence.]',
    '[Offer a hand.]',
    '"...I\'m. So sorry. ..."',
    '2(1)33(1)1(1)12121'],

['''[Their response is slow. Their own hand, though gloved, reaches up to take yours.]''',
    '"Are you hurt?"',
    '"Sorry I ran away. I didn\'t recognise you."',
    '"..."',
    '2(1)33(1)1(1)121212'],

['''[You help them up.]
Roulx: "I'm alright." 
[They take a stance in front of you. Slower breaths.] 
Roulx: "Are you,, are you alright?"''',
    '"Yes. I\'m alright."',
    '2(1)33(1)1(1)1212121'],

['''[They breathe. Inhale, exhale. But then take themself to gain poise.]
Roulx: "How have you been, Olive?"''',
    '"...Who\'s Olive?"',
    '2(1)33(1)1(1)12121211'],

['''[You help them up.]
Roulx: "That,, that's alright." 
[They look away to the side.] 
"What... How have you been, Olive?"''',
    '"...Who\'s Olive?"',
    '2(1)33(1)1(1)1212122'],

['''[The doors of the mall closes behind you,, seconds later than you would imagine. Hmm. That’s odd.]''',
    ['[Run.]', '2(1)33(1)'],
    '[Turn around.]',
    '"...Hello, Roulx."',
    '2(1)33(2)'],

['''[...You feel someone tapping on your shoulder in your half stumbling stroll. Who might that be?]''',
    ['[Freeze.]', '2(1)1'],
    '"...Hello, Roulx."',
    '2(1)33(3)'],

['''[Roulx is only a block away from its original spot. Now having lost its original target, it is staring over metal railings to the floor below...]''',
    '[Sneak around on the same floor.]',
    '[Go up the escalator to observe them from above.]',
    '2(2)2222'],

[f'''{stalk_downstairs}
{stalk1}''',
    '["I wonder what they are buying."]',
    '["I wonder why they\'re spending so luxuriously."]',
    '2(2)22221'],

['''[How curious.. What do they have... Clothes, jewels, tools... As you inspect the items abound, you don't forget who *you* are looking out for. Roulx has found their way into a tools repair workshop.]''',
    '[Idly wonder what they are buying.]', down_choice1, down_choice2,
    '2(2)222211'],

['''[You ponder what they might be buying, staying in spot. Roulx is inside the tools repair workshop.]
[Roulx... Usually utilises tools that are more ordinary for their work. It's rather peculiar to see them ponder items that,, by what you know, seldom in their standard.]''',
    down_choice1, down_choice2,
    '2(2)2222111'],

[f'''[Their bright figure is distinctive in the scarcely visited workshop. Peering, they take only short glances of the complicated parts and charts and diagrams on the walls. But an item they take out of their decorated tote bag catches your attention. A gloved hand, holding up a small, grey, staff-like item, conducting quiet chatter with the facilitator from the desk - which you cannot tell what they're talking about from your position, as their back is turned towards you.]''',
    wait,
    '[Listen in on their conversation.]',
    '2(2)2222112'],

["",
    '["...I\'m curious."]',
    ['["This is literally none of my business."]', '2(2)222211221'],
    '2(2)22221122'],

["😒",
    wait,
    ['[JUST GO TALK TO THEM GODDAMMIT]', '2(2)2221'],
    '2(2)222211221'],

['''[You wait around on the spot.]
[Roulx comes out of the store, noticing you creeping around the storefront... They look towards you, saying nothing but just a strange look.]''',
    '[Pretend you hadn’t noticed. Walk off again.]',
    '[Frown at them, like it\’s weird that they\’re staring. They\’re strangers after all.]',
    ['[Give in.]', '2(2)2221'],
    '2(2)22221121(1)'],

['''[Roulx comes out of the store. Luckily, they turn the other way, strolling past your sneaky behaviour.]''',
    watch,
    '2(2)22221121(2)'],

['''[You spin around before you they get the chance to make eye contact with you. Tucking your hands in pockets and sucking in a quick breath, you walk off. The way that you turn, almost reminds one of a video game NPC.]
[But they don't move. Completely silent the moment that they've spotted you. That when you turn away, you can tell from the net zero audio cue, that they have hadn't any steps taken away at all.]''',
    '',
    '2(2)22221121(1)1'],

['''[You frown at Roulx. They seem put off by that expression, tilting their head at you.]
Roulx: "Hmm? My apologies." 
[They turn, moving out of your way to the other side of the walkway. Presumably giving *you* space, as any polite stranger would.]''',
    '[Buy something. Anything.]',
    watch,
    '2(2)22221121(1)2'],

['''[You began to look for something to buy. Perhaps to make yourself look less suspicious.]
[However. The area that you are in doesn’t serve the cheapest… Well, to the least there is a food court near the same entrance that you came from, but that’s a few walls of distance as well.]''',
    '[Just browse, then.]',
    watch,
    '2(2)22221121(1)21'],

['''"..."''',
    watch,
    '2(2)22221121(1)211'],

['''[... You come to the sense, to watch. Roulx.]
[You turn around to them away. How they move as quiet as you remembered with coldness. But they haven’t left your sight. Or to say, you haven’t allowed them to leave your sight.]''',
    '[Follow them. You can’t afford to lose them.]',
    '2(2)22221121(2)1'],

[f'''[You creep back downstairs.]
{stalk_downstairs}''',
    down_choice1, down_choice2,
    '2(2)2222113'],

[f'''{feign_innocence}''',
    '"Who\'s Olive?"',
    '2(1)31'],

[f'''[You approach them with a look of surprise.]
{feign_innocence}''',
    ['"Who\'s Olive?"', '2(1)311'],
    '2(2)2221'],

['''Roulx: “Hmm? You’re Olive. Right?”
[They tilt their head, a gesture of confusion. A right hand which taps less patient than their tone may tell.]
"...Huh?" I\'m not Olive. I\'m Autumn. Autumn Sky. You must have confused me for someone else."
[Their expression drops, even if there weren’t much except for the way they stared at you.] 
Roulx: “O-Oh.” 
[They fidget, eyes darting away to the ground beside and their hand fiddling with tote bag straps on their shoulder.]
Roulx: “Ah… My apologies. I.. Must’ve mistaken you for a friend of mine.” 
[Friend.]''',
    ['"That\'s alright. Mistakes happen all the time."', '3111'],
    '2(1)311'],

['''[You go very, very still. As though that will help you now, Heh.]
[How silly of you!. Well they simply stare down at you, huffing, but slowing breaths noticeable as they stand right in front of you.] 
Roulx: “…” 
[It stares.]''',
    '[Stare back.]',
    ['"...Roulx?"', '2(1)31'],
    '"...Hello, Roulx."',
    '2(1)1'],

['''[Oh a staring contest?…]
[…]
[…]
[…]
[Their face scrunches up uncomfortably.]''',
    '[You\'re on.]',
    ['"...Roulx?"', '2(1)31'],
    '2(1)11']

]

memory = reset_memory()
while not end_game:
    #print interaction
    print("\n" + chat[chat_count][0] + "\n")

    #list options
    num = len(chat[chat_count]) - 1
    for i in range(1, num):
        if len(chat[chat_count][i]) == 3  or len(chat[chat_count][i]) == 2:
            print(str(i) + ". " + chat[chat_count][i][0])
        else:
            print(str(i) + ". " + chat[chat_count][i])
    
    #request input from user
    ans = input("\n" + input_msg)
    while not (1 <= int(ans) < num):
        error(num - 1)
        ans = int(input(input_msg))
    
    #print selected response
    if len(chat[chat_count][int(ans)]) == 3:
        print(str(ans) + ". " + chat[chat_count][int(ans)][0])
        id = roll(chat[chat_count][int(ans)])
    elif len(chat[chat_count][int(ans)]) == 2:
        id = chat[chat_count][int(ans)][1]
    else:
        print(str(ans) + ". " + chat[chat_count][int(ans)])
        id = allocate(chat[chat_count][-1], int(ans))
    
    print(id)
    chat_count = search_for_id(id)
    modify_memory(id, chat_count)