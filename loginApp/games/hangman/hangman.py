'''
"Hangman"
Eshaan Tripathi
10/18/22
Hangman game.
'''

#import sys library
import sys

#ask user for word they want to guess
initial_word = input("Enter the word you want to play for: ")

#print a bunch of new lines to block people from seeing original word
for i in range(20):
    print("\n")

#set the guess word as nothing
initial_guess_word = ""

#set the quess word as a bunch of stars at the length of the word
for i in range(len(initial_word)):
    initial_guess_word+="*"

#define win_count, count, lose_count, and lose_list variable which stores the graphics which symbolize hangman body parts
win_count = 0
count = 0
lose_count = 0
lose_list = ["o\n","I\n","/","\\\n","I\n","/","\\"]
#define the lose_li list which will store the body parts the user has collected due to their failure
lose_li = []

guessed_letters = []

#while loop to loop through each character of the original word as long as the user doesnt win
while win_count < len(initial_word):
    #ask for guess
    guess = input("\nEnter your guess: ")
    
    while guess in guessed_letters:
        guess = input("\nYou've already guessed that!: ")
    while guess not in initial_word:
        #if it is wrong, append a part of the lose_list to lose_li, and print the body parts
        lose_li.append(lose_list[lose_count])
        for i in lose_li:
            print(i,end=''),
        lose_count+=1

        #print the resulting guess word
        print(f"\nGuessed: {initial_guess_word}")

        #ask for new guess
        guess = input("Enter your guess: ")

    
    #find the index of the guess
    guess_indx = initial_word.index(guess)
    #make a new list that symbolizes the initial_guess_word
    list1 = list(initial_guess_word)
    #set the guess into its proper position in that list
    list1[guess_indx] = guess
    #mend the list1 list back into a string
    initial_guess_word = ''.join(list1)

    #print the result
    print(f"\nGuessed: {initial_guess_word}")
    #add to the win_count
    win_count+=len(guess)
    #print congratulation
    print("Nice guess!")

    #add one to the total count
    count+=1

    #check if the player has lost. If they have, print the losing statement and exit program
    if lose_count == 7:
        print("You lost!")
        sys.exit()

#once the player has won, print congratulation
print("Congrats you won")