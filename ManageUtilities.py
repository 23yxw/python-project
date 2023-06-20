# Utilities for manage the user account and emergency plan
import re
from datetime import date
from UserUtilities import get_nonempty_input, pwd_check
import Tables as tb


def getValidInput(title, options, next=False):
    while True:
        print("\n=====================================================")
        print(title)
        for i in range(len(options)):
            print("[{n}] ".format(n=i + 1) + options[i])
        if not next:
            print("[E] Cancel\n")
        else:
            print("[E] Next\n")
        ans = input("Select a valid option: ")
        if ans.upper() == "E":
            return "E"
        elif ans.isdigit() and 0 < int(ans) <= len(options):
            return int(ans)
        else:
            print("\033[91m {}\033[00m".format("\nInvalid Option, try again!\n"))


def editInformation(inObj):
    """Edit user Information"""

    def edit_menu():
        """print edit menu"""
        print("\n=====================================================")
        print("                EDIT INFORMATION")
        print("Please select what you want to edit: ")
        print("[1] Edit your username")
        print("[2] Edit your fullname")
        print("[3] Edit your password")
        print("[4] Edit your email")
        print("[5] Edit your phone number")
        print("[6] Edit your address")
        print("[E] Cancel\n")

    def edit_name():
        name = get_nonempty_input('Name')
        user.editInformation(username=name)

        return user

    def edit_fullname():
        firstname = get_nonempty_input('Firstname')
        lastname = get_nonempty_input('Lastname')
        user.editInformation(fullname=[firstname, lastname])

        return user

    def edit_password():
        print("\033[93m {}\033[00m".format(
            'Your password should be 5-12 digits, containing:\n at least one uppercase letter;'
            '\n at least one lowercase letter;\n at least one number;'
            '\n no space letter;\n and at least one special letter.'))
        while True:
            password = input("Password: ")
            done, error = pwd_check(password)
            if done:
                break

        while True:
            confirm_password = input("Confirm your password: ")
            if password != confirm_password:
                print("\033[91m {}\033[00m".format("Your passwords do not match, try again!\n"))
            else:
                break
        user.editInformation(password=password)

        return user

    def edit_email():
        while True:
            email = get_nonempty_input("\nEnter a new Email")
            if re.search(r"([a-z]*\d*)@([a-z]*\d*)", email, re.I) is not None \
                    and " " not in email \
                    and "@" != email[len(email) - 1] and "@" != email[0]:
                break
            else:
                print("\033[91m {}\033[00m".format("Wrong format of email address."))
                break
        user.editInformation(email=email)

        return user

    def edit_phoneNumber():
        while True:
            phoneNumber = get_nonempty_input("\nEnter a new Phone number")
            try:
                phoneNumber = int(phoneNumber)
                break
            except ValueError:
                print("\033[91m {}\033[00m".format("Phone number should be integer."))
                break
        user.editInformation(phoneNumber=phoneNumber)

        return user

    def edit_address():
        address = get_nonempty_input("\nEnter a new Address")
        user.editInformation(address=address)

        return user

    while True:
        edit_menu()
        user = inObj[0]
        user_input = input("Enter a valid number: ")
        if user_input == "1":
            return [edit_name()] + inObj[1:]
        elif user_input == "2":
            return [edit_fullname()] + inObj[1:]
        elif user_input == "3":
            return [edit_password()] + inObj[1:]
        elif user_input == "4":
            return [edit_email()] + inObj[1:]
        elif user_input == "5":
            return [edit_phoneNumber()] + inObj[1:]
        elif user_input == "6":
            return [edit_address()] + inObj[1:]
        elif user_input == "E" or user_input == "e":
            return [user] + inObj[1:]
        else:
            print("=====================================================")
            print("\nInvalid input, please try again\n")
            print("=====================================================")


