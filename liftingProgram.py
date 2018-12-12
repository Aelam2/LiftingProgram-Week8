
#This is complete
#Possbile clean up code with Array of weights to choose from
#Finds which plates should be added to the bar
from datetime import datetime
import os
import re
from queue import Queue


def optimalPlates(desiredWeight, weightsOnBar):
    if desiredWeight == 0: #Base case
        return weightsOnBar
    elif (desiredWeight % 5) != 0 and desiredWeight < 45: #Desired weight must be % 5 or there will be balance issues
        clearScreen()
        print('Weight must be an increment of 5 and greater than 45 Lbs')
        input("Enter to calculate new weight")
        calculateWeight()
        return False
    elif ((desiredWeight >= 90)): #We should always add a 45 to the bar until we get to smaller increments
        newWeight = desiredWeight - 90 #Adding a 45 means that 45 lbs is added to both SIDES which means 90 lb total
        weightsOnBar.append('45')
        return optimalPlates(newWeight, weightsOnBar)
    elif ( 90 > desiredWeight >= 50):
        newWeight = desiredWeight - 50
        weightsOnBar.append('25')
        return optimalPlates(newWeight, weightsOnBar)
    elif (50 > desiredWeight >= 20):
        newWeight = desiredWeight - 20
        weightsOnBar.append('10')
        return optimalPlates(newWeight, weightsOnBar)
    elif (20 > desiredWeight >= 10):
        newWeight = desiredWeight - 10
        weightsOnBar.append('5')
        return optimalPlates(newWeight, weightsOnBar)
    elif (10 > desiredWeight >= 5):
        newWeight = desiredWeight - 5
        weightsOnBar.append('2.5')
        return optimalPlates(newWeight, weightsOnBar)

#This is complete
#Mainly cleans up the array from the optimal weight method
#Counts how many times a plate is used and displays the data differently
def calculateWeight():
    clearScreen()
    # Subtract 45 from desired weight because the actual bar weighs 45 lb
    weightsOnBar = optimalPlates(int(input('Enter Desired Weight: ')) - 45, [])

    if weightsOnBar != False: #Only runs if weight was an increment of 5
        formatBarWeight(weightsOnBar)

def formatBarWeight(weightsOnBar):
    fortyFives = weightsOnBar.count("45")  # Counts occurences of each weight
    twentyFives = weightsOnBar.count("25")
    tens = weightsOnBar.count("10")
    fives = weightsOnBar.count("5")
    twoPointFives = weightsOnBar.count("2.5")

    if fortyFives >= 1:  # Makes everything look nice and pretty (3 x 45 lb, 2 x 10 lb) instead of 45 45 45 10 10
        print(fortyFives, "x 45")
    if twentyFives >= 1:
        print(twentyFives, "x 25")
    if tens >= 1:
        print(tens, "x 10")
    if fives >= 1:
        print(fives, "x 5")
    if twoPointFives >= 1:
        print(twoPointFives, "x 2.5")
    input("Enter to Continue")

def newWorkout():

    #Instructions
    clearScreen()
    print("Enter the name of the exercise and reps per set")
    print("You can enter as many exercises as you want")
    print("This routine will be available when you start a workout(3)")
    print("Type 'save' after you have entered your entire routine")
    print("")

    workoutTitle = input("Workout Title: ")
    #Dones't allow blank input or spaces only
    while True:
        if (workoutTitle.replace(" ","") == ""):
            print("Title can't be blank")
            workoutTitle = input("Workout Title: ")
        else:
            break

    #If a workfile exists then we need to check that there is not already
    #the same workout title to prevent duplicate names
    if os.path.isfile("workouts.txt"):
        titleExists = True
        while titleExists == True:
            workoutObject = open("workouts.txt", "r")
            if workoutTitle in workoutObject.read():
                print("This Title Already Exists, Enter a New Name.")
                workoutTitle = input("Workout Title: ")
                titleExists = True
            elif workoutTitle not in workoutObject.read():
                titleExists = False
        workoutObject.close()

    #If the file already exists and we found a non duplicate name
    #We reopen in append mode to add the workout and exercises
    #If the workout file never existed then this will create a brand new file
    #and we can ignore the duplicate check
    workoutObject = open("workouts.txt", "a")
    workoutObject.write("\nWorkout Title:" + workoutTitle)

    programStatus = True
    while programStatus == True:
        currentExercise = input("Enter new Exercise or Reps:")
        if currentExercise.lower() == "save":
            workoutObject.write("\nend")
            workoutObject.close()
            return
        elif currentExercise.replace(" ","").isalpha() == True:
            workoutObject.write("\n"+currentExercise+":")
        elif currentExercise.isnumeric() == True:
            workoutObject.write(" " + currentExercise)
        else:
            print("Exercises must be Letters only or Reps must be numbers only")

