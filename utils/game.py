"""


A wrongly_guessed_letters attribute that contains a list of strings where each element will be a letter guessed by the user that is not in the word_to_find.

A turn_count attribute that contain the number of turns played by the player. This will be represented as an int.

An error_count attribute that contains the number of errors made by the player.

A play() method that asks the player to enter a letter. Be careful that the player shouldn't be allowed to type something else than a letter, and not more than a letter. If the player guessed a letter well, add it to the correctly_guessed_letters list. If not, add it to the wrongly_guessed_letters list and add 1 to error_count.

A start_game() method that:

will call play() until the game is over (because the use guessed the word or because of a game over).
will call game_over() if lives is equal to 0.
will call well_played() if all the letter are guessed.
will print correctly_guessed_letters, bad_guessed_letters, life, error_count and turn_count at the end of each turn.
A game_over() method that will stop the game and print game over....

A well played() method that will print You found the word: {word_to_find_here} in {turn_count_here} turns with {error_count_here} errors!.

Constraints"""

class Hangman:

    #A  attribute that contains a list of words. Out of these words, one will be selected as the word to find. 
    # The list must also contain the following words: ['becode', 'learning', 'mathematics', 'sessions'].
    possible_words =['becode', 'learning', 'mathematics', 'sessions']
    #A  attribute that contains a list of strings. Each element will be a letter of the word.
    word_to_find = []
    #A  attribute that contains the number of lives that the player still has left. It should start at 5.
    lives = 5
    #A correctly_guessed_letters attribute that contains a list of strings where each element will be
    #  a letter guessed by the user. At the start, it should be equal to: _ _ _ _ _, with the same number of _ as the length of the word to find.
    #Each time the player finds a letter, replace the _ with the letter that the user suggested. 
    # If the word contains multiple times the same letter, the letter should be revealed at every place it appears in the word to find.
    #For example, if the word to find is P A P E R and the first guess of the user is P then correctly_guessed_letters should be 
    # equal to P _ P _ _.

    correctly_guessed_letters=[]

    #attribute that contains a list of strings where each element will be a letter guessed by the user that is not in the word_to_find.
    wrongly_guessed_letters =[]

    #A attribute that contain the number of turns played by the player. This will be represented as an int.
    turn_count = 0

    #An  attribute that contains the number of errors made by the player.
    error_count = 0

    good_count = 0

    #METHODS : 

   
    def play(self,secret_word):
      
        guessedLetter = input("Guess a letter : ")
        
        self.word_to_find =  list(secret_word)
        print("word to find",self.word_to_find)
        while len(guessedLetter)>1 :
            guessedLetter = input("Guess a letter : ")

        
        if guessedLetter in secret_word :
            index = self.word_to_find.index(guessedLetter)
            self.correctly_guessed_letters[index]= guessedLetter
            print("Right guessed !")
            self.good_count +=1
            #self.correctly_guessed_letters.append(guessedLetter)
        else : 
            print("wrong X !")
            self.lives -= 1
            self.wrongly_guessed_letters.append(guessedLetter)
            self.error_count +=1 



    #will print correctly_guessed_letters, bad_guessed_letters, life, error_count and turn_count at the end of each turn.

    def start_game(self) : 
        secret_word = "Math"
        #call play until game over or well guessed
        self.correctly_guessed_letters = ['_' for i in secret_word]

        #while self.error_count < self.lives or len(self.correctly_guessed_letters) != len(self.word_to_find):
        while True: 
            self.play(secret_word)
            if self.lives == 0: 
                self.game_over()
                break
            elif self.good_count == len(self.word_to_find):
                print(self.good_count , len(self.word_to_find))
                self.well_played()
                break
            print(f"correct guessed letters :{self.correctly_guessed_letters} , wrong guess letters{self.wrongly_guessed_letters} , more lives : {self.lives } , n_errors : {self.error_count} ,{self.turn_count}")
    
                  
    def game_over(self) :
        """#method that will stop the game and print game over...."""
        print("Game over")
        return True

    #method that will print You found the word: {word_to_find_here} in {turn_count_here} turns with {error_count_here} errors!.
    def well_played(self):
        word_find = "".join(self.word_to_find)
        
        print(f" You found the word {word_find} in { self.turn_count } turns with {self.error_count} errors!")


