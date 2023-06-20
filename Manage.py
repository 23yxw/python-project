# Class of camp and emergency plan


class EmergencyPlan:
    """Class of emergency plan"""
    def __init__(self, id, emergencyType, area, startDate, endDate, camps):
        """Initialise the emergency plan"""
        self.id = id
        self.emergencyType = emergencyType
        self.area = area
        self.startDate = startDate
        self.endDate = endDate
        self.camps = camps
        self.volunteerNumber = self.getVolunteerNumber()
        self.campNumber = len(self.camps)
        self.status = "Active"
    
    def getVolunteerNumber(self):
        num = 0
        for c in self.camps:
            num += c.volunteerNumber
        return num

    def __str__(self):
        volunteerList = ""
        for camp in self.camps:
            for volunteer in camp.volunteers:
                volunteerList += str(volunteer.id) + ", "

        campList = ""
        for camp in self.camps:
            campList += str(camp.id) + ", "

        return "PLan " + str(self.id) +\
            "\nEmergency type is " + self.emergencyType +\
            "\nArea is " + self.area +\
            "\nStart date is " + str(self.startDate) +\
            "\nEnd date is " + str(self.endDate) +\
            "\nVolunteer: " + volunteerList +\
            "\nCamp: " + campList


class Camp:
    """Class of refugee profile"""
    def __init__(self, id, volunteers, location):
        """Initialise the camp"""
        self.id = id
        self.volunteers = volunteers
        self.refugees = {}
        self.location = location
        self.refugeeNumber = len(self.refugees)
        self.volunteerNumber = len(self.volunteers)
        self.planID = "Not Assigned to Plan"

    def createRefugeeProfile(self, refugeeID, name, number, medicalCondition):
        """Create profile of refugee"""
        self.refugees[refugeeID] = [refugeeID, name, number, medicalCondition]
    
    def addVolunteer(self, volunteer):
        self.volunteers.append(volunteer)
        self.volunteerNumber += 1

    def deleteVolunteer(self, volunteer):
        self.volunteers.remove(volunteer)
        self.volunteerNumber -= 1

    def __str__(self):
        volunteerList = ""
        for volunteer in self.volunteers:
            volunteerList += str(volunteer.id) + ", "

        outStr = ""
        for refugeeID in self.refugees:
            refugeeInfo = "\nRefugee name is " + str(self.refugees[refugeeID][1]) + \
                "\nNumber of refugee is " + str(self.refugees[refugeeID][2]) + \
                "\nMedical condition: " + str(self.refugees[refugeeID][3])

            outStr += refugeeInfo

        return "Camp " + str(self.id) + \
            outStr + \
            "\nVolunteer: " + volunteerList
