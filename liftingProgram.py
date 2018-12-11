
#This is complete
#Possbile clean up code with Array of weights to choose from
#Finds which plates should be added to the bar
from pythonds import Queue


def optimalPlates(desiredWeight, weightsOnBar):
    if desiredWeight == 0: #Base case
        return weightsOnBar
    elif (desiredWeight % 5) != 0: #Desired weight must be % 5 or there will be balance issues
        clearScreen()
        print('Weight must be an increment of 5')
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
        fortyFives = weightsOnBar.count("45") #Counts occurences of each weight
        twentyFives = weightsOnBar.count("25")
        tens = weightsOnBar.count("10")
        fives = weightsOnBar.count("5")
        twoPointFives = weightsOnBar.count("2.5")

        if fortyFives >= 1: # Makes everything look nice and pretty (3 x 45 lb, 2 x 10 lb) instead of 45 45 45 10 10
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
    print("Enter the name of the exercise, total sets, and reps per set")
    print("You can enter as many exercises as you want")
    print("This routine will be available when you start a workout(3)")
    print("Type 'save' after you have entered your entire routine")
    print("")
    workoutTitle = input("Workout Title: ")

    programStatus = True

    #if workouts.txt doesn't exist
        #create workouts.txt

    workoutObject = open("workouts.txt", "a")
    workoutObject.write("\nWorkout Title:" + workoutTitle)

    while programStatus == True:
        currentExercise = input("Enter new Exercise or Reps:")
        if currentExercise.lower() == "save":
            workoutObject.write("\nend")
            workoutObject.close()
            return
        if currentExercise.replace(" ", "").isalpha() == True:
            workoutObject.write("\n"+currentExercise+":")
        if currentExercise.isnumeric() == True:
            workoutObject.write(" " + currentExercise)

def clearScreen():
    for n in range(15):
        print('')

def createWorkoutDictionary():
    allWorkoutsFile = open("workouts.txt", "r")
    read = allWorkoutsFile.readlines()

    allWorkouts = {}
    readWorkout = False
    exercises = []

    for lines in read:
        if ("Workout Title:" in lines) == True:
            currentWorkout = lines.replace('\n', "").replace(' ', "").split(':', 1)[1]
            readWorkout = True
            continue
        elif ("end" in lines) == True:
            allWorkouts[currentWorkout] = exercises
            exercises = []
            readWorkout = False
        if readWorkout == True:
            exercises.append(lines.replace("\n",""))

    allWorkoutsFile.close()
    return allWorkouts

def workoutQueue(workoutSelection):
    clearScreen()
    q = Queue()

    print("Workout Overview")
    for exercises in workoutSelection:
        print(exercises)



def startWorkout():
    clearScreen()
    allWorkouts = createWorkoutDictionary()
    print(allWorkouts)

    for workouts in allWorkouts:
        print(workouts)

    workoutSelection = input("Enter Workout Name to Start:")

    if workoutSelection in allWorkouts:
        workoutQueue(allWorkouts[workoutSelection])
    else:
        print("Invalid workout selection. ")
        startWorkout()

    input("")


def viewWorkout():
    pass

def maxLifts():
    pass



def main():
    allWorkouts = []
    programChoice = ""
    while programChoice != 6:
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
            allWorkouts.append(newWorkout())
        if programChoice == '3':
            startWorkout()
        if programChoice == '4':
            viewWorkout()
        if programChoice == '5':
            maxLifts()
        if programChoice == '6':
            exit()

main()