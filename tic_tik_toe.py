theboard = {"7": " ","8":" ","9":" ",
"4":" ","5":" ","6":" ",
"3":" ","2":" ","1":" "
}

Board_keys = []

for keys in Board_keys:
    Board_keys.append(keys)
    
def printbord(board):
        print(board["7"],"|",board["8"],"|",board["9"])
        print("--+-+--")
        print(board["4"],"|",board["5"],"|",board["6"])
        print("--+-+--")
        print(board["1"],"|",board["2"],"|",board["3"])
        
def game():
        
        turn = "X"
        count = 0
        
        for i in range(10):
            printbord(theboard)
            print("It is your turn",turn,". Which place do you want to go")
            move = input()
            
            if theboard[move] == " ":
                theboard[move] = turn
                count += 1
                
            
            else:
                print("The place is already full")
                print("Move at which place")
                
                continue
            
            
            if count >= 5:
                if theboard["7"] == theboard["8"] == theboard["9"] != " ":
                    printbord(theboard)
                    print("\n Game Over \n")
                    print(" *** ",turn,". Won"," *** ")
                    break
                elif theboard["6"] == theboard["5"] == theboard["4"] != " ":
                    printbord(theboard)
                    print("\n Game Over \n")
                    print(" *** ",turn,". Won"," *** ")
                    break
                elif theboard["3"] == theboard["2"] == theboard["1"] != " ":
                    printbord(theboard)
                    print("\n Game Over \n")
                    print(" *** ",turn,". Won"," *** ")   
                    break
                elif theboard["7"] == theboard["4"] == theboard["1"] != " ":
                    printbord(theboard)
                    print("\n Game Over \n")
                    print(" *** ",turn,". Won"," *** ")   
                    break
                elif theboard["2"] == theboard["5"] == theboard["8"] != " ":
                    printbord(theboard)
                    print("\n Game Over \n")
                    print(" *** ",turn,". Won"," *** ")   
                    break
                elif theboard["3"] == theboard["6"] == theboard["9"] != " ":
                    printbord(theboard)
                    print("\n Game Over \n")
                    print(" *** ",turn,". Won"," *** ")   
                    break
                
            if count == 9:
                print("Game Over")
                
            if turn == "X":
                turn = "O"
                
            else:
                turn = "X"
                
        Restart = input("Do you want to Play again (y/n): ")
        if Restart == "y":
            for key in Board_keys:
               theboard[key] = " "
                    
            game()
                
if "__main__" == __name__:
    game()