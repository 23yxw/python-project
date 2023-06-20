# Utilities for users
import random
import re
import Users
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

global is_login

MAIL = {
    "from": 'bohongwang00@gmail.com',
    "pwd": 'qacpdelotrpqrcrz',
    "smtp": 'smtp.gmail.com',
}


def send_email(user_reset_pwd, verification_code):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header('Password Reset Verification Code', 'utf-8')
    msg['From'] = MAIL['from']
    msg['To'] = user_reset_pwd

    html_message = MIMEText(verification_code, 'plain ', 'utf-8')
    html_message["Accept-Language"] = "en-us"
    html_message["Accept-Charset"] = "ISO-8859-1,utf-8"

    msg.attach(html_message)
    try:
        server = smtplib.SMTP_SSL(MAIL['smtp'])
        server.login(MAIL['from'], MAIL['pwd'])
        server.sendmail(MAIL['from'], user_reset_pwd, msg.as_string())
        print("\033[92m {}\033[00m".format('Password reset verification code has sent. Please check your email.'))

    except Exception as e:
        print('error', e)


def login(inObj):
    """Login menu"""

    def print_login_menu():
        """print login menu"""
        print("\n=====================================================")
        print("                  LOGIN OPTIONS: ")
        print("[1] Admin Login")
        print("[2] Volunteer Login")
        print("[3] Register as a Volunteer")
        print("[4] Forgot Password\n")

    user = inObj[0]
    userList = inObj[1]

    while True:
        print_login_menu()
        user_input = input("Enter a valid number: ")
        if user_input == "1":
            return admin_login(user, userList) + inObj[2:]
        elif user_input == "2":
            return volunteer_login(user, userList) + inObj[2:]
        elif user_input == "3":
            return register(user, userList) + inObj[2:]
        elif user_input == "4":
            return password_reset(userList, user) + inObj[2:]
        else:
            print("=====================================================")
            print("\nInvalid input, please try again\n")
            print("=====================================================")


def admin_login(user, userList):
    """print login menu"""
    global is_login

    print("\n=====================================================")
    print("                  ADMIN LOGIN\n")
    adminName = get_nonempty_input("Administrator name")
    password = get_nonempty_input("Password")

    if adminName == userList[0].username:
        if password == userList[0].password:
            print("\033[92m {}\033[00m".format("You have logged in as an administrator!"))
            is_login = True
            user = userList[0]

        else:
            print("\033[91m {}\033[00m".format("\n[ERROR] Incorrect password!"))

    else:
        print("\033[91m {}\033[00m".format("\n[ERROR] Wrong admin username!"))

    return [user, userList]


def volunteer_login(user, userList):
    """print login menu"""
    global is_login

    print("\n=====================================================")
    print("                VOLUNTEER LOGIN\n")
    username = get_nonempty_input("username")
    password = get_nonempty_input("Password")

    for volunteer in userList[1:]:
        if str(volunteer.username) == username:
            if not volunteer.activation:
                print("\033[91m {}\033[00m".format("\n[ERROR] Your account has been locked! Please contact the admin for more info"))

                return [user, userList]

            elif volunteer.password == password:
                print("\033[92m {}\033[00m".format("You have logged in, " + volunteer.firstName))
                is_login = True
                user = volunteer

                return [user, userList]

            else:
                print("\033[91m {}\033[00m".format("\n[ERROR] Wrong password!"))

                return [user, userList]

    print("\033[91m {}\033[00m".format("\n[ERROR] User ID doesn't exist! Or your account has been deleted!"))

    return [user, userList]


