#Perrin
#Marvel nickname generator
def Marvelpicker():
    print("What marvel character are you?")
    choice1=input("Are you enhanced or do you have a ego:")
    if choice1 == "ego":
        choice2= input("Are you more magical or metal:")
        if choice2 == "magical":
            choice3 = input("Do you identify more with the color red or gold:")
            if choice3 == "red":
                print("your marvel character is Skarlet Witch")
            elif choice3 == "gold":
                print("your marvel character is Dr. Strange")
        elif choice2 == "metal":
            choice4 = input("pick between joining the military or the american industrial complex:")
            if choice4 == "military":
                print("your marvel character is war machine:")
            elif choice4 == "american industrial complex":
                print("your marvel character is ironman")
    elif choice1 == "enhanced":
        choice5= input("are you young or old:")
        if choice5 == "young":
            choice6 = input("are you tiny or massive:")
            if choice6 == "tiny":
                print("your marvel character is spiderman")
            elif choice6 == "massive":
                print("your marvel character is the Hulk")
        elif choice5 == "old":
            choice7 = input("do you like a arm or a shield  better:")
            if choice7 == "arm":
                print("your marvel character is the winter soldier")
            elif choice7 == "shield":
                print("your marvel character is captian america")
Marvelpicker()

