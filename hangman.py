import random
from variation import fetchHangman

def gamePlay(word,blanks,chances,currentHangman,wordDict):
    guessedLetters = set()
    while chances >= 0:
        if ''.join(blanks) == word:
            print("Game Complete")
            break
        
        print(currentHangman)
        print(f"Guess the word: {' '.join(blanks)}")
        letter = input("Guess a letter in word: ")

        if letter in guessedLetters:
            print("Letter already guessed. Please try again!")

        else:
            if letter in wordDict:
                for index in wordDict[letter]:
                    blanks[index] = letter
            else:
                chances -= 1
                currentHangman = fetchHangman(chances)
            guessedLetters.add(letter)
            
            


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
    gamePlay(word,blanks,chances,currentHangman,wordDict)

if __name__ == '__main__':
    words = readFile('words.txt')
    score = 0

    initGame(words)
