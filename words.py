#Function to fetch words

import random;

WORDLIST = "wordlist.txt"


def getRandomWord():
    with open("wordlist.txt") as file:
        words = file.read().split(); #splits words by whitespace
    return random.choice(words);