def password_reset(userList, user):
    """print password reset menu"""
    print("\n=====================================================")
    print("Please enter your userID:\n")
    userID = get_nonempty_input("UserID")
    print("Please enter the email address when you registered the system:\n")
    volunteer_item = {}
    for volunteer in userList[1:]:
        if str(volunteer.id) == userID:
            volunteer_item = volunteer
            break
    while True:
        email = get_nonempty_input("Email")
        if str(volunteer_item.email) == email:
            break
        else:
            print("\033[91m {}\033[00m".format("email does not match. Please try again"))

    roundStr = ''.join(random.sample(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w',
         'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 8))

    send_email(email, roundStr)
    while True:
        Verification_Code = get_nonempty_input("Verification_Code")
        if Verification_Code == roundStr:
            print("Verification code accepted!")
            break
    print("\033[93m {}\033[00m" .format('Your password should be 5-12 digits, containing:'
          '\n at least one uppercase letter;\n at least one lowercase letter;\n at least one number;'
          '\n no space letter;\n and at least one special letter.'))
    while True:
        New_password = get_nonempty_input("New_password")
        done, error = pwd_check(New_password)
        if done:
            break
    volunteer_item.password = New_password

    return [user, userList]


def pwd_length(password, min_digit=5, max_digit=12):
    if min_digit <= len(password) <= max_digit:
        return True, None
    else:
        print("\033[91m {}\033[00m".format("The length of password should be 5-12 digits, please try again. "))
        return False, None


def pwd_capital(password):
    upper = re.search("[A-Z]+", password)
    if upper:
        return True, None
    else:
        print("\033[91m {}\033[00m".format("Your password should contain at least one Uppercase letter, Please try again."))
        return False, None


def pwd_lowercase(password):
    lower = re.search("[a-z]+", password)
    if lower:
        return True, None
    else:
        print("\033[91m {}\033[00m".format("Your password should contain at least one Lowercase letter, please try again."))
        return False, None


def pwd_number(password):
    number = re.search("[0-9]+", password)
    if number:
        return True, None
    else:
        print("\033[91m {}\033[00m".format("Your password should contain at least one number, please try again."))
        return False, None


def pwd_special(password):
    special = re.search("[~!@#$%^&*()\-_=+]+", password)
    if special:
        return True, None
    else:
        print("\033[91m {}\033[00m".format("Your password should contain at least one special letter, please try again. "))
        return False, None


def pwd_space(password):
    space = re.search("[ ]+", password)
    if space:
        print("\033[91m {}\033[00m".format("Your password should not contain any space letter, please try again. "))
        return False, None
    else:
        return True, None


def pwd_check(password):
    for temp in [pwd_length, pwd_capital, pwd_lowercase, pwd_number, pwd_special, pwd_space]:
        done, error = temp(password)
        if not done:
            return False, error
    return True, None


def register(user, userList):
    """register a volunteer account
        INCOMPLETE: need to add password RegEx
    """
    print("\n=====================================================")
    print("             VOLUNTEER REGISTRATION")
    print("\033[93m {}\033[00m" .format("\nPlease fill in the following information: \n"))

    if len(userList) == 1:
        userID = 1
    else:
        userID = userList[-1].id + 1

    
    while True:
        username = get_nonempty_input("Username")
        isvalid = True
        for user1 in userList:
            if user1.username == username:
                isvalid = False
        if not isvalid:
            print("\033[91m {}\033[00m".format("\nUsername already exists! Choose another one")) 
            print("\n=====================================================") 
        else:      
            break

    
    print("\033[93m {}\033[00m" .format('\nYour password should be 5-12 digits, containing:\n at least one uppercase letter;'
          '\n at least one lowercase letter;\n at least one number;'
          '\n no space letter;\n and at least one special letter.'))
    while True:
        password = input("\nEnter your password: ")
        done, error = pwd_check(password)
        if done:
            break

    while True:
        confirm_password = input("Confirm your password: ")
        if password != confirm_password:
            print("\033[91m {}\033[00m".format("Your passwords do not match, try again!\n"))
        else:
            break

    firstName = get_nonempty_input("First Name")
    lastName = get_nonempty_input("Last Name")

    while True:
        email = get_nonempty_input("Email")
        if re.search(r"([a-z]*\d*)@([a-z]*\d*)", email, re.I) is not None \
                and " " not in email \
                and "@" != email[len(email) - 1] and "@" != email[0]:
            break
        else:
            print("\033[91m {}\033[00m".format("Wrong format of email address."))

    while True:
        phone_number = get_nonempty_input("Phone number")
        try:
            phone_number = int(phone_number)
            break
        except ValueError:
            print("\033[91m {}\033[00m".format("Phone number should be integer."))

    address = get_nonempty_input("Address")

    print(
        "\n=====================================================\n"
        "                      ROLES\n"
        "[1] Medical help\n"
        "[2] Hygiene and cleanliness\n"
        "[3] Information Entry\n"
        "[4] Mental health help\n"
        "[5] Order Maintenance\n"
    )

    while True:
        numbers = {
            '1': "Medical help",
            '2': "Hygiene and cleanliness",
            '3': "Information Entry",
            '4': "Mental health help",
            '5': 'Order Maintenance'
        }
        role = get_nonempty_input("Select a valid role")
        if role in ('1', '2', '3', '4', '5'):
            role = numbers[role]
            break
        else:
            print("\033[91m {}\033[00m".format('Input error, please reselect!'))

    new_volunteer = Users.Volunteer(userID, username, password, firstName, lastName, email, phone_number, address, role)
    userList.append(new_volunteer)

    print("You are registered as a volunteer successfully. Your ID is: ", userID)

    return [user, userList]


def get_nonempty_input(strgot):
    """checks if input is empty"""
    while True:
        value = input(strgot + ": ")
        if value.strip() == "":
            print("\033[91m {}\033[00m".format("Your {} cannot be empty, try again!\n".format(str)))
        else:
            return value


# def check_username(str):
#     """checks if username is unique"""
#     pass


# def check_password():
#     """checks if password is right format"""
#     pass


# def check_camp_id():
#     """checks if camp ID exists"""
#     pass


def logout(inObj):
    global is_login
    user = inObj[0]

    is_login = False
    user = None

    return [user] + inObj[1:]