def manageVolunteerAccount(inObj):
    """Manage volunteer account"""
    user = inObj[0]
    userList = inObj[1]
    campList = inObj[2]
    idList = []
    for u in userList[1:]:
        idList.append(u.id)

    while True:
        tb.viewAllVolunteer(userList[1:])
        print("\n=====================================================")
        print("              CHOOSE ACCOUNT ID\n")

        accountID = get_nonempty_input("Enter Account ID or Press E to cancel")
        if accountID.isdigit() and int(accountID) in idList:
            break
        elif accountID == "E" or accountID == "e":
            return inObj
        else:
            print("\033[91m {}\033[00m".format("Invalid input."))

    while True:
        for volunteer in userList[1:]:
            if volunteer.id == int(accountID):
                status = volunteer.activation
                break
        print("\n=====================================================")
        if status:
            print("\033[93m {}\033[00m".format("ACCOUNT MANAGEMENT - CURRENT STATUS: ACTIVATED"))
            print("[1] Deactivate account")
        else:
            print("\033[93m {}\033[00m".format("ACCOUNT MANAGEMENT - CURRENT STATUS: DEACTIVATED"))
            print("[1] Activate account")

        print("[2] Delete account")
        print("[E] Cancel\n")

        user_input = input("Choose a valid option: ")
        if user_input == "1" and status is True:
            user.manageAccount(volunteer, 'deactivate')
            return [user, userList, campList, inObj[3]]
        elif user_input == "1" and status is False:
            user.manageAccount(volunteer, 'activate')
            return [user, userList, inObj[2], inObj[3]]
        elif user_input == "2":
            userList.remove(volunteer)
            return [user, userList, campList, inObj[3]]
        elif user_input.upper() == "E":
            return inObj
        else:
            print("\033[91m {}\033[00m".format("INVALID INPUT! TRY AGAIN"))


def changeRole(inObj):
    """Change Role"""
    print("\n=====================================================")
    user = inObj[0]
    print(
        "Select the role that you want to change to: \n"
        "[1] Medical help\n"
        "[2] Hygiene and cleanliness\n"
        "[3] Information Entry\n"
        "[4] Mental health help\n"
        "[5] Order Maintenance\n"
        "[E] Return to former page\n"
    )

    numbers = {
        '1': "Medical help",
        '2': "Hygiene and cleanliness",
        '3': "Information Entry",
        '4': "Mental health help",
        '5': 'Order Maintenance'
    }

    while True:
        num = input("Please select your purpose: ")
        if num in ('1', '2', '3', '4', '5'):
            print(
                "\033[92m {}\033[00m".format('Your have successfully chosen the following responsibility: ') + numbers[
                    num])
            user.changeRole(numbers[num])
            break
        elif num in ('E', 'e'):
            print('')
            break
        else:
            print("\033[91m {}\033[00m".format('Input error, please reselect!'))

    return [user, inObj[1]]


def changeRegion(inObj):
    """Change working region"""
    print("\n=====================================================")
    user = inObj[0]
    numbers = {
        '1': 'West',
        '2': 'East',
        '3': 'South',
        '4': 'North',
        '5': 'All'
    }

    if not user.availability:
        print("\033[93m {}\033[00m".format(
            '\nYour currently status is: unavailable, change your region to set availability to available!'))

        while True:
            num = input(
                'Please select the region you want to work in:\n'
                "[1] West\n"
                "[2] East\n"
                "[3] South\n"
                "[4] North\n"
                "[5] ALL\n"
                "[E] Return to former page\n"
            )

            if num in ('1', '2', '3', '4', '5'):
                print("\033[92m {}\033[00m".format('\nYou are now enrolled in the region: ') + numbers[num])
                user.changeAvailability()
                user.changeRegion(numbers[num])
                break
            elif num in ('E', 'e'):
                print('')
                break
            else:
                print("\033[91m {}\033[00m".format('Input error, please reselect!'))

    else:
        print("\033[93m {}\033[00m".format(
            '\nYour currently status is: available, and you are now enrolled in Region: ') + user.region)
        print('\nYou can change your status or region:\n'
              '\n[1] : Status\n'
              '[2] : Region\n'
              '[E] : Cancel\n'
              )

        while True:
            swi = input("Please select your purpose: ")
            if swi == '1':
                user.changeAvailability()
                user.changeRegion(region=None)
                print("\033[92m {}\033[00m".format('\nYour status is changed to unavailable!'))
                return [user, inObj[1]]
            elif swi == '2':
                while True:
                    num = input(
                        'Please select the region you want to work in:\n'
                        "[1] West\n"
                        "[2] East\n"
                        "[3] South\n"
                        "[4] North\n"
                        "[5] ALL\n"
                        "[E] Return to former page\n"


                        "\nPlease select your purpose: "
                    )
                    if num in ('1', '2', '3', '4', '5'):
                        user.changeRegion(numbers[num])
                        print("\033[92m {}\033[00m".format('Your region is changed to %s!' % user.region))
                        return [user, inObj[1]]
                    elif num in ('E', 'e'):
                        print('')
                        return [user, inObj[1]]
                    else:
                        print("\033[91m {}\033[00m".format('Input error, please reselect!'))
            elif swi in ('E', 'e'):
                print('Status kept!')
                return [user, inObj[1]]
            else:
                print("\033[91m {}\033[00m".format('Input error, please reselect!'))

    return [user, inObj[1]]


