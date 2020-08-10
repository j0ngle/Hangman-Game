from string import ascii_lowercase
from words import getRandomWord   #imports the words.py file
import random;
import time;

usedLetters_p1 = "";
usedLetters_cpu = "";

def getWord():
    return getRandomWord();

def formatDisplay(input):
    #Stringbuilder
    output_p1 = "";
    for i in range(0, len(input)):
        if (usedLetters_p1.find(input[i]) == -1): #finds letter in usedLetter string
            output_p1 += "*";
        else:
            output_p1 += input[i];

    output_cpu = "";
    for i in range(0, len(input)):
        if (usedLetters_cpu.find(input[i]) == -1):
            output_cpu += "*";
        else:
            output_cpu += "^";

    #Win Detection
    if (output_p1.find("*") == -1):
        print("You win!");
        exit();
    if (output_cpu.find("*") == -1):
        print("HangBot Wins!");
        exit();

    print("PLAYER  : " + output_p1);
    print("COMPUTER: " + output_cpu);
    print();

def selectLetter():
    global usedLetters_p1;
    while True:
        letter = input("Select a letter: ");
        if (usedLetters_p1.find(letter) != -1):
            print("Letter already selected, try again");
        else:
            usedLetters_p1 += letter;
            if (word.find(letter) != -1):
                print("Letter found!");
            else:
                print("Letter not found :(");
            formatDisplay(word); #displays game state
            selectLetter_CPU_easy();
            return;



"""CPU ALGORITHMS"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def selectLetter_CPU_easy():
    print("HangBot: Thinking...");
    time.sleep(2);

    global usedLetters_cpu;
    letter = random.choice(letters);
    #letters.remove(selected);
    usedLetters_cpu += letter;

    if (word.find(letter) != -1):
        print("HangBot found a letter\n");
    else:
        print("HangBot guessed incorrectly!\n");

    formatDisplay(word);
    selectLetter();

word = getWord();

selectLetter();
#formatDisplay(word);



