"""
Create a method that: is called repeatAL takes in a single parameter 
- an ArrayList of Booleans and returns nothing
This method should modify its ArrayList parameter by repeating its ArrayList values.
For example, if the parameter is 
(true, false, false)
The modified ArrayList should be
(true, false, false, true, false, false)
"""

def repeatAL(bools):
    
    for i in range(len(bools)):
        bools.append(bools[i])
    
    print("output : ", bools)
    
#  MAIN
    
bools = [True, False, False]
print("\ninput   : ", bools)
repeatAL(bools)