def changeCamp(inObj):
    user = inObj[0]
    campList = inObj[1]

    while True:
        tb.viewAllCamp(campList)
        availableCampIDs = []
        for camp in campList:
            availableCampIDs.append(camp.id)
        inp = input(
            "\nEnter the camp ID that you want to change to (OR enter E to cancel): "
        )
        if inp.isdigit() and int(inp) in availableCampIDs:
            if user.campID == "No Camp Assigned":
                for camp in campList:
                    if camp.id == int(inp):
                        camp.volunteers.append(user)
            else:
                for camp in campList:
                    if camp.id == user.campID:
                        camp.volunteers.remove(user)
                    if camp.id == int(inp):
                        camp.volunteers.append(user)

            user.campID = int(inp)
            print("\n CAMP CHANGED TO " + inp)
            return [user, campList]
        elif inp.upper() == "E":
            return [user, campList]
        else:
            print("\033[91m {}\033[00m".format("\nINVALID INPUT!"))


def displayInfo(inObj):
    user = inObj[0]
    print(
        "\n====================================================="
        "\n                 USER INFO"
        "\n Username: " + user.username +
        "\n First Name: " + user.firstName +
        "\n Last Name: " + user.lastName +
        "\n Email: " + user.email +
        "\n Phone Number: " + str(user.phoneNumber) +
        "\n Address: " + user.address +
        "\n Role: " + user.role +
        "\n Camp: " + str(user.campID) +
        "\n Region: " + str(user.region) +
        "\n Availability: " + str(user.availability)
    )
    input("\nPress any key to continue: ")
    return [user, inObj[1]]


def createEmergencyPlan(inObj):
    """Create emergency plan"""
    user = inObj[0]
    campList = inObj[2]
    planList = inObj[3]
    if not planList:
        planID = 1
    else:
        planID = planList[-1].id + 1

    while True:
        num = input(
            "\n=====================================================\n"
            '                      REGIONS\n'
            "[1] West\n"
            "[2] East\n"
            "[3] South\n"
            "[4] North\n"
            "[E] Cancel\n"
            '\nSelect the region of the emergency plan: '
        )
        numbers = {
            '1': 'West',
            '2': 'East',
            '3': 'South',
            '4': 'North,'
        }
        if num == "1" or num == "2" or num == "3" or num == "4":
            area = numbers[num]
            break
        elif num == "e" or num == "E":
            return inObj
        else:
            print("\033[91m {}\033[00m".format("\nInvalid Input!\n"))

    [camps_in_plan, campList] = getCamp(campList, area, inObj, planID)
    if not camps_in_plan:
        return inObj

    while True:
        num = input(
            "\n=====================================================\n"
            '                    EMERGENCY TYPE\n'
            "[1] Earthquake\n"
            "[2] Flood\n"
            "[3] Landslide\n"
            "[4] Tsunami\n"
            "[5] Volcano eruption\n"
            "[6] Storm\n"
            "[E] Cancel\n"
            '\nSelect the type of the emergency plan: '
        )
        numbers = {
            '1': 'Earthquake',
            '2': 'Flood',
            '3': 'Landslide',
            '4': 'Tsunami',
            '5': 'Volcano eruption',
            '6': 'Storm'
        }

        if num == "1" or num == "2" or num == "3" or num == "4" or num == "5" or num == "6":
            emergencyType = numbers[num]
            break
        elif num == "e" or num == "E":
            return inObj
        else:
            print("\033[91m {}\033[00m".format("\nInvalid Input!\n"))

    startDate = getStartDate()
    endDate = getEndDate(startDate)

    plan = user.createPlan(planID, emergencyType, area, startDate, endDate, camps_in_plan)
    planList.append(plan)

    return [user, inObj[1], campList, planList]


