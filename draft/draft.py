
def get_word() -> str: 
    """This function prompts the chooser player for his word and returns that word"""
    word = input("What is your word master ?")
    return word 

def get_lives() -> int : 
    """This function which prompts the chooser player for a number of lives and returns this number of lives"""
    n_of_lives = int(input("Enter the number of lives master : "))
    return n_of_lives

def  get_guess( suggested_letters=[]) -> str:
    """function which takes as argument: suggested_letters,
      a list of the letters suggested by the guesser player throughout the game"""


    """The function does the following:
    prompts the user for a letter:
    if already suggested letter, prompt again
    returns the guessed letter"""
    guessedLetter = input("Guess a letter : ")

    while len(guessedLetter)>1 :
        guessedLetter = input("Guess a letter : ")

    suggested_letters.append(guessedLetter)

    return guessedLetter


def assess_guess(secret_word, guessed_letter, lives_left) -> int  :
    """which takes as argument:
    secret_word, the word to be guessed
    guessed_letter, the last letter suggested from guesser player
    lives_left, lives left
    assess_guess(...) does the following:
    outputs if the guess is correct or not
    returns the current lives of the player depending on the outcome of the guess"""
    
    if guessed_letter in secret_word :
        print("Well guessed ! ")
        
    else : 
        print("wrong X !")
        lives_left -=1 
    return lives_left
     
#koni       ,#k 
def display_word(secret_word, suggested_letters) -> bool :
    """secret_word, the word to be guessed
    suggested_letters, a list of the letters suggested by the guesser player throughout the game
    display_word(...) does the following:
    displays the secret word with white spaces between the letters, hiding the non-guessed letters by replacing them with '_'
    returns True if the correct word has been found, False otherwise"""
    found = False
    count = 0
   
    printed_result_word=['_' for i in secret_word]

    print(suggested_letters)
    for guessed_letter in suggested_letters :
        if guessed_letter in secret_word :
            index = secret_word.index(guessed_letter)
            printed_result_word[index] = guessed_letter
            count +=1
            if(count == len(secret_word)):
                print("found")
                found= True
        else : 
            found = False 
    #k__i
    print("".join(printed_result_word[0:len(secret_word)]))
    return found


def main():
    """function which orchestrates a full game"""
    suggested_letters = []#k

    #The master player : 
    secret_word = get_word() 
    lives_left = get_lives()
    win = False
    #The player who guess
    while lives_left > 0 and win is not True  : 

        guessed_letter = get_guess(suggested_letters)
        lives_left = assess_guess(secret_word, guessed_letter, lives_left) 
        print("number of lives left :",lives_left)
        win = display_word(secret_word, suggested_letters)

    if win  : 
            print("Game Win ! ")
    else : 
            print("Game Failed")

main()