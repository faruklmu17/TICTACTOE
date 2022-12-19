myDictionary = {1: " ", 2: " ", 3: " ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
myDictionary1 = {1: "1", 2: "2", 3: "3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

def dictFunction(dashes):
    for i in range(1, 10):
        if i % 3 == 0:
            print(str(dashes[i]),end="")
            print()
            if i ==9:
                break
            else:
                print("-+-+-")
        else:
            print(str(dashes[i]),end="|")
def game():
    print("Each space of TIC TAC TOE board is represented by a number as shown below")

    dictFunction(myDictionary1)
    print()
    value = "X"
    num = "1"
    # this is used to keep track of the turns
    count = 0
    for i in range(100):
        if count ==9:
            print("It's a tie!")
            break

        print("Player"+num+",Type a number (1 to 9) to continue...:")
        key = int(input())
        if key>9 or key<=0:
            print("Not valid")
            continue
        else:
            if myDictionary[key] == " ":
                myDictionary[key] = value
                dictFunction(myDictionary)
                # if a spot is taken, updating the counter
                count+=1
                print("Checking count: ",count)
                if value == "X":
                    value = "O"
                    num = "2"
                else:
                    value = "X"
                    num = "1"
                # after 9 turns, if no one wins, declare that it's a tie

                if count>=5:
                    # 1 2 3
                    if myDictionary[1] == myDictionary[2] == myDictionary[3] == "X":
                        print("Player1 wins!")
                        break
                    elif myDictionary[1] == myDictionary[2] == myDictionary[3] == "O":
                        print("Player2 wins!")
                        break
                    # 4 5 6
                    elif myDictionary[4] == myDictionary[5] == myDictionary[6] == "X":
                        print("Player1 wins!")
                        break
                    elif myDictionary[4] == myDictionary[5] == myDictionary[6] == "O":
                        print("Player2 wins!")
                        break
                    # 7 8 9
                    elif myDictionary[7] == myDictionary[8] == myDictionary[9] == "X":
                        print("Player1 wins!")
                        break
                    elif myDictionary[7] == myDictionary[8] == myDictionary[9] == "O":
                        print("Player2 wins!")
                        break
                    # 1 4 7
                    elif myDictionary[1] == myDictionary[4] == myDictionary[7] == "X":
                        print("Player1 wins!")
                        break
                    elif myDictionary[1] == myDictionary[4] == myDictionary[7] == "O":
                        print("Player2 wins!")
                        break
                    # 2 5 8
                    elif myDictionary[2] == myDictionary[5] == myDictionary[8] == "X":
                        print("Player1 wins!")
                        break
                    elif myDictionary[2] == myDictionary[5] == myDictionary[8] == "O":
                        print("Player2 wins!")
                        break
                    # 3 6 9
                    elif myDictionary[3] == myDictionary[6] == myDictionary[9] == "X":
                        print("Player1 wins!")
                        break
                    elif myDictionary[3] == myDictionary[6] == myDictionary[9] == "O":
                        print("Player2 wins!")
                        break
                    # 1 5 9
                    elif myDictionary[1] == myDictionary[5] == myDictionary[9] == "X":
                        print("Player1 wins!")
                        break
                    elif myDictionary[1] == myDictionary[5] == myDictionary[9] == "O":
                        print("Player2 wins!")
                        break
                    # 3 5 7
                    elif myDictionary[3] == myDictionary[5] == myDictionary[7] == "X":
                        print("Player1 wins!")
                        break
                    elif myDictionary[3] == myDictionary[5] == myDictionary[7] == "O":
                        print("Player2 wins!")
                        break




            else:
                print("This position is already taken.Try again")


        print()
    #print("It's a tie!")

for i in range(100):
    game()
    print("Do you want to play again?Type Y or N")
    response = input()
    if response =="N":
        break
    else:
        print("Let's play again!")
        for i in myDictionary:
            myDictionary[i] = " "
        
