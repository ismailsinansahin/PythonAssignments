"""
Given an array nums, calculate the count of even numbers in nums and print out to console.
Sample Output:
     nums → [2, 1, 2, 3, 4]) → 3
     nums → [2, 2, 0, 3, 5]) → 3
     nums → [1, 3, 5, 7, 9]) → 0
"""

def countEvens(nums):
    counter = 0
    
    for each in nums:
        if each%2 == 0:
            counter += 1
            
    return counter

#  MAIN
    
nums1 = [2, 1, 2, 3, 4]
nums2 = [2, 2, 0, 3, 5]
nums3 = [1, 3, 5, 7, 9]

print("\nnums1 -> ", nums1, " ==> ", countEvens(nums1))
print("\nnums2 -> ", nums2, " ==> ", countEvens(nums2))
print("\nnums3 -> ", nums3, " ==> ", countEvens(nums3))