def clearScreen():
    for n in range(15):
        print('')

def generateWorkoutQueues():

    if os.path.isfile("workouts.txt") == True:
        allWorkoutsFile = open("workouts.txt", "r")
        read = allWorkoutsFile.readlines()

        allWorkouts = {}
        readWorkout = False

        for lines in read:
            if ("Workout Title:" in lines) == True:
                currentWorkout = lines.replace('\n', "").replace(' ', "").split(':', 1)[1]
                allWorkouts[currentWorkout] = {}
                readWorkout = True
                continue
            elif ("end" in lines) == True:
                readWorkout = False
            if readWorkout == True:
                # exercises.append(lines.replace("\n",""))
                exerciseQueue = Queue()
                exerciseQueue1 = []
                cleanLine = re.sub('[:\n]', "", lines).split(" ")
                for words in cleanLine:
                    if words.isalpha() == True:
                        exercise = words
                    if words.isnumeric() == True:
                        exerciseQueue.put(words)
                    if (words == cleanLine[-1]):
                        allWorkouts[currentWorkout][exercise] = exerciseQueue


        allWorkoutsFile.close()
        return allWorkouts
    else:
        return False

def recordDay(workoutSelection, workoutDate, workoutname):
    clearScreen()
    q = Queue()
    print(workoutSelection)
    workoutHistory = open("workoutHistory.txt", "a")
    workoutHistory.write(workoutDate+","+workoutname)
    for exercises in workoutSelection:
        print("Current Exercise: " + exercises)
        workoutHistory.write(","+exercises)
        exerciseReps = workoutSelection[exercises]
        for repNum in range(exerciseReps.qsize()):
            currentRep = exerciseReps.get()
            print("Set #" + str(repNum + 1) + ": " + currentRep + " reps")
            currentWeight = int(input("Enter Weight: "))
            if currentWeight > 45:
                weightsOnBar = optimalPlates(currentWeight - 45, [])
                formatBarWeight(weightsOnBar)
            else:
                currentWeight = str((round(currentWeight) / 2))
                print("Use "+ currentWeight + " lb dumbbells")
                input("Enter to Continue")
            workoutHistory.write(","+str(currentRep)+"x"+str(currentWeight))


def startWorkout(workoutDictionary):
    clearScreen()

    if workoutDictionary != False:
        while True:
            workoutDate = input("Enter workout date: (MM/DD/YYYY)")
            try:
                if workoutDate != datetime.strptime(workoutDate, "%m/%d/%Y").strftime("%m/%d/%Y"):
                    raise ValueError
                break
            except ValueError:
                print("Invalid Format. Ex. '04/11/1997' or '11/05/2018'")
                continue

        for workouts in workoutDictionary:
            print(workouts)
        while True:
            workoutSelection = input("Enter Workout Name to Start:")
            if workoutSelection in workoutDictionary:
                recordDay(workoutDictionary[workoutSelection], workoutDate, workoutSelection)
                break
            else:
                print("Invalid workout selection. ")
                continue

        input("")
    else:
        input("There are no workouts created.\nEnter to continue.")
        return


def viewWorkout():
    if os.path.isfile("workoutHistory.txt") == True:
        while True:
            workoutHistory = open("workoutHistory.txt", "r")

            print("1)Enter Specific Date\n2)Display all workouts in a month\n"
                  "3)Display full list of workout dates\n4)Exit History\n")
            userChose = input("Enter Option:")
            if userChose == "1":
                pass
            if userChose == "2":
                userMonth = input("Enter Month by number (01 = Jan, 02 = Feb, Ect.)")
                for lines in workoutHistory:
                    workouts = lines.split(",")
                    if userMonth in workouts[0][:2]:
                        print(workouts[0])
            if userChose == "3":
                for lines in workoutHistory:
                    workouts = lines.split(",")
                    print(workouts[0])
            if userChose == "4":
                break
    else:
        input("There are currently no workouts in history.")

def maxLifts():
    pass


def main():
    workoutDictionary = generateWorkoutQueues()
    print(workoutDictionary)
    programChoice = ""
    while programChoice != 6:
        clearScreen()
        print("James Elam Fitness Program")
        print("1 : Calculate optimal plates for a weight")
        print("2 : Create a new workout")
        print("3 : Start a workout")
        print("4 : View a specific workout by date (MM/DD/YYYY)")
        print("5 : View your max lifts")
        print("6 : Exit Program")

        programChoice = input("Enter Option: ")

        if programChoice == '1':
            calculateWeight()
        if programChoice == '2':
            newWorkout()
            workoutDictionary = generateWorkoutQueues()
        if programChoice == '3':
            startWorkout(workoutDictionary)
        if programChoice == '4':
            viewWorkout()
        if programChoice == '5':
            maxLifts()
        if programChoice == '6':
            exit()

main()