

class Hangman:

    possible_words =['becode', 'learning', 'mathematics', 'sessions']
    word_to_find = []
    lives = 5

    correctly_guessed_letters=[]
    wrongly_guessed_letters =[]

    turn_count = 0
    error_count = 0
    good_count = 0

   
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