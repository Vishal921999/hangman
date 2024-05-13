import random
from variation import fetchHangman

def gamePlay(word,blanks,chances,currentHangman,wordDict):

    guessedLetters = []
    isGuessedCorrectly = False

    while chances >= 0:
        # exit condition - win
        if ''.join(blanks) == word:
            isGuessedCorrectly = True
            break
        
        print(currentHangman)

        # exit condition - lose
        if(chances == 0):
            break

        print(f"Guess the word: {' '.join(blanks)}")
        print(f"Letters used: {guessedLetters}")

        letter = input("Guess a letter: ")

        if letter in guessedLetters:
            print("Letter already guessed. Please try again!")

        else:
            if letter in wordDict:
                for index in wordDict[letter]:
                    blanks[index] = letter
            else:
                chances -= 1
                currentHangman = fetchHangman(chances)
            guessedLetters.append(letter)
            
    return isGuessedCorrectly


def readFile(file):
    with open(file,'r') as f:
        words = f.readlines()
    return words

def createDictionary(word):
    wordDict = {}

    for i,character in enumerate(word):
        if character not in wordDict:
            wordDict[character] = [i]
        else:
            wordDict[character].append(i)
    return wordDict

def initGame(words):
    word = words[random.randint(0,len(words))][:-1]
    blanks = ['_'] * len(word)
    chances = 6
    currentHangman = fetchHangman(chances)
    wordDict = createDictionary(word)
    return word, gamePlay(word,blanks,chances,currentHangman,wordDict)

def playAgain():

    playAgain = True

    while playAgain:
        option = input("Play again? (Y/N): ")

        if option.lower() == "n":
            print("Thanks for playing!\n")
            playAgain = False
            break

        elif option.lower() == "y":
            print("*---- NEW GAME ----*\n")
            break

        else:
            print("Invalid input")
    
    return playAgain

if __name__ == '__main__':
    words = readFile('words.txt')
    score = 0

    while True:
        word, result = initGame(words)

        if result:
            score += 10
            print(f"\nYou guessed {word} correctly!")

        else:
            print(f"Oops! You hanged the man :(")
            print(f"The word was: {word}")

        print(f"Score: {score}")
        print("\n==============================\n")

        if not playAgain():
            break 
    
    print(f"Final Score: {score}\n")