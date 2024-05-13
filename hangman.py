import random
from variation import fetchHangman

def readFile(file):
    with open(file,'r') as f:
        words = f.readlines()
    return words

def gamePlay(words):
    word = words[random.randint(0,len(words))]
    word = word[:-1]

    blanks = '_ ' * len(word)

    chances = 6

    currentHangman = fetchHangman(chances)

if __name__ == '__main__':
    words = readFile('words.txt')
    score = 0

    gamePlay(words)