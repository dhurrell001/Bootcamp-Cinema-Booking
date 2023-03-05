import os
import pickle
import time
import datetime

class ValueOutOfRange(Exception): # creates child class of Exception
  pass
def ClearScreen():
    # Clearing the Screen
    os.system('cls')
 
#======================= Cinema classes ===================

class Screen:

    def __init__(self,name):
        self.name =name
        self.seating = [[True for x in range(10)] for y in range(5)] # creates an array of seats set at True fo available
        self.row = {'a':0,'b':1,'c':2,'d':3,'e':4}
        self.moviesShowing = [] # will take movie object
        self.times = {1:'10.30',2:'13.00',3:'16.00',4:'19.00'}
        self.cinema_prices = {'Standard Adult':12,'Standard Child':8,'Standard Senior':10
                            ,'Premium Adult':18,'Premium Child':12,'Premium Senior':14
                            ,'Loyalty Discount Adult':8,'Loyalty Discount Child':4
                            ,'Loyalty Discount Senior':4}
      
    def SeatAvailable(self,row,seat):
        # Checks to see in seat has already been booked. True for available. False for booked

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
        print('================= MOVIES SHOWN ==================')
        for film in self.moviesShowing:
            print(f'{film.title}\n{film.times}\n')

    def MovieMenu(self):
        brunning = True
        while brunning:
            try:
                print('================= MOVIES SHOWING ===============')
                for i in range(0, len(self.moviesShowing)):
                    print(str(i) + ": " + str(self.moviesShowing[i].title))

                choice = int(input("\nPlease select a movie from the above options \n"))

                return self.moviesShowing[choice].title
            except:
                print('Please enter  valid input')
                time.sleep(0.5)
                ClearScreen()
                continue
    
    def TimeMenu(self):
        brunning = True
        while brunning:
            try:
                print('================= TIMES SHOWING ===============')
            
                for k,v in self.times.items():
                    print(f'{k} : {v}')
                iChoice = int(input('Please enter a time you would like to view movie : \n'))
                return self.times[iChoice]
            except:
                ClearScreen()
                print('Please enter a valid number\n')
                time.sleep(1)
                continue
        
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
        print(f'Date Joined : {self.date_joined}\n')

class Admin:
    def __init__(self,Name,Surname,username,password):

        self.name = Name
        self.surname = Surname
        self.username = username
        self.password = password
    def __str__(self):
        return (f'{self.username} {self.password}')

class Booking(Member,Screen):

    def __init__(self):

        self.name = ""
        self.surname = ""
        self.movie = ""
        self.time = ''
        self.date = None
        self.tickets = 0
        self.seats = []
        self.current_screen = 0
        self.ticket_price = 0

    def GetMember(self):

        name = GetName('m')
        surname = GetSurname('m' )
        
        for guest in members:
            if guest.name == name and guest.surname == surname:
                current_member = guest
                print('\nMember Found..')
                input()

                self.name = name
                self.surname = surname

    def GetSeats(self):

        #self.current_screen = GetScreen()    
        ClearScreen()  
        try:       
            ticket_amount = int(input('\nHow many tickets would you like : '))
        except:
            print('Please enter a valid number')
            time.sleep(0.5)
            ClearScreen()
            ticket_amount = int(input('\nHow many tickets would you like : '))

        self.tickets = ticket_amount
        for x in range(ticket_amount):
            row ,seat= SeatingMenu(self.current_screen)
            #current_member.AssignSeats(row,seat)  
            self.seats.append((row.upper(),seat))
            input()
            ClearScreen()

    def GetMovie(self):

        self.current_screen = GetScreen() 
        Selected_Movie =self.current_screen.MovieMenu()
        #self.current_screen.TimeMenu()
        self.movie = Selected_Movie 
    def GetTime(self):
        self.time = self.current_screen.TimeMenu()

    def GetBookingDate(self):
        self.date = datetime.datetime.now()

    def GetTicketPrice(self):

        age_dictionary = {1:'Adult',2:'Child', 3:'Senior'}
        quality_dictionary = {1:'Standard',2:'Premium',3:'Loyalty Discount'}

        menu_list_age = ['============== TICKET TYPE =======\n','Adult','Child','Senior']
        ticket_type = DynamicMenu(menu_list_age)
        
        menu_list_quality = ['============== TICKET QUALITY ==========\n','Standard','Premium','Loyalty discount']
        ticket_quality =DynamicMenu(menu_list_quality)
        ticket = f'{quality_dictionary[ticket_quality]} {age_dictionary[ticket_type]}'
        self.ticket_price = self.current_screen.cinema_prices[ticket]

    def PrintTicket(self):

        print('========== TICKET ==========')
        print(f'\nName : {self.name} {self.surname}')
        print(f'Date Booked : {self.date}')
        print(f'Movie : {self.movie}')
        print(f'Seats : {self.seats}')
        print(f'Viewing time : {self.time}')
        print(f'Ticket Price : {self.ticket_price}')
        print(f'Admit : {self.tickets}\n')
        print('============================')

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

