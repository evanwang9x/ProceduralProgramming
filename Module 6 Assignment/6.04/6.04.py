#Evan Wang
#6/10/2022
#To help determine what to do for colleges.
response = ""
response1 = ""
totalStudents = 0

naturalSciVote = 0
mathmeticsVote = 0
foreignLanguageVote = 0
englishVote = 0
humanityVote = 0
socialScienceVote = 0
vAndpArts = 0

import csv
import random
import math

def studentLogin():
    #To make a userName and passWord
    global response
    global response1
    print("Hello, please create your college account and answer the survey to help us determine what classes to increase or downsize in.")
    response = input("Hello what is your name? ")
    response1 = input("Hello there " + response + " please enter a password that is at between 8-16 characters long and has one uppercase character. ")
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
def randomStatsGenerator():
    #To Randomly Generate Stats for the Vote
    global totalStudents
    global naturalSciVote
    global mathmeticsVote
    global foreignLanguageVote
    global englishVote
    global humanityVote
    global socialScienceVote
    global vAndpArts

    courses = 7
    totalStudents= random.randint(6300, 7300)

    rand_n = [ random.random() for i in range(courses) ]

    result = [ math.floor(i * totalStudents / sum(rand_n)) for i in rand_n ]

    result[random.randint(0,3)] += 1
    naturalSciVote = result[0]
    mathmeticsVote = result[1]
    foreignLanguageVote = result[2]
    englishVote = result[3]
    humanityVote = result[4]
    socialScienceVote = result[5]
    vAndpArts = result[6]



