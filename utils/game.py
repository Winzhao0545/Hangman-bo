import random
class Hangman:

    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        #create a list contains _ _ _ _  ,length should be the same as word_to_find
        self.correctly_guessed_letters  = []
        for i in range(len(self.word_to_find)):
            self.correctly_guessed_letters.append('_') 
        self.wrongly_guessed_letters = [] 
        self.turn_count = 0
        self.error_count = 0

    
    def play(self):
        """
        Function that would :
        - ask player to enter a letter
        - check if the input is valid
        - check if the guessed letter is correct or wrong
        """
        user_input = input("please enter a letter: ")
        if self.input_check(user_input):
            self.turn_count += 1
            # when player guessed the right letter, and it doesn't exist already in the correctly_gussed letters, replace the "_" with the correct letter
            if user_input.lower() in self.word_to_find and user_input.lower() not in self.correctly_guessed_letters:
                for i in range(len(self.word_to_find)):
                    if self.word_to_find[i] == user_input.lower():
                        self.correctly_guessed_letters[i]= user_input.lower()
            # when player guessed the right letter, but it already exist
            elif user_input.lower() in self.correctly_guessed_letters:
                print(f"You already guessed the letter {user_input} correctly!")
                self.lives -= 1
            #when player guessed the wrong letter, subtract 1 from lives, add 1 to error_count, add the wrong guessed letter to the list
            else:
                self.lives -= 1
                self.error_count += 1
                if user_input not in self.wrongly_guessed_letters:
                    self.wrongly_guessed_letters.append(user_input)




    def input_check(self, value):
        """
        Function to check if the input from the user is a letter and returns a boolean
        """
        allowed_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if value.lower() not in allowed_input:
            print("Please check if you entered a letter.")
            return False
        else:
            return True


    def start_game(self):
        """
        Function that would :
        - call play() until the game is over
        - call game_over() is player's lives is equal to 0
        - call well_played() if all letters are guessed
        - print the summary text at the end of each turn
        """
        print("Hello, welcome to this hangman game!")
        while True:
            self.play()
            print(f"Correctly guessed letters: {self.correctly_guessed_letters}\nWrongly guessed letters: {self.wrongly_guessed_letters}\nYour life :{self.lives}\nYour error counts:{self.error_count}\nYour turn counts: {self.turn_count}")
            if self.lives == 0:
                self.game_over()
                break
            elif self.correctly_guessed_letters == self.word_to_find:
                self.well_played()
                break

    def game_over(self):
        """Function that would stop the game once the player fails in guessing the correct word"""
        print("Game over...")
    
    def well_played(self):
        """Function that would congrat the player if they win"""
        word = "".join(self.word_to_find)
        print(f"You found the word '{word}' in {self.turn_count} turns with {self.error_count} errors!")
    