def GetName(flag):
    # flag  'm' for member message
    if flag.lower() == 'm':
        return input('\nPlease enter cinema members first name name :\n') 
    return input('\nPlease enter your first name :\n')  

def GetSurname(flag):
    # flag  'm' for member message
    if flag.lower() == 'm':
        return input('\nPlease enter cinema members surname : \n') 
    return input('\nPlease enter your surname : \n')  

def GetUsername():
  return input('\nPlease enter your new username : \n')    

def GetPassword():
  return input('\nPlease enter your new password : \n')

def GetMemberDetails():
    
    user_name = Check_new_Username(GetUsername()) 
    user_password = Check_new_Password(GetPassword())

def Check_If_Admin():
    #Checks through list of admin class objects (Admin_Detail) and return true if
    # admin account exists. else false

    Username = input('Please enter your admin username :\n ')
    Password = input('Please enter your password :\n ')

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
        ClearScreen()
        print('New cinema member created...')
        time.sleep(1)
    else:
        print('\nPlease login as administrator to create new members')

def CreateAdmin():
    #Create a new admin account, running checks for valid password and username
    # add new admin object to Admin_details list

    name = GetName('a')
    surname = GetSurname('a')
    username = Check_new_Username(GetUsername()) 
    userpassword = Check_new_Password(GetPassword())

    Admin_details.append(Admin(name,surname,username,userpassword))
    ClearScreen()
    print('New Admin. Account created....')
    time.sleep(1)

# ======================= Cinnema fuctions =====================


def AddMovie(screenObject):
    # parameter is a Screen() object. gets movie title and adds to screen object,
    # movies showing attribute.

    print('============== Add New Movie ==============')
    title =input ('\nPlease enter the name of the movie : \n')
    screenObject.moviesShowing.append(Movie(title))

def AddScreen():
    # Creates new screen object and add to screens list

    print('============== ADD CINEMA SCREEN ==================')
    ScreenName = input('Please enter the name of New Cinema Screen : \n\n')
    Screens.append(Screen(ScreenName))

def GetScreen():
    brunning = True
    valid_screens = [screen for screen in Screens]
    
    while brunning:
        try:
            print('================= AVAILABLE SCREENS ===============')
            for i,screen in enumerate(valid_screens):
                print(f'{i} : {screen.name}')

            iChoice = int(input('Please enter a number for screen to view :'))
            return valid_screens[iChoice]
        except:
            print('error here')
            input()
            print('Please enter a valid number')
            time.sleep(0.5)
            iChoice = int(input('Please enter a number for screen to view :'))


                
"""
def GetScreen():
    #Prints list of existing saved screens. compares user input to screen.name in Saved screen list
    #return screen object
    bRunning = True
    while bRunning:
        print('=============== AVAILABLE SCREENS ===============\n')
        for x in Screens:
            print(x.name)
        screen_choice = input('\nPlease enter the name of screen you would like to access : \n')
        for screen in Screens:
            if screen.name == screen_choice:
                return screen
        else:
            print('Screen name not found')
            input()
            continue"""

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
        

