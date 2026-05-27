#CREATE project 2026
#Game recommender: recommends board games based on input
#initiation
import random
import pandas as pd
import re
#lists/arrays
data =pd.read_csv('games.csv')
id = data['id'].tolist()#takes a list of game IDs from a dataset of Board Games
name = data['Name'].tolist()#takes a list of names from a dataset of Board Games
Minimum_players = data['Minimum players'].tolist()#takes a list of the minimum amount of players for a certain game from a dataset of Board Games
Maximum_Players = data['Maximum players'].tolist()#takes a list of the maximum amount of players for a certain game from a dataset of Board Games
Average_game_time =  data['Average game time'].tolist()#takes a list of Average game time from a dataset of Board Games
Year_released = data['Year released'].tolist()#takes a list of the year that a game was released from a dataset of Board Games
Mechanics = data['Mechanics'].tolist()#takes a list of mechanics from a dataset of Board Games
Category = data['Category'].tolist()#takes a list of game catagories from a dataset of Board Games
Designer = data['Designer'].tolist()#takes a list of game designers from a dataset of Board Games
url = data['More info URL'].tolist()#takes a list of game urls from a dataset of Board Games
id_filter2=[]#Filters work to sort game they are cleared after use and then refilled in the next function
id_filter1=[]#They contain the game ids for the game and are neccesary for the filtering system and are regularly appended.
#functions

def time_checker(time): #checks to see which board games the user can play in the time they have
        for i in range(len(Average_game_time)):
            try:
                f=int(time)
                if Average_game_time[i]<=int(time):
                    id_filter1.append(id[i])
            except:
                time=input("please enter a valid number: ")
def mechanics(workchoice):#searches through the games based on the mechanics and the paramater
    while True:
        if re.search(r'\d+',workchoice):
            workchoice=input("please enter a valid mechanic that is a word: ")
        else:
             break
    for i in range (len(id_filter1)):
                if workchoice.strip().lower() in Mechanics[id_filter1[i]-1].strip().lower():
                    id_filter2.append(id_filter1[i])
    id_filter1.clear()
def players(number):#searches through the games based on the amount of players and the paramater
    for i in range (len(id_filter2)):
        try:
            f=int(number)
            if int(number)>=Minimum_players[id_filter2[i]-1] and int(number)<=Maximum_Players[id_filter2[i]-1]:
                id_filter1.append(id_filter2[i])
        except:
            number=input("please enter a valid number: ")
    id_filter2.clear()
def categories(categories):#searches through the games based off of the different categpories and the paramater
    while True:
        if re.search(r'\d+',categories):
            categories=input("please enter a valid category that is a word: ")
        else:
             break
    for i in range (len(id_filter1)):
        try:
            if re.search(r'\d+',workchoice):
                    workchoice=input("please enter a valid mechanic that is a word: ")
        except:
            if categories.strip(" ").lower() in Category[id_filter1[i]-1].strip(" ").lower():
                id_filter2.append(id_filter1[i])
    id_filter1.clear()
def main():
    while True:#The entire loop for the program
        z=input("""Welcome to board Game finder!
                This application will find you a board game based on your wants and needs!
                1-Find A Game!
                2-Quit Application
                What would you like to do?: """)
        if z=="1":
            time_checker(input("How many minutes do you have to play?: "))
            mechanics(input("What is a mechanic you would like your game to have? (EX. 'Trading' or 'Dice Rolling'): "))
            players(input("How many people do you have to play?: "))
            categories(input("What category game would you like to play? (EX. 'Animals' or 'Fantasy'): "))
            if len(id_filter2)== 0:
                print("Sorry, no games fit your needs.")
            else:
                x=random.randint(0,len(id_filter2))
                print(f"You should play '{name[id_filter2[x]-1]}'")
                print(f"Here is some more info about '{name[id_filter2[x]-1]}'" )
                print(data.loc[id_filter2[x]-1])
        elif z=="2":
             print("Goodbye, hope we were helpful")
             break
        else:
             print("Please enter a valid number")
#main

main()#calls the main function







#sources
#Board Game Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://www.kaggle.com/datasets/mrpantherson/board-game-data
# Board Game Dataset
# Website Name: Code.org
# URL: https://code.org/en-US
# Dataset Source:https://www.kaggle.com/datasets/mrpantherson/board-game-data
# Creator: Mr. Pantherson
