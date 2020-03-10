"""
Switch the last element in an array with the first and return the array.
Sample Output:
     do_switch([1,2,3,4])
     returns:[[4,2,3,1]
     do_switch([7,2,3,5])
     returns:[5,2,3,7]
"""

def do_switch(nums):
    
    temp = nums[0]
    nums[0] = nums[len(nums)-1]
    nums[len(nums)-1] = temp

    return nums
    
#  MAIN
    
nums = [1,2,3,4]
print("\ninput   : ", nums)
print("output : ", do_switch(nums))