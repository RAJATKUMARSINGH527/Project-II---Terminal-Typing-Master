import random
import time
import json

import os
os.system("color")
from termcolor import colored

def UpdateLeaderBoard(username,wpm):
    
    #json--python dict
    # with open("LeaderBoard.json","r") as f:
    #     leaderboard = json.load(f)
    try:
        with open("LeaderBoard.json","r") as f:
            leaderboard = json.load(f)
    
    except FileNotFoundError: #To handle the Error of empty file
        leaderboard = {}
    
    leaderboard[username] = wpm
    
    #sort
    leaderboard = dict(sorted(leaderboard.items(),key = lambda item:item[1] ,reverse=True) )

    #python-dict ==>json
    with open ("LeaderBoard.json","w") as g:
        json.dump(leaderboard,g)
    
def ShowLeaderBoard():
    with open ("LeaderBoard.json","r") as file :
        leaderboard=json.load (file)
    return leaderboard #leaderboard ek dictionary hai

def main():
    # UpdateLeaderBoard
    print(colored("\nWelcome to Terminal Typing Master!⌨️","red","on_white"))
    username = input("\nEnter your username :- ")

    while True:
        print("\nOptions:\n")
        print("1. Start Typing Test ⌨️")
        print("2. Show Leaderboard")
        print("3. Exit ❌")
        choice = input("\nEnter your choice :- ")

        if choice == "1":
            category = input("\nChoose a category (e.g., animals, fruits): ")
            print()
            words = load_words_from_category(category)
            start_time = time.time()
            words_typed = 0

            for word in words:
                print(word)
                user_input = input("\nType the word (Ctrl + Q to quit ❌): ")
                print()
                if user_input.lower() == "ctrl+q":
                    print("Exiting❌ Typing Test...")
                    break
                words_typed += 1

            end_time = time.time()
            time_taken = end_time - start_time
            wpm = calculate_wpm(words_typed, time_taken)
            print(f"\nWords Per Minute (WPM): {wpm:.2f}")
            
            UpdateLeaderBoard(username,wpm)
            
        elif choice=="2":
            # UpdateLeaderBoard(username,wpm)
            my_leaderboard = ShowLeaderBoard()

            print()
            print(colored("LeaderBoard :- ","green"))
            print()

            # print(my_leaderboard)
            rank = 1
            for j in my_leaderboard:
                
                print(str(rank)+".    "+ j +"     - "+str(my_leaderboard[j])+" WPM")
                rank+=1
            
        elif choice == "3":
            print(colored("\nExiting❌ Terminal Typing Master⌨️...\n","cyan","on_white"))
            break

        else:
            print(colored("\nInvalid choice!!❎ Please choose again.","black","on_light_red"))

def load_words_from_category(category):
    if category == "animals":
        return ["cat", "dog", "elephant", "lion", "tiger"]
    elif category == "fruits":
        return ["apple", "banana", "orange", "grape", "watermelon"]
    else:
        print("Invalid category. Using default category 'animals'.")
        return ["cat", "dog", "elephant", "lion", "tiger"]

def calculate_wpm(words_typed, time_taken):
    wpm = (words_typed / 5) / (time_taken / 60)  # Assuming 5 words per sentence
    return wpm

if __name__ == "__main__":
    main()