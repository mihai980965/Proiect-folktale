coins = 0
print("Welcome to the Folktale Game!")
print("You need to collect 10 coins to win the game!")
x = input("Start the game by typing 'start': ")
if( x == "start"):
    print("You have started the game!🎉🎉")
    print("You will need to assemble words to collect coins.")
    print("You will be given a set of letters and you need to form a word using those letters.")    
else:
    while(x != "start"):
        print("Try again! Type 'start' to start the game.")
        x = input()
x = input("Type 'ready' to start the game: ")
if(x == "ready"):
    print("You are ready to start the game!🎉🎉")
    print("You will be given a set of letters and you need to form a word using those letters.")
    print("You will get 1 coin for each correct word you form.")
    print("You need to collect 10 coins to win the game!")
    print("Good luck!")
    print("Your first set of letters is: HISF")
else:
    while(x != "ready"):
        print("Try again! Type 'ready' to start the game.")
        x = input()
    print("You are ready to start the game!")
    print("You will be given a set of letters and you need to form a word using those letters.")
    print("You will get 1 coin for each correct word you form.")
    print("You need to collect 10 coins to win the game!")
    print("Good luck!")
    print("Your first set of letters is: HISF")
x = input()
if(x == "FISH"):
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("Your next set of letters is: KILM")
else:
    while(x != "FISH"):
        print("Try again! Type the correct word to form using the letters given.")
        x = input()
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("Your next set of letters is: KILM")    
x = input()
if(x == "MILK"):
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("Your next set of letters is: RTAE")
else:
    while(x != "MILK"):
        print("Try again! Type the correct word to form using the letters given.")
        x = input()
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("Your next set of letters is: RTAE")
x = input()
if(x == "TEAR"):
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("Your next set of letters is: TNEPLA")
else:
    while(x != "TEAR"):
        print("Try again! Type the correct word to form using the letters given.")
        x = input()
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("Your next set of letters is: TNEPLA")
x = input()
if(x == "PLANET"):
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("Your next set of letters is: NTOANI")
else:
    while(x != "PLANET"):
        print("Try again! Type the correct word to form using the letters given.")
        x = input()
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("Your next set of letters is: NTOANI")
x = input()
if(x == "NATION"):
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("The next set of words will be 2 coins each!")
    print("Your next set of letters is: ROTMPCUE")
else:
    while(x != "NATION"):
        print("Try again! Type the correct word to form using the letters given.")
        x = input()
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("The next set of words will be 2 coins each!")
    print("Your next set of letters is: ROTMPCUE")
x = input()
if(x == "COMPUTER"):
    coins += 2
    print("Correct! + 2 ", coins , " coins")
    print("Your next set of letters is: REDANG")
else:
    while(x != "COMPUTER"):
        print("Try again! Type the correct word to form using the letters given.")
        x = input()
    coins += 2
    print("Correct! + 2 ", coins , " coins")
    print("Your next set of letters is: REDANG")
x = input()
if(x == "DANGER"):
    coins += 2
    print("Correct! + 2 ", coins , " coins")
    print("The last word you need to complete the first level is 1 coin but its the hardest word to form!")
    print("Your next set of letters is: KONLCU")
else:
    while(x != "DANGER"):
        print("Try again! Type the correct word to form using the letters given.")
        x = input()
    coins += 2
    print("Correct! + 2 ", coins , " coins")
    print("The last word you need to complete the first level is 1 coin but its the hardest word to form!")
    print("Your next set of letters is: KONLCU")
x = input()
if(x == "UNLOCK"):
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("You have collected ", coins , " coins!")
    print("You collected all the coins! Congrats!")
    print("You need to complete the next level to win the game!")
    print("Make the next word: 3 - 1 - 20")
else:
    while(x != "UNLOCK"):
        print("Try again! Type the correct word to form using the letters given.")
        x = input()
    coins += 1
    print("Correct! + 1 ", coins , " coins")
    print("You have collected ", coins , " coins!")
    print("You need to complete the next level to win the game!")
    print("Make the next word: 3 - 1 - 20")
x = input()
if(x == "CAT"):
    print("You collected all the coins! Congrats!🎉🎉🎉❤❤🤩🤩")
else:
    while(x != "CAT"):
        print("Try again! Type the correct word to form using the letters given.")
        x = input()
    print("You collected all the coins! Congrats!🎉🎉🎉❤❤🤩🤩")
