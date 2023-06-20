import Users as u
import MainUtilities as mu
import UserUtilities as uut
import ManageUtilities as mut
import Tables as tb

global is_login


# default admin account
def createAdmin():
    a = u.Admin("admin", "firstName", "lastName", "111", "root@ucl.ac.uk", 123456, "address")

    return a


# testing accounts
def createVolunteer():
    v1 = u.Volunteer(1, "volunteer1", "111", "first1", "last1", "volunteer1@163.com", 123456, "address", "Test")
    v2 = u.Volunteer(2, "volunteer2", "111", "first2", "last2", "volunteer2@163.com", 123456, "address", "Test")
    v3 = u.Volunteer(3, "volunteer3", "111", "first3", "last3", "volunteer3@163.com", 123456, "address", "Test")
    v4 = u.Volunteer(4, "volunteer4", "111", "first4", "last4", "volunteer4@163.com", 123456, "address", "Test")
    v5 = u.Volunteer(5, "volunteer5", "111", "first5", "last5", "volunteer5@163.com", 123456, "address", "Test")

    return [v1, v2, v3, v4, v5]


def default():
    print("Invalid input. Try again!")

    return


def main():
    global is_login
    user = None
    campList = mu.loadCampData()
    planList = mu.loadPlanData()
    if not mu.loadVolunteerData():
        userList = [createAdmin()] + createVolunteer()
    else:
        userList = mu.loadVolunteerData()

    case = ""

    mu.welcome()
    while case != "E" and case != "e":
        case = input(
            "\n=====================================================\n"
            "                      MAIN MENU\n"
            "[1] Login and Registration\n"
            "[E] Exit!\n"
            "\nPlease select your purpose: "
        )
        if case != "1" and case not in ("E", "e"):
            default()
            continue
        switch = {
            "1": uut.login,
            "e": mu.exit,
            "E": mu.exit
        }

        inObj = [user, userList, campList, planList]

        outObj = switch.get(case)(inObj)
        user = outObj[0]
        userList = outObj[1]
        if len(outObj) == 4:
            campList = outObj[2]
            planList = outObj[3]

        try:
            is_login = uut.is_login
        except AttributeError:
            is_login = False

        if is_login:
            if user.username == userList[0].username:
                while case != "E" and case != "e":
                    case = input(
                        "\n=====================================================\n"
                        "                      ADMIN MENU\n\n"
                        "[1] Edit personal information\n"
                        "[2] Manage volunteer account\n"
                        "[3] View all volunteers\n"
                        "[4] Create emergency plan\n"
                        "[5] Edit emergency plan\n"
                        "[6] View emergency plan summaries\n"
                        "[7] View camps in plans\n"
                        "[8] Create new camp\n"
                        "[9] Delete camps\n"
                        "[10] View all camps\n"
                        "[E] Logout!\n"
                        "\nPlease select your purpose: "
                    )

                    if case not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "e", "E"):
                        default()
                        continue
                    switch = {
                        "1": mut.editInformation,
                        "2": mut.manageVolunteerAccount,
                        "3": tb.viewAllVolunteers,
                        "4": mut.createEmergencyPlan,
                        "5": mut.editEmergencyPlans,
                        "6": tb.viewAllPlans,
                        "7": tb.viewPlan,
                        "8": mut.createCamp,
                        "9": mut.removeCamp,
                        "10": tb.viewAllCamps,
                        "e": uut.logout,
                        "E": uut.logout
                    }
                    inObj = [user, userList, campList, planList]
                    outObj = switch.get(case)(inObj)
                    user = outObj[0]
                    userList = outObj[1]
                    if len(outObj) == 4:
                        campList = outObj[2]
                        planList = outObj[3]

                case = ""

            else:
                while case != "E" and case != "e":
                    case = input(
                        "\n=====================================================\n"
                        "                  VOLUNTEER MENU\n"
                        "[1] Display my information\n"
                        "[2] Edit personal information\n"
                        "[3] Change region\n"
                        "[4] Change role\n"
                        "[5] Change camp  {Current camp: " + str(user.campID) + "}\n"
                        "[6] Create refugee profile\n"
                        "[7] View all refugees\n"
                        "[8] Delete refugees from camps\n"
                        "[E] Logout!\n"
                        "\nPlease select your purpose: "
                    )
                    if case not in ("1", "2", "3", "4", "5", "6", "7", "8", "e", "E"):
                        default()
                        continue
                    switch = {
                        "1": mut.displayInfo,
                        "2": mut.editInformation,
                        "3": mut.changeRegion,
                        "4": mut.changeRole,
                        "5": mut.changeCamp,
                        "6": mut.createRefugeeProfile,
                        "7": tb.viewCamps,
                        '8': mut.deleteRefugeesFromCamps,
                        "e": uut.logout,
                        "E": uut.logout
                    }

                    inObj = [user, campList]
                    outObj = switch.get(case, default)(inObj)
                    user = outObj[0]
                    campList = outObj[1]

                case = ""


if __name__ == "__main__":
    main()
