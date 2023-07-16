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
    else:
        print("Answer doesn't exist yet :P.")
        return 0

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
Roulx: Olive? How have you been?
[They smile, relieved as they comprehend your presence.]''',
    '[Smile back.]',
    '[Leave. This was a bad idea.]',
    '"..."'],

    ['''[You smile back at them. They are your friend. Smiling is the polite thing to do.]
"..."''',
    '"...Roulx. I\'m not Olive."']
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