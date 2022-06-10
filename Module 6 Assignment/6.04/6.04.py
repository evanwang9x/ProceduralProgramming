#Evan Wang
#6/10/2022
#To help determine what to do for colleges.

def studentLogin():
    import csv
    print("Hello, please create your college account and answer the survey to help us determine what classes to increase or downsize in.")
    response = input("Hello what is your name?")
    response1 = input("Hello there " + response + " please enter a password that is at between 8-16 characters long and has one uppercase character.")
    if len(response1) < 8:
        print("Please make sure that your password is at least 8 characters long")
        exit()
    if len(response1) > 16:
        print("Please make sure that your password at most is 16 characters long")
        exit()
    lower = any(response1.islower() for response1 in response1)
    upper = any(response1.isupper() for response1 in response1)
    if not upper:
        print("Please make sure that your password has at least one character in upper case")
        exit()
    if not lower:
        print("Please make sure that your password has at least one character in lower case")
        exit()
    #I realized too late that the file path wouldn't work on your computer so I will have to hard code the step in as a variable
    #with open('D:/Python Course Information/Module 6 Assignment/6.04/info.csv', 'r') as csvfile:
        #readCSV = csv.reader(csvfile, delimiter=',')
        #for column in readCSV:
            #csvwriter = csv.writer(csvfile)
            #csvwriter.writerow([response, response1])
            #print(column)
    #csvfile.close()
studentLogin()

def main():
    studentLogin()






main()