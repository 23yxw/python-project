import pickle


def loadVolunteerData():
    try:
        volunteerFile = open("volunteers.txt", "rb")
        userList = pickle.load(volunteerFile)
        volunteerFile.close()

        return userList
    except Exception as e:
        print(e)

        return []


def loadCampData():
    try:
        campFile = open("camps.txt", "rb")
        campList = pickle.load(campFile)
        campFile.close()

        return campList
    except Exception as e:
        print(e)

        return []


def loadPlanData():
    try:
        planFile = open("plans.txt", "rb")
        planList = pickle.load(planFile)
        planFile.close()

        return planList
    except Exception as e:
        print(e)

        return []


def exit(inObj):
    """Save data into file and exit the program"""
    userList = inObj[1]
    campList = inObj[2]
    planList = inObj[3]
    try:
        volunteerFile = open("volunteers.txt", "wb")
        campFile = open("camps.txt", "wb")
        planFile = open("plans.txt", "wb")
        pickle.dump(userList, volunteerFile)
        pickle.dump(campList, campFile)
        pickle.dump(planList, planFile)
        volunteerFile.close()
        campFile.close()
        planFile.close()
    except Exception as e:
        print(e)

    return [None, None, None, None]


def welcome():
    """print welcome message"""
    print("=====================================================\n")
    print("Welcome to the Humanitarian Disaster Relief System!\n")
    print("=====================================================\n")
    print("\033[93m {}\033[00m" .format("IMPORTANT NOTICE: Please exit the program by selecting\n the exit button to save your changes!"))
    
