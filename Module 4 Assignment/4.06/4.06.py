#Evan Wang
#6/10/22
#To help streamline the check in process for a battle royale game
def main():
    print("Hello welcome to Evan's Battle Royale")
    response = input("To search to see if a player is registered please enter 1, To find the number of a specific user please enter 2, To print a list of all players and their information please select 3.")
    
    import csv
    result =0 
    if response == "1":
        response1 = input("Please enter the name of the player that you wish to find.")
        with open("battle_royale.csv") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for column in readCSV:
                for row in column:
                    if response1 == row:
                        result +=1
        if result == 1:
            print("Yes " + (response1) + " is registered in this game")
        else: 
            print("No " + (response1) + " is not registered in this game")
        csvfile.close()

    elif response == "2":
        response1 = (input("Please enter the number of the user"))
        with open("battle_royale.csv") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for column in readCSV:
                for row in column:
                    if row == response1:
                        print("Yes " + (response1) + " is registered in this game as " + column[1])
                        break

    else:
        with open("battle_royale.csv") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for column in readCSV:
                print(column)
        csvfile.close()





        main()