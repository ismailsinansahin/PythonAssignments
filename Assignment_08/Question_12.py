def hamletQuote(state1, state2):
    if state1== "True" or state2== "True":
        return True
    else:
        return False

state1 = input("Please enter the state 1 - 'True or False': ")
state2 = input("Please enter the state 2 - 'True or False': ")
print("Returns : ",hamletQuote(state1, state2))
    

# Please enter the state 1 - 'True or False': True
# Please enter the state 2 - 'True or False': True
# Returns :  True

# Please enter the state 1 - 'True or False': False
# Please enter the state 2 - 'True or False': True
# Returns :  True

# Please enter the state 1 - 'True or False': True
# Please enter the state 2 - 'True or False': False
# Returns :  True

# Please enter the state 1 - 'True or False': False
# Please enter the state 2 - 'True or False': False
# Returns :  False