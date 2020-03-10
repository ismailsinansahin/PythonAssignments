"""
Create a method that is called timesTwo takes in a single parameter 
- an ArrayList of Integers called nums returns nothing
This method should take the ArrayList parameter and multiply every value by two.
"""

def timesTwo(nums):
    
    for i in range(len(nums)):
        nums[i] *= 2
    
    print("output : ", nums)
    
#  MAIN
    
nums = [1,2,3,4]
print("\ninput   : ", nums)
timesTwo(nums)

