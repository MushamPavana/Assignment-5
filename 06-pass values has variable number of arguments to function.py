#write a function to find sum of given values, pass values has variable number of arguments to function

def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total
result = find_sum(11,22,33,44,55)
print("Sum:", result) 

