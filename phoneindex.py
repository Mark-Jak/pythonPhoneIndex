phoneBook={'1111111111':'Amal',
           '2222222222':'Maged',
           '3333333333':'John',
           '4444444444':'Marko',
           '5555555555':'Nader',
           '6666666666':'Vico'}


#fun check number exist return true/false
def checkNum(num):
    if num in phoneBook:
        return True
    else:
        return False
    

#fun return name  
def getName(num):
    return phoneBook[num]


#fun check number if not 10 digits  
def validate(num):
    if (len(num)== 10):
        return True
    else:
        return False
 
#fun add number // return successfuly added or error 
def addNewNumber():
    num=input('add new number:')
    #check format
    if not (validate(num)):
        return "number is not valid format"
    #check exist
    elif checkNum(num):
        return "number exist and name is:  " +   getName(num)
    #if valid format and not exist, then add
    else:
        name=input('number is valid formate and is not exist, please add correspondeing name: ')
        phoneBook[num]=name
        return 'successfully added '+ getName(num) + ' to number '+ num



print (getName('1111111111'))
print (checkNum('1111111110'))
print(validate('1111111111'))
print (addNewNumber())
