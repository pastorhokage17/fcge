#function find_divisible(a, b, k) is defined on line 28
def prompt():
    print("Problem B: Write a function find_divisible(a, b, k) that accepts\nthree integers: a, b and k, and returns the total\ncount of the numbers between a and b (inclusive)\nthat are divisible by k\n")
    try:
        ar = []
        ar.append(int(input("a >> ")))
        ar.append(int(input("b >> ")))
        ar.append(int(input("k >> ")))
        print("Your array: ", ar)
        return ar

    except:
        print("Please enter an integer")

def count_div_rules(ar,k):
    count = 0
    for x in ar:
        if not(x % k):
            count += 1
    return count;

def populate(a,b):
    ar = []
    for x in range(a,b+1):
        ar.append(x)
    return ar    


def find_divisible(a, b, k):
    ar = populate(a,b)
    count = count_div_rules(ar,k)    
    print("there are {} numbers in the array that is divisible by {}".format(count,k))

def ProblemB():
    ar = prompt()
    find_divisible(ar[0], ar[1], ar[2])



