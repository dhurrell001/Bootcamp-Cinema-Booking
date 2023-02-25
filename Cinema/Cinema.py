import os
import pickle
import time
def ClearScreen():
    # Clearing the Screen
    os.system('cls')
 
#======================= Cinema classes ===================

class Screen:

    def __init__(self):
        self.seating = [[True for x in range(10)] for y in range(5)]
        self.row = {'a':0,'b':1,'c':2,'d':3,'e':4}
        self.moviesShowing = [] # will take movie object
        

    def SeatAvailable(self,row,seat):

        if self.seating[self.row[row]][seat]== True:
            print('\nSeat Available')
            self.seating[self.row[row]][seat] = False
            input()
            return True
        else:
            print('\nSeat is unavailable')
            input()
            return False
    def PrintScreen(self):
        for film in self.moviesShowing:
            print(f'{film.title}\n{film.times}\n')

class Movie:

    def __init__(self,title): # Will take variable in future

        self.title = title
        self.times = {1:'10.30',2:'13.00',3:'16.00',4:'19.00'}

class Member:

    def __init__(self,Name,Surname):

        self.name = Name
        self.surname = Surname
        self.password = ""
        self.date_joined = ""
        self.loyalty = 0
        self.seats = []

    def AssignSeats(self,row,seat):
        self.seats.append((row,seat))

    def PrintMember(self):
        print(f'First name : {self.name} \nSurname : {self.surname}')
        print(f'Date Joined : {self.date_joined} \nSeats : {self.seats}')

class Admin: 
    def __init__(self,Name,Surname,username,password):

        self.name = Name
        self.surname = Surname
        self.username = username
        self.password = password
        

#===================  Login Functions =============================
def Check_new_Username(username):
           
    bFlag = True
    while bFlag:
        lErrorMessages = []
        if len(username) < 5:
            lErrorMessages.append('Username too short. Must be at least 5 characters')
        
        if username.isalpha() == False:
            lErrorMessages.append('Username must be only letters')

        if len(lErrorMessages) > 0:
            for item in lErrorMessages:
                    print(item)
            username = input('Please re-enter username : ')
                   
        else:
            print('\n======= Username saved =======\n')
            return username

def Check_new_Password(password):

    lErrorMessages = []
    sSpecial_characters = '!@#$%^&*()-+?_=,<>/"'
    iSpecial_count = 0
    #check if password is correct length and contains a lower and uppercase char 

    if len(password) < 6:
        lErrorMessages.append('Password too short. Must be at least 6 characters')
    if password.lower() == password:
        lErrorMessages.append('Password must contain at least one uppercase character')
    if password.upper() == password:
        lErrorMessages.append('Password must contain at least one lowercase character')
        
    #= check if password contains special character==
    for letter in password:
        if letter in sSpecial_characters:
            iSpecial_count+=1
    if iSpecial_count == 0:
        lErrorMessages.append('Password must contain a special character')

    if len(lErrorMessages) > 0:
        for item in lErrorMessages:
            print(item)
        password = Check_new_Password(GetPassword())
    else:
        print('\n======= password saved =======\n')
    return password

def GetName():
    return input('\nPlease enter your your name : \n ')  

def GetSurname():
    return input('\nPlease enter your your surname : \n')  

def GetUsername():
  return input('\nPlease enter your your new username : \n')    

def GetPassword():
  return input('\nPlease enter your your new password : \n')

def GetMemberDetails():
    
    user_name = Check_new_Username(GetUsername()) 
    user_password = Check_new_Password(GetPassword())

def Check_If_Admin():
    #Checks through list of admin class objects (Admin_Detail) and return true if
    # admin account exists. else false

    Username = input('Please enter your admin username : ')
    Password = input('Please enter your password')

    for user in Admin_details:
        if user.username == Username and user.password == Password:
            return True
    print ('Sorry, You do not have admin privilages')
    return False