def DynamicMenu(list):
  # Takes menu options a list, error checks for integer input, return integer
  brunning = True # creates loop. exits loop when valid value is returned
  
  while brunning:
    
    ClearScreen()
    print(list[0])
    
    try:
      for num in range(1,len(list)): # uses range to index over each item of list
        print(f'{num} : {list[num]}')
      
      iChoice = int(input('\nPlease select an option : \n'))
      
      if iChoice > len(list)-1 or iChoice < 1: # create conditoion to trigger custom exception
        raise ValueOutOfRange
        
    except ValueOutOfRange: # triggers error if input is not within menu options (IndexError)
      print(f'Please enter a number between 1 and {len(list)-1}')
      input('\n[Please press ENTER to continue....]')
      
    except ValueError: # Triggers value error i.e letter entered instead of number
      print(f'Whoops ... Please enter a whole number between 1 and {len(list)-1}')
      input('\n[Please press ENTER to continue....]')
      continue

    except: # General exception if above exceptions are not triggered
      print('Unknown Error. Please try again')
      input('\n[Please press ENTER to continue....]')
    else: # returns chpice if nothing else is triggered
      return iChoice   
        

def AdminMenu():

    bRunning = True
    while bRunning:
        ClearScreen()
        print('============= Welcome to Admin Menu ===========')
        print('\n1) Create Admin Account 2) Create new member')
        print('3) Add Movie  4) Add New Screen 5) Save details')
        print('6) View existing members 7) Main Menu')
        iChoice = input('\nPlease select an option : \n')

        if iChoice =='1':

            CreateAdmin()
            print(Admin_details)

        if iChoice =='2':
            CreateMember()

        if iChoice =='3':
            screen = GetScreen()
            AddMovie(screen)
            screen.PrintScreen()
            input()

        if iChoice =='4':
            AddScreen()

        if iChoice =='5':
            SaveToFile(Admin_details,'AdminTest')
            SaveToFile(members,'CinemaMembers')
            SaveToFile(Screens,'Movies')
        if iChoice == '6':
            for member in members:
                member.PrintMember()
            input()
        if iChoice == '7':
            MainMenu()



def MainMenu():

    bRunning = True
    while bRunning:
        ClearScreen()
        print('============= Welcome to Weston Cinema ===========')
        print('\n1) Administration Menu   2) Book Tickets')
        print('3) Save Details  4)View screen movies ' )
        
        print('5) View movie times 6) Exit Program')
        iChoice = input('\nPlease select an option : \n')

        if iChoice =='1':

            AdminMenu()
        if iChoice =='2':
            ClearScreen()
            # Assign Variables for this booking
            current_booking = Booking()
            current_booking.GetMember()
            ClearScreen()
            current_booking.GetMovie()
            ClearScreen()
            current_booking.GetSeats()
            ClearScreen()
            current_booking.GetTime()
            ClearScreen()
            current_booking.GetBookingDate()
            ClearScreen()
            current_booking.GetTicketPrice()
            current_booking.PrintTicket()          
            input()  
            
        
        if iChoice =='3':
            SaveToFile(Admin_details,'AdminTest')
            SaveToFile(members,'CinemaMembers')
            SaveToFile(Screens,'Movies')

        if iChoice =='4':
            current_screen = GetScreen()
            ClearScreen()
            current_screen.PrintScreen()
            input()

        if iChoice =='5':
            current_screen = GetScreen()
            print('i am here')
            input()
            current_screen.TimeMenu()
            input()
       

def SeatingMenu(screen_name):
    #Takes user input for row letter and seat number. Takes screen object as parameter. 
    #uses screem method to check if seat is available. 
    # if seat available returns row and seat as tuple

    ValidResponseRow = 'abcde'
    ValidResponseSeat = range(1,11)
    InnerWhile = True

    while InnerWhile:
        print('=============== Seating Reservation Menu ================')
        Row = input('\nPlease enter the row letter [A,B,C,D,E] : ')
        if Row in ValidResponseRow:
            Seat = int(input('\nPlease enter a seat number : \n'))
            if int(Seat)in ValidResponseSeat:
                
                if screen_name.SeatAvailable(Row,Seat )== True:    
                    return (Row,Seat)
                else:                   
                    input()
                    continue
        else:
            print('\nInvalid Seat Number')
            input()
            SeatingMenu(screen_name)
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
    print(x)
input()
members = OpenFiles('CinemaMembers')
Standard_users = []
Screens= OpenFiles('Movies')





#screen1.PrintScreen()
#input()
    #print(x.title)
#input()

MainMenu()
"""
file opening error messages
from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))



"""
  

