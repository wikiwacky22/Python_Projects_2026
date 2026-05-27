#Perrin and Caleb
#We are making a slot machine
#Initiation
import random
#Function
def slotmachine(credits2,choice,creditsp,simulation,timesrun):
    try:
        file = open('scoreboard.txt','x')
        y = 0
        try:
            x = 1
            names=[]
            scores= []
            with open('scoreboard.txt','r') as file:
                    for line in file:
                        name, score = line.strip().split(":")
                        scores.append(score)
                        names.append(name)
            pairedSC=zip(scores,names)
            sortedSC=sorted(pairedSC)
            sortedscore,sortedname= zip(*sortedSC)
            print("TOP 5 MONEY MAKERS")
            for i in range(5):
                print(f"{sortedname[len(names)-x]}:{sortedscore[len(names)-x]}")
                x=x+1
            global credits
            credits=creditsp
            if choice != "no":
                username= input("what is your name:")
                with open('scoreboard.txt','r') as file:
                    for line_number, line in enumerate(file):
                        name, score = line.strip().split(":")
                        if name == username:
                            y=1
                            credits = int(score)
            global gplayed
            gplayed=0
            while True:
                while True:
                    if credits2 != "no":
                        credits2=input("How many credits do you want to load into your account, 500, 100, or 50? (if none write no):")
                    try:
                        if int(credits2)==500:
                            credits=credits+500
                        elif int(credits2)== 100:
                            credits=credits+100
                        elif int(credits2)==50:
                            credits=credits+50
                    except:
                        if credits2 == "no":
                            break
                        else:
                            print("please enter valid response")
                if credits>= 10:
                    credits=credits-10
                    picker= [7,"♠","♡","♢","♠","♡","♢"]
                    a = random.randint(0,3)
                    b= random.randint(0,3)
                    c= random.randint(0,3)
                    print(f"{picker[a]}-{picker[b]}-{picker[c]}")
                    if a!=7 and a==b and b==c:
                        print("you got a match")
                        credits= credits+150
                        gplayed=gplayed+1
                    elif a==7 and a==b and b==c:
                        print("you got a jackpot")
                        print("you got 100 credits")
                        credits=credits+3000
                        gplayed=gplayed+1
                    else:
                        print("you lost")
                        gplayed=gplayed+1
                else:
                    print("you have an insufficient amount of funds")
                if simulation== "yes":
                    if gplayed == timesrun:
                        break
                if choice != "no":
                    choice = input("do you want to cash out(yes or no)")
                if choice == "no":
                    choice = "yes"
                    continue
                else:
                    if y == 1:
                        with open('scoreboard.txt','r') as file:
                            lines = file.readlines()
                        for i, line in enumerate(lines):
                            name, score = line.strip().split(":")
                            if name == username:
                                lines[i]= f"{username}:{credits}\n"
                                break
                        with open('scoreboard.txt','w') as file:
                            file.writelines(lines)
                            break
                    else:
                        try:
                            file = open('scoreboard.txt','x')
                            file.write(f"{username}:{credits}\n")
                            file.close()
                            break
                        except:
                            with open('scoreboard.txt','a') as file:
                                file.write(f"{username}:{str(credits)}\n")
                                file.close()
                            with open('scoreboard.txt','r') as f:
                                scoreboard = f.read()
                                print(scoreboard)
                            break
        except:

            credits=creditsp
            if choice != "no":
                username= input("what is your name:")
                with open('scoreboard.txt','r') as file:
                    for line_number, line in enumerate(file):
                        name, score = line.strip().split(":")
                        if name == username:
                            y=1
                            credits = int(score)
            gplayed=0
            while True:
                while True:
                    if credits2 != "no":
                        credits2=input("How many credits do you want to load into your account, 500, 100, or 50? (if none write no):")
                    try:
                        if int(credits2)==500:
                            credits=credits+500
                        elif int(credits2)== 100:
                            credits=credits+100
                        elif int(credits2)==50:
                            credits=credits+50
                    except:
                        if credits2 == "no":
                            break
                        else:
                            print("please enter valid response")
                if credits>= 10:
                    credits=credits-10
                    picker= [7,"♠","♡","♢","♠","♡","♢"]
                    a = random.randint(0,3)
                    b= random.randint(0,3)
                    c= random.randint(0,3)
                    print(f"{picker[a]}-{picker[b]}-{picker[c]}")
                    if a!=7 and a==b and b==c:
                        print("you got a match")
                        credits= credits+150
                        gplayed=gplayed+1
                    elif a==7 and a==b and b==c:
                        print("you got a jackpot")
                        print("you got 100 credits")
                        credits=credits+3000
                        gplayed=gplayed+1
                    else:
                        print("you lost")
                        gplayed=gplayed+1
                else:
                    print("you have an insufficient amount of funds")
                if simulation== "yes":
                    if gplayed == timesrun:
                        break
                if choice != "no":
                    choice = input("do you want to cash out(yes or no)")
                if choice == "no":
                    choice = "yes"
                    continue
                else:
                    if y == 1:
                        with open('scoreboard.txt','r') as file:
                            lines = file.readlines()
                        for i, line in enumerate(lines):
                            name, score = line.strip().split(":")
                            if name == username:
                                lines[i]= f"{username}:{credits}\n"
                                break
                        with open('scoreboard.txt','w') as file:
                            file.writelines(lines)
                            break
                    else:
                        try:
                            file = open('scoreboard.txt','x')
                            file.write(f"{username}:{credits}\n")
                            file.close()
                            break
                        except:
                            with open('scoreboard.txt','a') as file:
                                file.write(f"{username}:{str(credits)}\n")
                                file.close()
                            with open('scoreboard.txt','r') as f:
                                scoreboard = f.read()
                                print(scoreboard)
                            break
    except:
        y = 0
        x = 1
        names=[]
        scores= []
        try:
            with open('scoreboard.txt','r') as file:
                    for line in file:
                        name, score = line.strip().split(":")
                        scores.append(int(score))
                        names.append(name)
            pairedSC=zip(scores,names)
            sortedSC=sorted(pairedSC)
            sortedscore,sortedname= zip(*sortedSC)
            print("TOP 5 MONEY MAKERS")
            for i in range(5):
                print(f"{sortedname[len(names)-x]}:{sortedscore[len(names)-x]}")
                x=x+1
            credits=creditsp
            if choice != "no":
                username= input("what is your name:")
                with open('scoreboard.txt','r') as file:
                    for line_number, line in enumerate(file):
                        name, score = line.strip().split(":")
                        if name == username:
                            y=1
                            credits = int(score)
            gplayed=0
            while True:
                while True:
                    if credits2 != "no":
                        credits2=input("How many credits do you want to load into your account, 500, 100, or 50? (if none write no):")
                    try:
                        if int(credits2)==500:
                            credits=credits+500
                        elif int(credits2)== 100:
                            credits=credits+100
                        elif int(credits2)==50:
                            credits=credits+50
                    except:
                        if credits2 == "no":
                            break
                        else:
                            print("please enter valid response")
                if credits>= 10:
                    credits=credits-10
                    picker= [7,"♠","♡","♢","♠","♡","♢"]
                    a = random.randint(0,3)
                    b= random.randint(0,3)
                    c= random.randint(0,3)
                    print(f"{picker[a]}-{picker[b]}-{picker[c]}")
                    if a!=7 and a==b and b==c:
                        print("you got a match")
                        credits= credits+150
                        gplayed=gplayed+1
                    elif a==7 and a==b and b==c:
                        print("you got a jackpot")
                        print("you got 100 credits")
                        credits=credits+3000
                        gplayed=gplayed+1
                    else:
                        print("you lost")
                        gplayed=gplayed+1
                else:
                    print("you have an insufficient amount of funds")
                if simulation== "yes":
                    if gplayed == timesrun:
                        break
                if choice != "no":
                    choice = input("do you want to cash out(yes or no)")
                if choice == "no":
                    choice = "yes"
                    continue
                else:
                    if y == 1:
                        with open('scoreboard.txt','r') as file:
                            lines = file.readlines()
                        for i, line in enumerate(lines):
                            name, score = line.strip().split(":")
                            if name == username:
                                lines[i]= f"{username}:{credits}\n"
                                break
                        with open('scoreboard.txt','w') as file:
                            file.writelines(lines)
                            break
                    else:
                        try:
                            file = open('scoreboard.txt','x')
                            file.write(f"{username}:{credits}\n")
                            file.close()
                            break
                        except:
                            with open('scoreboard.txt','a') as file:
                                file.write(f"{username}:{str(credits)}\n")
                                file.close()
                            with open('scoreboard.txt','r') as f:
                                scoreboard = f.read()
                                print(scoreboard)
                            break
        except:
            credits=creditsp
            if choice != "no":
                username= input("what is your name:")
                with open('scoreboard.txt','r') as file:
                    for line_number, line in enumerate(file):
                        name, score = line.strip().split(":")
                        if name == username:
                            y=1
                            credits = int(score)
            gplayed=0
            while True:
                while True:
                    if credits2 != "no":
                        credits2=input("How many credits do you want to load into your account, 500, 100, or 50? (if none write no):")
                    try:
                        if int(credits2)==500:
                            credits=credits+500
                        elif int(credits2)== 100:
                            credits=credits+100
                        elif int(credits2)==50:
                            credits=credits+50
                    except:
                        if credits2 == "no":
                            break
                        else:
                            print("please enter valid response")
                if credits>= 10:
                    credits=credits-10
                    picker= [7,"♠","♡","♢","♠","♡","♢"]
                    a = random.randint(0,3)
                    b= random.randint(0,3)
                    c= random.randint(0,3)
                    print(f"{picker[a]}-{picker[b]}-{picker[c]}")
                    if a!=7 and a==b and b==c:
                        print("you got a match")
                        credits= credits+150
                        gplayed=gplayed+1
                    elif a==7 and a==b and b==c:
                        print("you got a jackpot")
                        print("you got 100 credits")
                        credits=credits+3000
                        gplayed=gplayed+1
                    else:
                        print("you lost")
                        gplayed=gplayed+1
                else:
                    print("you have an insufficient amount of funds")
                    continue
                if simulation== "yes":
                    if gplayed == timesrun:
                        break
                if choice != "no":
                    choice = input("do you want to cash out(yes or no)")
                if choice == "no":
                    choice = "yes"
                    continue

                else:
                    if y == 1:
                        with open('scoreboard.txt','r') as file:
                            lines = file.readlines()
                        for i, line in enumerate(lines):
                            name, score = line.strip().split(":")
                            if name == username:
                                lines[i]= f"{username}:{credits}\n"
                                break
                        with open('scoreboard.txt','w') as file:
                            file.writelines(lines)
                            break
                    else:
                        try:
                            file = open('scoreboard.txt','x')
                            file.write(f"{username}:{credits}\n")
                            file.close()
                            break
                        except:
                            with open('scoreboard.txt','a') as file:
                                file.write(f"{username}:{str(credits)}\n")
                                file.close()
                            with open('scoreboard.txt','r') as f:
                                scoreboard = f.read()
                                print(scoreboard)
                            break
def simulation():
    global credits
    slotmachine("no","no",10000000000000,"yes",1000)
    credits=10000000000000-credits
    print(f"house total profit{credits}")
    print(f"profit per spin{credits/1000}")
#Main
slotmachine("yes","yes",0,"no",0)

