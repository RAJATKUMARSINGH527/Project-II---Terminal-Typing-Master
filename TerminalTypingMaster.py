# Importing the necessary modules for the script:

# import random  # FOR CHOOSING RANDOM WORDS

import time  # TO CALCULATE REAL TIME 
import json  # TO USE JSON OBJECTS

# Importing modules for terminal color output:
import os
os.system("color")
from termcolor import colored  # TO GIVE TERMINAL COLOR

# Definition of the function to update the leaderboard:
def UpdateLeaderBoard(username, wpm):
    """
    Update the leaderboard with the username and WPM score.
    """
    # Attempting to open and read the contents of the leaderboard file:
    try:
        with open("LeaderBoard.json", "r") as f:  # Open any file within the main file
            leaderboard = json.load(f)  # Convert JSON object to Python dictionary
    # Handling the case where the leaderboard file is not found:
    except FileNotFoundError:
        leaderboard = {}  # To handle the Error of an empty file
    
    # Updating the leaderboard with the new user's data:
    leaderboard[username] = wpm  # Update the data of the user
    
    # Sorting the leaderboard by WPM score in descending order:
    leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))
    
    # Writing the updated leaderboard back to the JSON file:
    with open("LeaderBoard.json", "w") as g:  # "R" ==> READ , "W" ==> WRITE
        json.dump(leaderboard, g)  # DUMP ==> DICT TO JSON OBJECT

# Function to display the leaderboard:
def ShowLeaderBoard():
    """
    Load and return the leaderboard.
    """
    # Opening the leaderboard file and loading its contents:
    with open("LeaderBoard.json", "r") as file:
        leaderboard = json.load(file)
    return leaderboard  # leaderboard is a dictionary

# Main function to orchestrate the program's flow:
def main():
    """
    Main function to run the typing test game.
    """
    # Printing a welcome message:
    print(colored("\nWelcome to Terminal Typing Master!⌨️", "red", "on_white"))
   
    
    # Asking for the user's username:
    username = input("\nEnter your username :- ")
    
    while True:
        # Displaying the menu options:
        print("\nOptions:\n")
        print("1. Start Typing Test ⌨️")
        print("2. Show Leaderboard")
        print("3. Exit ❌")
        
        # Asking for the user's choice:
        choice = input("\nEnter your choice :- ")
        
        if choice == "1":
            # Asking the user to choose a category:
            category = input("\nChoose a category (e.g., animals, fruits): ")
            print()
            # Loading words based on the chosen category:
            words = load_words_from_category(category)  # An array containing some words
            start_time = time.time()  # Storing the current time
            
            # Variables to track typing performance:
            words_typed = 0
            accurate_word = 0
            
            # Looping through each word:
            for word in words:
                print(word) 
                # Asking the user to type the word:
                user_input = input("\nType the word (Ctrl + Q to quit ❌): ")
                print()
                if user_input.lower() == "ctrl+q":
                    print("Exiting❌ Typing Test...")
                    break

                # Checking if the typed word matches the actual word:
                if user_input == word:
                    accurate_word += 1
                words_typed += 1
            print("\nAccurate Words -->> ",accurate_word)
            
            # Calculating performance metrics:
            end_time = time.time()  # Storing the current time
            time_taken = end_time - start_time  # Calculating the time taken
            wpm = calculate_wpm(words_typed, time_taken, accurate_word)  # Calculating WPM
            
            # Displaying the WPM score:
            print(f"\nWords Per Minute :- {wpm:.2f} WPM")  # 'f' string
            print()
            
            # Updating the leaderboard with the user's performance:
            UpdateLeaderBoard(username, wpm)
        
        elif choice == "2":
            # Displaying the leaderboard:
            my_leaderboard = ShowLeaderBoard()  # A dictionary containing real-time data

            print(colored("\nLeaderboard :- \n", "green"))
          
            # Displaying each user's performance:
            rank = 1
            for user, wpm in my_leaderboard.items():
                print(f"{rank}.  {user}    ->  {wpm:.2f} WPM")
                rank += 1
            print()
            # rank=1
            # for j in my_leaderboard:
                # print(f"{rank}.  {j} ->  {my_leaderboard[j]:.2f} WPM")
                # print(str(rank)+".    "+ j +"     - "+str(my_leaderboard[j])+" WPM")
                # rank += 1
        
        elif choice == "3":

            # Exiting the program:
            print(colored("\nExiting❌ Terminal Typing Master⌨️...\n", "black", "on_white"))
            break

        else:
            # Handling invalid choices:
            print(colored("\nInvalid choice!!❎\n", "white", "on_light_red"))
            print("Please choose again!!")
           

# Function to load words from a specific category:
def load_words_from_category(category):
    """
    Load and return words based on the chosen category.
    """
    if category == "animals":
        return ["cat", "dog", "elephant", "lion", "tiger"]
    elif category == "fruits":
        return ["apple", "banana", "orange", "grape", "watermelon"]
    else:
        print("Invalid category!! Using default category -> 'animals'\n")
        return ["cat", "dog", "elephant", "lion", "tiger"]

# Function to calculate WPM (Words Per Minute):
def calculate_wpm(words_typed, time_taken, accurate_word):
    """
    Calculate and return the WPM score.
    """
    wpm = (accurate_word / 5) / (time_taken / 60)  # Assuming 5 words per sentence
    return wpm

# Running the main function if the script is executed directly:
if __name__ == "__main__":
    main()
