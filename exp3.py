#Hangman game
word=input("PLAYER 1 \n Enter word : ")
print("\n"*10)
life=6
letters=set()
print("PLAYER2")
while life>0:
    print("LIFE : ","|"*life)
    print("Word :  ","".join(i if i in letters else "_" for i in word ))
    guess=input("Guess a letter : ")
    if guess in word:
        letters.add(guess)
    else:
        life-=1
    if len(set(word))==len(letters):
        print("You guessed the word : ",word)
        break
if life==0:
    print(f"Game over, the word was {word} ")