def main():
    global totalStudents
    global naturalSciVote
    global mathmeticsVote
    global foreignLanguageVote
    global englishVote
    global humanityVote
    global socialScienceVote
    global vAndpArts
    studentLogin()
    randomStatsGenerator()

    #Verification Process
    print("Hello there, please sign into your account and answer the survey")
    userName = input("Please enter your userName: ")
    passWord = input("Please enter your password: ")
    if(response != userName or response1 != passWord):
        print("Please enter the correct username or password")
        exit()
    print()
    print("Welcome to the survey all answers will be monitored and record")
    print("Here is a list of all classes that you can vote for: \n-naturalSciVote \n-mathmeticsVote \n-foreignLanguageVote \n-englishVote \n-humanityVote \n-socialScienceVote \n-vAndpArts")
    userVote = input("Please vote for your preferred class! ")
    #Adding userVote to all data
    totalStudents += 1
    if userVote == "naturalSciVote":
        naturalSciVote += 1
    elif userVote == "mathmeticsVote":
        mathmeticsVote += 1
    elif userVote == "foreignLanguageVote":
        foreignLanguageVote += 1
    elif userVote == "englishVote":
        englishVote += 1
    elif userVote == "humanityVote":
        humanityVote += 1
    elif userVote == "socialScienceVote":
        socialScienceVote += 1
    elif userVote == "vAndpArts":
        vAndpArts += 1
    else:
        print("Please make sure that you entered the name of the program correctly please.")
        exit()
    #Printing stats collected
    print()
    print()

    print("Here are the overall Results for the voting now: ")
    print("Total Class Size: " + str(totalStudents))
    print("Natural Science Vote Count: " + str(naturalSciVote))
    print("Mathmatics Vote Count: " + str(mathmeticsVote))
    print("Foreign Language Vote Count: " + str(foreignLanguageVote))
    print("English Vote Count: " + str(englishVote))
    print("Humanity Vote Count: " + str(humanityVote))
    print("Social Science Vote Count: " + str(socialScienceVote))
    print("Visual and Performing Arts Vote Count: " + str(vAndpArts))
    print("")

    #Compiling stats for determining what class to include
    natSciProf = 0
    if naturalSciVote > 1 and naturalSciVote <= 10:
        natSciProf =- 5
    elif naturalSciVote > 10 and naturalSciVote <= 100:
        natSciProf =- 3
    elif naturalSciVote > 100 and naturalSciVote <= 500:
        natSciProf = "No Change"
    elif naturalSciVote > 500 and naturalSciVote <= 1000:
        natSciProf =+ 2
    elif naturalSciVote >1000 and naturalSciVote <= 1500:
        natSciProf =+ 4
    elif naturalSciVote >1500 and naturalSciVote <= 2000:
        natSciProf =+ 6
    else:
        natSciProf =+ 10

    mathProf= 0
    if mathmeticsVote > 1 and mathmeticsVote < 10:
        mathProf=- 5
    elif mathmeticsVote > 10 and mathmeticsVote < 100:
        mathProf=- 3
    elif mathmeticsVote > 100 and mathmeticsVote < 500:
        mathProf= "No Change"
    elif mathmeticsVote > 500 and mathmeticsVote < 1000:
        mathProf=+ 2
    elif mathmeticsVote >1000 and mathmeticsVote < 1500:
        mathProf=+ 4
    elif mathmeticsVote >1500 and mathmeticsVote < 2000:
        mathProf=+ 6
    else:
        mathProf=+ 10

    foreignLangProf= 0
    if foreignLanguageVote > 1 and foreignLanguageVote < 10:
        foreignLangProf=- 5
    elif foreignLanguageVote > 10 and foreignLanguageVote < 100:
        foreignLangProf=- 3
    elif foreignLanguageVote > 100 and foreignLanguageVote < 500:
        foreignLangProf= "No Change"
    elif foreignLanguageVote > 500 and foreignLanguageVote < 1000:
        foreignLangProf=+ 2
    elif foreignLanguageVote >1000 and foreignLanguageVote < 1500:
        foreignLangProf=+ 4
    elif foreignLanguageVote >1500 and foreignLanguageVote < 2000:
        foreignLangProf=+ 6
    else:
        foreignLangProf=+ 10

    englishProf= 0
    if englishVote > 1 and englishVote < 10:
        englishProf=- 5
    elif englishVote > 10 and englishVote < 100:
        englishProf=- 3
    elif englishVote > 100 and englishVote < 500:
        englishProf= "No Change"
    elif englishVote > 500 and englishVote < 1000:
        englishProf=+ 2
    elif englishVote >1000 and englishVote < 1500:
        englishProf=+ 4
    elif englishVote >1500 and englishVote < 2000:
        englishProf=+ 6
    else:
        englishProf=+ 10

    humanityProf= 0
    if humanityVote > 1 and humanityVote < 10:
        humanityProf=- 5
    elif humanityVote > 10 and humanityVote < 100:
        humanityProf=- 3
    elif humanityVote > 100 and humanityVote < 500:
        humanityProf= "No Change"
    elif humanityVote > 500 and humanityVote < 1000:
        humanityProf=+ 2
    elif humanityVote >1000 and humanityVote < 1500:
        humanityProf=+ 4
    elif humanityVote >1500 and humanityVote < 2000:
        humanityProf=+ 6
    else:
        humanityProf=+ 10

    socialSciProf= 0
    if socialScienceVote > 1 and socialScienceVote < 10:
        socialSciProf=- 5
    elif socialScienceVote > 10 and socialScienceVote < 100:
        socialSciProf=- 3
    elif socialScienceVote > 100 and socialScienceVote < 500:
        socialSciProf= "No Change"
    elif socialScienceVote > 500 and socialScienceVote < 1000:
        socialSciProf=+ 2
    elif socialScienceVote >1000 and socialScienceVote < 1500:
        socialSciProf=+ 4
    elif socialScienceVote >1500 and socialScienceVote < 2000:
        socialSciProf=+ 6
    else:
        socialSciProf=+ 10

    visualProf= 0
    if vAndpArts > 1 and vAndpArts < 10:
        visualProf=- 5
    elif vAndpArts > 10 and vAndpArts < 100:
        visualProf=- 3
    elif vAndpArts > 100 and vAndpArts < 500:
        visualProf= "No Change"
    elif vAndpArts > 500 and vAndpArts < 1000:
        visualProf=+ 2
    elif vAndpArts >1000 and vAndpArts < 1500:
        visualProf=+ 4
    elif vAndpArts >1500 and vAndpArts < 2000:
        visualProf=+ 6
    else:
        visualProf=+ 10

    #I had some bad phrasing here but it is supposed to imply if positive extra staffing and if negative less staffing
    print("After compiling the results here is the determined changes to our staffing: ")
    print("Natural Science will have: " + str(natSciProf) + " professors")
    print("Mathmatics will have: " + str(mathProf) + " professors")
    print("Foreign Language will have: " + str(foreignLangProf) + " professors")
    print("English will have: " + str(englishProf) + " professors")
    print("Humanity will have: " + str(humanityProf) + " professors")
    print("Social Science will have: " + str(socialSciProf) + " professors")
    print("Visual and Performance Arts will have: " + str(visualProf) + " professors")
main()