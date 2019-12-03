import api as ac

ADD_USER = 1
AUTHENTICATE = 2
ADD_USER_TO_GROUP = 3
ADD_OBJECT_TO_GROUP = 4
ADD_ACCESS = 5
CAN_ACCESS = 6
SHOW_USERS = 7
SHOW_USER_GROUPS = 8
SHOW_OBJECT_GROUPS = 9
SHOW_PERMISSIONS = 10
QUIT = 11

def getChoice():
    print()
    print('Select an option below')
    print(ADD_USER, ': Create a new user')
    print(AUTHENTICATE, ': Authenticate a user\'s password')
    print(ADD_USER_TO_GROUP, ': Add a user to a user group')
    print(ADD_OBJECT_TO_GROUP, ': Add an object to an object group')
    print(ADD_ACCESS, ': Define an access right')
    print(CAN_ACCESS, ': Check if a user can perform a specified operation on an object')
    print(SHOW_USERS, ': Show all current users')
    print(SHOW_USER_GROUPS, ': Show all current user groups')
    print(SHOW_OBJECT_GROUPS, ': Show all current object groups')
    print(SHOW_PERMISSIONS, ': Show all current permissions')
    print(QUIT, ': Quit')
    return int(input('Enter choice: '))
    
def add_user():
    user = input("Enter user to add: ")
    password = input("Enter password: ")
    ac.addUser(user, password)
        
        
def auth_user():
    user = input("Enter user to authenticate: ")
    password = input("Enter password to authenticate: ")
    ac.authenticate(user, password)

def add_user_to_group():
    user = input("Enter user to add to group: ")
    groupname = input("Enter group to add user into: ")
    ac.addUserToGroup(user, groupname)

def add_object_to_group():
    objectname = input("Enter object to add to group: ")
    groupname = input("Enter group to add object into: ")
    ac.addObjectToGroup(objectname, groupname)

def add_access():
    operation = input("Enter permission to be granted: ")
    usergroupname = input("Enter user group to be granted permission: ")
    objectgroupname = input("Enter object group to be granted permission: ")
    ac.addAccess(operation, usergroupname, objectgroupname)
    
def check_access():
    user = input("Enter user to be checked: ")
    operation = input("Enter permission to be checked: ")
    obj = input("Enter object to be checked: ")
    ac.canAccess(user, operation, obj)
    

def main():
    print('Welcome to Zach Christoff\'s Authentication and Access Control library!' )
    choice = getChoice()
    
    while (choice != QUIT):
        if (choice < 1 | choice > QUIT):
            choice = int(input('Incorrect choice.  Please choose again: '))
        elif (choice == ADD_USER):
                add_user()
        elif (choice == AUTHENTICATE):
            auth_user()
        elif (choice == ADD_USER_TO_GROUP):
            add_user_to_group()
        elif (choice == ADD_OBJECT_TO_GROUP):
            add_object_to_group()
        elif (choice == ADD_ACCESS):
            add_access()
        elif (choice == CAN_ACCESS):
            check_access()
        elif (choice == SHOW_USERS):
            print('\nUsers and passwords are:')
            ac.printUsers()
        elif (choice == SHOW_USER_GROUPS):
            print('\nUser groups are:')
            ac.printUsersGroups()
        elif (choice == SHOW_OBJECT_GROUPS):
            print('\nObject groups are:')
            ac.printObjectGroups()
        elif (choice == SHOW_PERMISSIONS):
            print('\nPermissions are: ')
            ac.printPermissions()
        
        
            
        choice = getChoice()
            
                
                
            
    
if (__name__== "__main__"):
    main()



