'''
Created on Sep 24, 2019

@author: Zach Christoff
'''
import ast


with open("user_list.txt", "r") as data:
    user_list = ast.literal_eval(data.read())
with open("user_groups.txt", "r") as data:
    user_groups = ast.literal_eval(data.read())
with open("object_groups.txt", "r") as data:
    object_groups = ast.literal_eval(data.read())
with open("permissions.txt", "r") as data:
    permissions = ast.literal_eval(data.read())
    

def addUser(user, password):
    if (checkUser(user_list, user) == True):
        print('The specified user has already been added.')
        return
    
    user_list[user] = password
    with open("user_list.txt", "w") as file:
        file.write(str(user_list))
    print("\nUser successfully added")

    
def authenticate(user, password):
    if (checkUser(user_list, user) == False):
        raise ValueError('There is no such user.')
    
    password_to_check = user_list[user]
    
    if (password_to_check == password):
        print('\nSuccess', user, 'is authenticated')
        return
    else:
        print('Incorrect password')
        return    


def addUserToGroup(user, groupname):
    if (checkUser(user_list, user) == False):
        raise ValueError(user, 'does not exist.') 
        
    if (checkGroupname(user_groups, groupname) == False):
        user_groups[groupname] = []
    
    if (checkUserInGroupname(user, user_groups[groupname])):
        print('The user is already in the specified group')
        return
    
    user_groups[groupname].append(user)
    print("\nSuccess. Users in", groupname, "group are:")
    
    print (user_groups[groupname])
    
    with open("user_groups.txt", "w") as file:
        file.write(str(user_groups))
        
    return

def addObjectToGroup(objectname, groupname):
    if (checkGroupname(object_groups, groupname) == False):
        object_groups[groupname] = []
        
    if (checkUserInGroupname(objectname, object_groups[groupname])):
        print('The object is already in the specified group')
        return
    
    object_groups[groupname].append(objectname)
    print("\nSuccess.  Objects in", groupname, "group are: ")
    
    print(object_groups[groupname])
    
    with open("object_groups.txt", "w") as file:
        file.write(str(object_groups))
    
    return
    
def addAccess(operation, usergroupname, objectgroupname = None):
    user_keys = list(user_groups.keys())
    for x in user_keys:
        if (x == usergroupname):
            user_key = x
            break
        
    object_keys = list(object_groups.keys())
    for x in object_keys:
        if (x == objectgroupname):
            object_key = x
            break
    
    if(objectgroupname == None):
        permissions[operation] = [user_key]
        print(operation, "permission successfully added")
        print("The current permissions are: ")
        print(permissions)
    else:   
        if not(operation in permissions.keys()):
            permissions[operation] = [[user_key]]
            index = permissions[operation].index([user_key])
            (permissions[operation][index]).append(object_key)
        else:
            permissions[operation].append([user_key, object_key])
        
        print(operation, "permission successfully added")
        print("The current permissions are: ")
        print(permissions)
    
    with open("permissions.txt", "w") as file:
            file.write(str(permissions))

def canAccess(user, operation, obj = None):
    if not(user in user_list):
        raise ValueError('There is no such user')
    
    if not(operation in permissions):
        raise ValueError('There is no such permission')
    
    permission_list = permissions[operation]
    
    
    if not (obj == None):
        user_group = findUsergroup(user, permission_list)
        object_group = findObjectgroup(obj, permission_list)
        for x in permission_list:
            if(x[0] == user_group):
                if(x[1] == object_group):
                    print(user, 'has access to', object)
                    return
        
        print(user, 'does not have access to', object)
    else:
        user_group = findUsergroupNoObject(user, permission_list)
        for x in permission_list:
            if(x == user_group):
                print(user, 'has permissions to', operation)
                return
        print(user, 'does not have permission to', operation)
               
    
    
            
      

'''
Checks if the user exists
Returns true if the user exists, false otherwise
'''
def checkUser(list_of_users, user):
    if user in list_of_users.keys():
        return True
    else:
        return False

'''
Checks if the groupname exists
Returns true if the groupname exists, false otherwise
'''
def checkGroupname(list_of_groups, groupname):
    if groupname in list_of_groups.keys():
        return True
    else:
        return False
   
'''
Checks if the user is in the specified groupname
Returns true if the user is in the specified groupname, false otherwise
'''    
def checkUserInGroupname(user, groupname):
    for x in groupname:
        if (x == user):
            return True
        else:
            return False

def findUsergroup(user, lst):
    for x in lst:
        potential_key = x[0]
        lst_of_users = user_groups[potential_key]
        if(user in lst_of_users):
            return potential_key  
        
def findUsergroupNoObject(user, lst):
    for x in lst:
        potential_key = x
        lst_of_users = user_groups[potential_key]
        if(user in lst_of_users):
            return potential_key     
        
            
def findObjectgroup(obj, lst):        
    for x in lst:
        potential_key = x[1]
        lst_of_objects = object_groups[potential_key]
        if(obj in lst_of_objects):
            return potential_key
        
        

def printUsers():
    print(user_list)
    
def printUsersGroups():
    print(user_groups)
        
def printObjectGroups():
    print(object_groups)

def printPermissions():
    print(permissions)
        