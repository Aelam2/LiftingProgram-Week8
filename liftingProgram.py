
class Workout:
    def __init__(self, workoutTitle):
        self.workoutTitle = workoutTitle

    def getWorkoutTitle(self):
        return self.workoutTitle

#This is complete
#Possbile clean up code with Array of weights to choose from
#Finds which plates should be added to the bar
def optimalPlates(desiredWeight, weightsOnBar):
    if desiredWeight == 0: #Base case
        return weightsOnBar
    elif (desiredWeight % 5) != 0: #Desired weight must be % 5 or there will be balance issues
        print('Weight must be an increment of 5')
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
    for n in range(10):
        print('')

    #Instructions
    print("Enter the name of the exercise, total sets, and reps per set")
    print("You can enter as many exercises as you want")
    print("This routine will be available when you start a workout(3)")
    print("Type 'save' after you have entered your entire routine")
    print("")

    workoutTitle = input("Workout Title: ")
    Workout(workoutTitle)

    programStatus = True
    numOfExercises = 1

    while programStatus == True:
        exercise = input("Exercise " + str(numOfExercises) + ": ")
        if exercise.lower() == "save":
            return workoutTitle
        numOfSets = int(input("total sets: "))

        for n in range(numOfSets):
            reps = input("Set " + str(n + 1) + " reps: ")

        numOfExercises += 1

def startWorkout(allWorkouts):
    print("Select a Workout: ")
    for workouts in allWorkouts:
        print(workouts)
    selectedWorkout = input("Enter Option: ")
    print()


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
            startWorkout(allWorkouts)
        if programChoice == '4':
            viewWorkout()
        if programChoice == '5':
            maxLifts()
        if programChoice == '6':
            exit()

main()