def getStartDate():
    while True:
        startDate = input("Start Date (yyyy-mm-dd): ").split("-")
        try:
            startDate = date(int(startDate[0]), int(startDate[1]), int(startDate[2]))
            break
        except ValueError:
            print("\033[91m {}\033[00m".format("Date is in a wrong format."))

    return startDate


def getEndDate(startDate):
    while True:
        endDate = input("End Date (yyyy-mm-dd): ").split("-")
        try:
            endDate = date(int(endDate[0]), int(endDate[1]), int(endDate[2]))
        except ValueError:
            print("\033[91m {}\033[00m".format("Date is in a wrong format."))
            continue

        if endDate > startDate:
            break
        else:
            print("\033[91m {}\033[00m".format("End date should be greater than start date."))

    return endDate


def getCamp(campList, area, inObj, planID):
    availableCamps = {}
    for camp in campList:
        if camp.location == area and camp.planID == "Not Assigned to Plan":
            availableCamps[camp.id] = camp
    camps = []
    while True:
        if availableCamps:
            print("\n=====================================================\n")
            print("DISPLAYING CAMPS IN THE " + area + " region")
            tb.viewAllCamp(list(availableCamps.values()))

            choice = getValidInput("", ["Choose a camp", "Create a new camp"])
            if choice == 1:
                while True:
                    campID = input("Enter Camp ID: ")
                    if campID.isdigit() and int(campID) in availableCamps:
                        camp = availableCamps[int(campID)]
                        camps.append(camp)
                        availableCamps.pop(int(campID))
                        camp.planID = planID
                        print("\033[92m {}\033[00m".format("\nCAMP ") + campID + "\033[92m {}\033[00m".format(
                            " HAS BEEN ADDED TO THE EMERGENCY PLAN!"))
                        break
                    else:
                        print("\033[91m {}\033[00m".format("\n INCORRECT CAMP ID! TRY AGAIN"))
                        continue
            elif choice == 2:
                camp = createCamp(inObj, area=area)
                if camp:
                    camp.planID = planID
                    camps.append(camp)
                    campList.append(camp)
                    print("\033[92m {}\033[00m".format("\nCAMP HAS BEEN ADDED TO THE EMERGENCY PLAN!"))

            else:
                return [camps, campList]

        else:
            if camps:
                nextBool = True
            else:
                nextBool = False
            choice = getValidInput(
                "\033[91m {}\033[00m".format("\nNO AVAILABLE CAMPS LEFT, CREATE A NEW CAMP FIRST\n"),
                ["Create new Camp"],
                next=nextBool
            )
            if choice == 1:

                camp = createCamp(inObj, area=area)
                if camp:
                    camp.planID = planID
                    camps.append(camp)
                    campList.append(camp)
                    print("\033[92m {}\033[00m".format("\nCAMP HAS BEEN ADDED TO THE EMERGENCY PLAN!"))
            else:
                print("")
                return [camps, campList]


