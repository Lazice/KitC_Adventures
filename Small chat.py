def error (options):
    if (options < 1):
        print(f"... There are only {options}.")
    elif (options == 1):
        print("... There is literally only one option.")
    else:
        print("Get lost.")

print("""greetings
[Roulx stands in front of you, distant, familiar, close. It has been some years after, since it all happened... The people, the scheming, the lights. Isn't it all more than a memory?]")
[They stand there in front of you, seemingly stunned as the tapping of their fingers stands frozen mid-action.]")
1: Oh hi Roulx.
2: Who are you?"
3: [Points.] What are you holding?
4: [Do nothing/walk away.]""")

Chat1 = input("Please input a number --> ") 

if (Chat1 == 1):
        print("Roulx: Olive? How have you been?")
        print("1: Who's Olive?")
        options = 1
elif (Chat1 == 2): 
        
elif (Chat1 == 3): 

elif (Chat1 == 4): 

else:
    error()

