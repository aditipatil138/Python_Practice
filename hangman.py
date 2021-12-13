import random
from words import words
import string

def valid_word(words):
    computer_choice_word = random.choice(words) #Compuetr selects random word from words list
    while '-' in computer_choice_word or ' ' in computer_choice_word:
        computer_choice_word = random.choice(words)
    return computer_choice_word.upper()

def hangman():
    computer_choice_word = valid_word(words)
    computer_word_letters = set(computer_choice_word)
    valid_alphabets = set(string.ascii_uppercase)
    used_user_letters = set() #set of user guessed letters
    
    lives = 6
    
    while len(computer_word_letters) > 0 and lives > 0:
        #' '.join(['a', 'b', 'cd']) => 'a b cd'
        print("You have ", lives ,"lives and The letters that you have guessed are: ",' '.join(used_user_letters))
        
        #W-RD
        word_display_list = [letter if letter in used_user_letters else '-' for letter in computer_choice_word]
        print("The word guessed so far is: ",' '.join(word_display_list))
        
        user_input_letter = input("Enter your Guess Letter: ")
        
        if user_input_letter in valid_alphabets - used_user_letters:
            used_user_letters.add(user_input_letter)
            if user_input_letter in computer_word_letters:
                computer_word_letters.remove(user_input_letter)
            else:
                lives = lives - 1
                print("The letter you guessed is not in the word! Try again")
        
        elif user_input_letter in used_user_letters:
            print("\nYou have already guessed this letter try again!")
        
        else:
            print("\nYou have entered an invalid character! Please enter a valid alphabet to guess")
    
    if lives == 0:
        print("You Lost!! You have used all your lives! The word is ", computer_choice_word)
    else:
        print("You have guessed the word ", computer_choice_word, "Congratualtions!!")
    
hangman()