def CreateMember():
    # checks if user has admin privaliges to allow for new member to be created
    # if member is created, member object added to members list

    if Check_If_Admin() == True:
        name = input('\nPlease enter members first name : \n')
        surname = input('\nPlease enter members surname : \n')

        members.append(Member(name,surname))
    else:
        print('\nPlease login as administrator to create new members')

def CreateAdmin():
    #Create a new admin account, running checks for valid password and username
    # add new admin object to Admin_details list

    name = GetName()
    surname = GetSurname()
    username = Check_new_Username(GetUsername()) 
    userpassword = Check_new_Password(GetPassword())

    Admin_details.append(Admin(name,surname,username,userpassword))
# ======================= Cinnema fuctions =====================



def AddMovie(screenObject):
    # parameter is a Screen() object. gets movie title and adds to screen object,
    # movies showing attribute.

    print('============== Add New Movie ==============')
    title =input ('\nPlease enter the name of the movie')
    screenObject.moviesShowing.append(Movie(title))

#=====================  Menu Functions ================================

def Continue():
    # Routine to allow exit from menu\program

    sValidResponse = 'ynYn'   
    sChoice = input('\nWould you like to exit to main menu? Y,N,y,n : ')

    if sChoice in sValidResponse :
        if sChoice.lower() == 'n':
            return True
        else: 
            ClearScreen()
            print('\nThank you for using Cinema Booking'.center(60,'+'))
            return False
     
def MainMenu():

    bRunning = True
    while bRunning:
        ClearScreen()
        print('============= Welcome to Weston Cinema ===========')
        print('\n1) Create Admin Account         2) Create new member')
        print('3) Book tickets ')
        print('5) Assign movies to screen   6)View movie times')
        print('7) Save details 8) Add movie')
        iChoice = input('\nPlease selcet an option : \n')

        if iChoice =='1':

            CreateAdmin()
            print(Admin_details)

        if iChoice =='2':
            CreateMember()

        if iChoice =='3':
            current_member = None
            name = GetName()
            surname = GetSurname()
            for guest in members:
                if guest.name == name and guest.surname == surname:
                    current_member = guest
                    print('Welcome')
                    input()
                
            ticket_amount = int(input('\nHow many tickets would you like : '))
            for x in range(ticket_amount):
                seat,row = SeatingMenu()
                current_member.AssignSeats(row,seat)
                
              
            print(current_member.PrintMember())
            input()  

        if iChoice =='5':

            AddMovie(screen1)
            screen1.PrintScreen()
            input()


        if iChoice =='7':
            SaveToFile(Admin_details,'AdminTest')
            SaveToFile(members,'CinemaMembers')

       

def SeatingMenu():

    ValidResponseRow = 'abcde'
    ValidResponseSeat = range(1,11)
    InnerWhile = True

    while InnerWhile:
        print('=============== Seating Reservation Menu ================')
        Row = input('\nPlease enter the row letter [A,B,C,D,E] : ')
        if Row in ValidResponseRow:
            Seat = int(input('\nPlease enter a seat number : \n'))
            if int(Seat)in ValidResponseSeat:
                
                if screen1.SeatAvailable(Row,Seat )== True:    
                    return (Row,Seat)
                else:                   
                    input()
                    continue
        else:
            print('\nInvalid Seat Number')
            input()
            SeatingMenu()
    else:
        print('\nInvalid Row letter ')
        input()
        SeatingMenu()


# ======================== Save Data Functions ===================
def SaveToFile(SaveVarable,filename):
    # saveVariable is the existing variable containing information to be saved
    # filename is name of file to be created (string)
       
      fileObj = open(filename, 'wb')
      pickle.dump(SaveVarable,fileObj)
      fileObj.close()
      print('File Saved')
      time.sleep(1)

def OpenFiles(filename):
      fileObj = open(filename, 'rb')
      return pickle.load(fileObj)
      fileObj.close()
    

        




Admin_details = OpenFiles('AdminTest')
for x in Admin_details:
    print(x.name)
members = OpenFiles('CinemaMembers')
Standard_users = []
screen1= Screen()

MainMenu()
