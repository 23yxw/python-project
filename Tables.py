from tabulate import tabulate


def viewAllPlans(data):
    plans = data[3]
    table = []
    if not plans:
        print(
            "\n=====================================================\n"
            "\nTHERE ARE CURRENTLY NO EMERGENCY PLANS\n")
        input("Press any key to continue: ")
    else:
        for plan in plans:
            table.append([
                plan.id,
                plan.emergencyType,
                plan.area,
                plan.startDate,
                plan.endDate,
                plan.volunteerNumber,
                plan.campNumber,
                plan.status
            ])

        print(tabulate(table,
                       headers=[
                           "Plan ID",
                           "EmergencyType",
                           "Location",
                           "Start Date",
                           "End Date",
                           "# Volunteers",
                           "# Camps",
                           'Status'
                       ],
                       tablefmt="grid"))
        input("Press any key to continue: ")

    return data


def viewAllVolunteers(data):
    viewAllVolunteer(data[1][1:])
    input("Press any key to continue: ")
    return data


def viewAllVolunteer(volunteers):
    table = []
    if not volunteers:
        print(
            "\n=====================================================\n"
            "\nTHERE ARE CURRENTLY NO VOLUNTEERS\n")

    else:
        for volunteer in volunteers:
            table.append([
                volunteer.id,
                volunteer.firstName,
                volunteer.lastName,
                volunteer.role,
                volunteer.campID,
                volunteer.region,
                volunteer.email,
                volunteer.phoneNumber,
                volunteer.address,
                volunteer.activation,
                volunteer.availability
            ])

        print(tabulate(table,
                       headers=[
                           "User ID",
                           "First Name",
                           "Last Name",
                           "Role",
                           "Camp",
                           "Region",
                           "Email",
                           "Phone",
                           "Address",
                           "Activation",
                           "Available"
                       ],
                       tablefmt="grid"))

    return


def viewAllCamps(data):
    viewAllCamp(data[2])
    input("Press any key to continue: ")
    return data


def viewAllCamp(camps):
    table = []
    if not camps:
        print(
            "\n=====================================================\n"
            "\nTHERE IS CURRENTLY NO CAMPS\n")

    else:
        for camp in camps:
            volunteerIDList = []
            for volunteer in camp.volunteers:
                volunteerIDList.append(volunteer.id)

            table.append([
                camp.id,
                camp.location,
                camp.refugeeNumber,
                volunteerIDList,
                camp.planID
            ])

        print(tabulate(table,
                       headers=[
                           "Camp ID",
                           "Location",
                           "Number of Refugees",
                           "Volunteers ID List",
                           "Emergency Plan ID"
                       ],
                       tablefmt="grid"))

    return

def viewCamps(data):
    campList = data[1]

    viewCamp(campList)
    input("Press any key to continue: ")
    return data


def viewCamp(campList):
    """displays all refugee data in camp"""
    
    if not campList:
        print(
            "\n=====================================================\n"
            "\nTHERE ARE CURRENTLY NO CAMPS\n")
    else:
        for camp in campList:
            if not camp.refugees:
                print(
                    "\n=====================================================\n"
                    "\nTHERE ARE CURRENTLY NO REFUGEES\n")
            else:
                table = []
                print("Camp ", camp.id)
                for refugeeID in camp.refugees:
                    table.append([
                        camp.refugees[refugeeID][0],
                        camp.refugees[refugeeID][1],
                        camp.refugees[refugeeID][2],
                        camp.refugees[refugeeID][3]
                    ])

                print(tabulate(table,
                               headers=[
                                   "Refugee ID",
                                   "Refugee Name",
                                   "Number of people in family",
                                   "Medical Conditions"
                               ],
                               tablefmt="grid"))

    # input("Press any key to continue: ")

    return 


def viewPlan(data):
    """displays all camps in a plan"""
    planList = data[3]
    if not planList:
        print(
            "\n=====================================================\n"
            "\nTHERE IS CURRENTLY NO PLANS\n")
    else:
        for plan in planList:
            if not plan.camps:
                print(
                    "\n=====================================================\n"
                    "\nTHERE IS CURRENTLY NO CAMPS\n")
            else:
                table = []
                print("Plan ", plan.id)
                for camp in plan.camps:
                    volunteerIDList = []
                    for volunteer in camp.volunteers:
                        volunteerIDList.append(volunteer.id)

                    table.append([
                        camp.id,
                        camp.location,
                        camp.refugeeNumber,
        
                        volunteerIDList
                        
                    ])

                print(tabulate(table,
                               headers=[
                                   "Camp ID",
                                   "Camp Location",
                                   "Refugee Number in Camp",
                                   "Volunteers ID List"
                               ],
                               tablefmt="grid"))

    input("Press any key to continue: ")

    return data
