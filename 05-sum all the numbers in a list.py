##Write a Python function to sum all the numbers in a list.
##Sample List : (8, 2, 3, 0, 7)
##Expected Output : 20 

def sum(num):
    total = 0
    for x in num:
        total += x
    return total
print(sum((8,2,3,0,7)))