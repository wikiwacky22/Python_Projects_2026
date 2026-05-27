#Dog Breed(CREATE TASK)
#Perrin
#Create project for helping users chose a dog breed that meets their needs.
#Initiate
#Starts by importing tables
import random
import pandas as pd
import webbrowser
y=0
data=pd.read_csv('dogs.csv')
name= data['Name'].tolist()
breedgroup= data['Breed Group'].tolist()
minweight = data['Minimum Weight'].tolist()
id= data['id'].tolist()
temperament= data['Temperament'].tolist()
image= data['Image'].tolist()
bred_for= data['BredFor'].tolist()
filterdog = []
idbreedfilter = []
#Functions
def getdogsize(size):
    if size == "tiny":
        for i in range(len(name)):
            if minweight[i] <= 10:
                filterdog.append(name[i])
    elif size == "small":
        for i in range(len(name)):
            if minweight[i] <= 25 and minweight[i] >= 11:
                filterdog.append(name[i])
    elif size == "medium":
        for i in range(len(name)):
            if minweight[i] <= 60 and minweight[i] >= 26:
                filterdog.append(name[i])
    elif size == "large":
        for i in range(len(name)):
            if minweight[i] > 60:
                filterdog.append(name[i])
    print("here are the dogs that meet your recomended weight class:")
    print(*filterdog)
    print("I reccomend this dog")
    print(filterdog[random.randint(0,len(filterdog)-1)])
    filterdog.clear()
def dogsearch(breed_name):
    global y
    y=0
    while True:
            for i in range(len(name)):
                if breed_name == str(name[i]):
                    print(temperament[i])
                    webbrowser.open(image[i])
                    y=y+1
            if y == 0:
                breed_name= input("that dog does not exist input a new one:")
            else:
                break
def advanced_dogsearch(purpose):
    global x
    x=0
    while True:
        for i in range(len(name)):
            if purpose in bred_for[i]:
                print(*name[i])
                x=x+1
        if x==0:
            purpose= input("that purpose does not exist try again:")
        else:
            break
def Main():
    global size
    global breed_name
    print("this aplication will help find the right dog for you")
    while True:
        choice= input("Do you want to find a dog that will fit your size:")
        if choice == "yes":
            size = input("what size dog do you want (tiny,small,medium,large):")
            getdogsize(size)
        elif choice == "no":
            choice2 = input("do you want to find a dog that matches your breed:")
            if choice2 == "yes":
                breed_name = input("what type of dog breed do you want type the name:")
                dogsearch(breed_name)
            elif choice2 == "no":
                choice3= input("do you want to find a dog based on your desired trait:")
                if choice3 == "yes":
                    purpose = input("input a trait that you desire in a dog:")
                    advanced_dogsearch(purpose)
                elif choice3 == "no":
                    choice4 = input("do you want to stop researching yes or no:")
                    if choice4 == "yes":
                        break
                    elif choice4 == "no":
                        continue
        choice5 = input("do you want to continue using the program:")
        if choice5 == "no":
            break
        elif choice5 == "yes":
            continue

#Main
Main()

#Sources
#Dog DataSet
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