def createCamp(inObj, area=None):
    user = inObj[0]
    campList = inObj[2]
    userList = inObj[1]

    if not campList:
        campID = 1
    else:
        campID = campList[-1].id + 1

    state = 0
    if area is None:
        state = 1  # if accessed from admin menu directly
        inp = getValidInput("               SELECT AREA\n", ["West", "East", "South", "North"])
        areas = {'1': 'West',
                 '2': 'East',
                 '3': 'South',
                 '4': 'North',
                 'E': 'E'}
        area = areas[str(inp)]
        if area == "E":
            return inObj

    print("\nDISPLAYING AVAILABLE VOLUNTEERS IN THE " + area + " AREA\n")

    availableVolunteers = {}
    for vol in userList[1:]:
        if (vol.region == area or vol.region == "All") and vol.availability is True:
            availableVolunteers[vol.id] = vol
    volunteers = []
    while True:
        if availableVolunteers != {}:
            tb.viewAllVolunteer(list(availableVolunteers.values()))

            print("\nCHOOSE A VOLUNTEER TO WORK IN THE CAMP")
            userID = input("Enter Volunteer ID: ")
            if userID.isdigit() and int(userID) in availableVolunteers:
                volunteers.append(availableVolunteers[int(userID)])
                availableVolunteers[int(userID)].availability = False
                availableVolunteers.pop(int(userID))
                for vol in userList[1:]:
                    if vol.id == int(userID):
                        vol.campID = campID

                print("\033[92m {}\033[00m".format("\nVolunteer ") + userID + "\033[92m {}\033[00m".format(
                    " has been added to the camp!"))
            else:
                print("\033[91m {}\033[00m".format("Incorrect user ID!"))

            a = input(
                "\n=====================================================\n"
                "\n[1] Add another volunteer\n"
                "[ANY KEY] Cancel and return\n"
                "\nEnter a valid option: ")
            if a == "1":
                continue
            elif volunteers:
                break
            elif state == 0:
                return False
            else:
                return [inObj[0], inObj[1], campList, inObj[3]]

        else:
            print("\033[91m {}\033[00m".format("\nNO VOLUNTEERS AVAILABLE, RECRUIT MORE!\n"))
            if volunteers:
                break
            elif state == 0:
                return False
            else:
                return [inObj[0], inObj[1], campList, inObj[3]]

    camp = user.createCamp(campID, volunteers, area)
    print("\033[92m {}\033[00m".format("CAMP CREATED!"))

    if state == 0:
        return camp
    else:
        campList = inObj[2]
        campList.append(camp)
        return [inObj[0], inObj[1], campList, inObj[3]]


def deleteRefugeesFromCamps(inObj):
    """Delete refugees information from camps"""
    campList = inObj[1]
    tb.viewCamp(campList)
    print("\n=====================================================")
    if campList == []:
        return inObj

    while True:
        try:
            campID = int(input("\nChoose the id of the camp: "))
        except ValueError:
            print("\033[91m {}\033[00m".format("Camp id should be an integer."))
            continue

        exist = False
        for camp in campList:
            if campID == camp.id:
                exist = True
                break

        if not exist:
            print("\033[91m {}\033[00m".format("Camp does not exist! Try again"))
            continue
        else:
            break

    for camp in campList:
        if camp.id == campID:
            while True:
                try:
                    RefugeeID = int(input("\nSelect the id of the refugee: "))
                except ValueError:
                    print("\033[91m {}\033[00m".format("\nRefugee id should be an integer."))
                    continue
                if RefugeeID <= 0 or RefugeeID > len(camp.refugees):
                    print("\033[91m {}\033[00m".format("\nInvalid Refugee ID."))
                    continue
                else:
                    break
            del camp.refugees[RefugeeID]
            print("\033[92m {}\033[00m".format("\n Refugee has been deleted successfully!"))
    return [inObj[0], campList]


def createRefugeeProfile(inObj):
    """Create refugee profile"""
    user = inObj[0]
    campList = inObj[1]

    tb.viewAllCamp(campList)

    if campList == []:
        print("\n=====================================================\n"
              "\033[91m {}\033[00m".format("\nTHERE ARE CURRENTLY NO CAMPS\n"))
        return inObj

    while True:
        try:
            print("\n=====================================================\n")
            campID = int(input("Choose the id of the camp: "))
        except ValueError:
            print("\033[91m {}\033[00m".format("Camp id should be integer."))
            continue

        exist = False
        for camp in campList:
            if campID == camp.id:
                exist = True
                break

        if not exist:
            print("\033[91m {}\033[00m".format("Camp does not exist! Try again"))
            continue
        else:
            break

    if camp.refugees == {}:
        refugeeID = 1
    else:
        refugeeID = camp.refugees[list(camp.refugees.keys())[-1]][0] + 1

    refugee_name = get_nonempty_input("Name of refugee")

    while True:
        try:
            refugee_number = int(input("\nNumber of people in family: "))
        except ValueError:
            print("\033[91m {}\033[00m".format("\nRefugee id should be an integer."))
            continue
        break

        while True:
            try:
                refugee_number = int(input("\nNumber of people in family: "))
            except ValueError:
                print("\033[91m {}\033[00m".format("\nRefugee id should be an integer."))
                continue
            break

    print(
        "Select the medical conditions that you are under now: \n"
        "[1] Severe\n"
        "[2] Medium\n"
        "[3] Well\n"
    )

    while True:
        numbers = {
            '1': "Severe",
            '2': "Medium",
            '3': "Well"
        }
        medical_condition = get_nonempty_input("Select your medical condition: ")
        if medical_condition in ('1', '2', '3'):
            medical_condition = numbers[medical_condition]
            break
        else:
            print("\033[91m {}\033[00m".format('Input error, please reselect!'))

    user.createRefugeeProfile(camp, refugeeID, refugee_name, refugee_number, medical_condition)
    print("\033[92m {}\033[00m".format("\nRefugee has been successfully added!"))
    return [user, campList]


