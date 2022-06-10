#Evan Wang
#6/4/2022
#To help with time slots

#Evan Wang
#6/4/2022
#To help with time slots

def main():
    import csv
    print("Hello welcome to Evan's Marathon")
    response = (input("PLease enter a time you would like to race at"))
    with open("sun_data.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for column in readCSV:
                if response == column:
                                print("Yes " + str(response) + "is available at this time.")
                                response1 = input("Would you like to schedule to race at this time?")
                                if response1.lower() == "yes":
                                        print("Thank you your time has been scheduled")
                                        break
                                else:
                                        print("Very well your time has not been scheduled please choose another time to race")
    print("Sorry that time was not found please choose again")
    csvfile.close()
main()