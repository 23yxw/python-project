# Class of the user, including administrator and the volunteer
import Manage


class Admin:
    """Class of the administrator"""
    def __init__(self, username, firstName, lastName, password, email, phoneNumber, address):
        """Initialise the administrator"""
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address

    def editInformation(self, username=None, fullname=None, password=None, email=None, phoneNumber=None, address=None):
        """Edit user information"""
        if username is not None:
            self.username = username
        if fullname is not None:
            self.firstName = fullname[0]
            self.lastName = fullname[1]
        if password is not None:
            self.password = password
        if email is not None:
            self.email = email
        if phoneNumber is not None:
            self.phoneNumber = phoneNumber
        if address is not None:
            self.address = address

    def createCamp(self, id, volunteer, area):
        """Create camp"""
        if self.__class__.__name__ == 'Admin':
            camp = self.__createCamp(id, volunteer, area)

            return camp
        else:
            print('No permission.')

            return None

    def createPlan(self, id, emergencyType, area, startDate, endDate, camp):
        """Create plan"""
        if self.__class__.__name__ == 'Admin':
            plan = self.__createEmergencyPlan(id, emergencyType, area, startDate, endDate, camp)

            return plan
        else:
            print('No permission.')

            return None

    def manageAccount(self, account, manage):
        """Manage the volunteer's account"""
        if self.__class__.__name__ == 'Admin':
            if manage == 'activate':
                self.__activateAccount(account)
            elif manage == 'deactivate':
                self.__deactivateAccount(account)
            else:
                print('Wrong instruction.')
        else:
            print('No permission.')

    @staticmethod
    def __createEmergencyPlan(id, emergencyType, area, startDate, endDate, camp):
        """Create a emergency plan"""
        plan = Manage.EmergencyPlan(id, emergencyType, area, startDate, endDate, camp)

        return plan

    @staticmethod
    def __createCamp(id, volunteer, area):
        """Create a camp"""
        camp = Manage.Camp(id, volunteer, area)

        return camp

    @staticmethod
    def __activateAccount(account):
        """Activate the volunteer account"""
        account.activation = True

    @staticmethod
    def __deactivateAccount(account):
        """Deactivate the volunteer account"""
        account.activation = False

    def __str__(self):
        return "Name: " + self.username +\
            "\nEmail address: " + self.email +\
            "\nPhone number: " + str(self.phoneNumber) +\
            "\nAddress: " + self.address


class Volunteer(Admin):
    """Class of the volunteer"""
    def __init__(self, id, username, password, firstName, lastName, email, phoneNumber, address, role):
        """Initialise the volunteer"""
        super(Volunteer, self).__init__(username, firstName, lastName, password, email, phoneNumber, address)
        self.id = id
        self.role = role
        self.region = 'All'
        self.activation = True
        self.campID = "No Camp Assigned"
        self.availability = self.getAvailability()

    def getAvailability(self):
        # print(self.campID)
        if self.campID == "No Camp Assigned":
            return True
        else:
            return False

    def changeRole(self, role):
        """Change the identification of volunteer"""
        self.role = role

    def changeAvailability(self):
        """Change the availability of volunteer"""
        self.availability = not self.availability

    def changeRegion(self, region):
        """Change the working region of volunteer"""
        self.region = region

    @staticmethod
    def createRefugeeProfile(camp, refugeeID, refugeeName, refugeeNumber, medicalCondition):
        """Create a refugee profile"""
        camp.createRefugeeProfile(refugeeID, refugeeName, refugeeNumber, medicalCondition)

        return camp

    def __str__(self):
        info = super(Volunteer, self).__str__()
        return "Volunteer " + str(self.id) + "\n" +\
            info + "\nRole: " + self.role +\
            "\nAvailability: " + str(self.availability) +\
            "\nActivation: " + str(self.activation)
