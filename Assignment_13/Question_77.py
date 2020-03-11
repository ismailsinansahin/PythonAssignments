"""
All products that go into the warehouse go through a machine that checks if they are intact. 
To declare if the shipment of the product was good or bad it also gets a limited number of 
how many products can be broken for it to be considered a good shipment.
badP is a method that gets an int array named products and an int named limit.
products(int[]) - is an int array representing the products it checked, if the item is 
intact it will be represented by 1 if it is broken its 0. for example: [0,1,1,1,0], 
this array represents 2 broken items and 3 intact.
limit(int) - represents the max amount of broken items for this shipment to be considered 
good (and the method returns true) for example: products [1,1,1,1,0] limit:3, 
there is only 1 broken product and it is less than the limit (3) return true.
Sample Output:
     badP([1,1,1,1],5)
     returns true
     badP([1,1,1,1,0,0,0,0],2)
     returns false
     badP([1,1,0,0],2)
     returns false
     badP([1,1,1,0],6)
     returns true
"""

def badP(arr, limit):

    return arr.count(0) < limit

#  MAIN
    
arr1 = [1,1,1,1]
limit1 = 5
print("\nbadP(", arr1, ",", limit1, ")")
print("returns ", badP(arr1, limit1))


arr2 = [1,1,1,1,0,0,0,0]
limit2 = 2
print("\nbadP(", arr2, ",", limit2, ")")
print("returns ", badP(arr2, limit2))

arr3 = [1,1,0,0]
limit3 = 2
print("\nbadP(", arr3, ",", limit3, ")")
print("returns ", badP(arr3, limit3))

arr4 = [1,1,1,0]
limit4 = 6
print("\nbadP(", arr4, ",", limit4, ")")
print("returns ", badP(arr4, limit4))