def removeCamp(data):
    tb.viewAllCamp(data[2])
    Camp_Remove = get_nonempty_input("Please type the ID of camp you want to remove")
    campList1 = data[2]
    for camp in campList1:
        if camp.id == int(Camp_Remove):
            campList1.remove(camp)
            data[1] = removeCampVolunteer(data[1], int(Camp_Remove))
            break

    return data


def removeCampVolunteer(user_list, campID):
    for volunteer in user_list:
        if hasattr(volunteer, "campID") and volunteer.campID == campID:
            volunteer.campID = "No Camp Assigned"
    return user_list


def handleCampMenu(data):
    input_choose = getValidInput('CAMP MENU', ['see camp details', 'delete camp'])
    if input_choose == 1:
        tb.viewAllCamps(data)
    elif input_choose == 2:
        removeCamp(data)
    return data


def editEmergencyPlans(inObj):
    """Edit Emergence Plans."""
    campList = inObj[2]
    planList = inObj[3]
    tb.viewAllPlans(inObj)
    while True:
        if not planList:
            break
        else:
            editPlan = input("Please input the emergency plan ID you want to edit (Or 'E' to cancel) : ")
            plan_id = []
            for plan in planList:
                plan_id.append(plan.id)
            if editPlan.isdigit() and int(editPlan) in plan_id:
                if planList[int(editPlan) - 1].status == "Inactive":
                    print("\nInactive Plan!\n")
                    continue

                while True:
                    plan = planList[int(editPlan) - 1]
                    camps = plan.camps
                    tb.viewAllCamp(campList)
                    num = input(
                        "\n=====================================================\n"
                        '                       Edit\n'
                        "[1] Add new camps\n"
                        "[2] Delete camps\n"
                        "[3] End plans\n"
                        "[E] Cancel\n"
                        '\nPlease Select What You Want to Edit: '
                    )
                    if num == '1':
                        newCamp = input("Please input the camp ID: ")
                        for camp in campList:
                            if camp.planID == "Not Assigned to Plan" and newCamp.isdigit() and int(newCamp) == camp.id:
                                camp.planID = plan.id
                                camps.append(camp)
                                plan.campNumber += 1
                                print("Add camp successfully.")
                                break
                        else:
                            print("\033[91m {}\033[00m".format("Invalid camp Id, please input another number"))
                            continue
                        break

                    if num == '2':
                        delCamp = input("Please input the camp ID: ")
                        for camp in camps:
                            if delCamp.isdigit() and int(delCamp) == camp.id:
                                camp.planID = "Not Assigned to Plan"
                                plan.campNumber -= 1
                                camps.remove(camp)
                                print("Delete camp successfully.")
                                break
                        else:
                            print("\033[91m {}\033[00m".format("Invalid camp Id, please input another number"))
                            continue
                        break

                    if num == '3':
                        actPlan = editPlan
                        for plan in planList:
                            if actPlan.isdigit() and int(actPlan) == plan.id:
                                plan.status = 'Inactive'
                                print("Inactivate plan successfully.")
                                break
                        else:
                            print("\033[91m {}\033[00m".format("Invalid plan Id, please input another number"))
                            continue
                        break

                    elif num == "e" or num == "E":
                        return inObj
                    else:
                        print("\033[91m {}\033[00m".format("\nInvalid Input!\n"))

            elif editPlan == "e" or editPlan == "E":
                return inObj

            else:
                print("\033[91m {}\033[00m".format("\nInvalid Input!\n"))
