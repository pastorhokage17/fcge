#Function missing_int(A) is defined on line 41

def prompt():
    print("Problem A: Given an array A of N integers, write a function missing_int(A)\nthat returns the smallest positive integer\n(greater than 0) that does not occur in A.\n")
    try:
        n = int(input("Enter N number of integers: "))
        a = []
        for x in range(n):
            a.append(int(input("[{}] >> ".format(x+1))))
        print("Your array:", a)
        return a    
    except:
        print("Please enter an integer")


#create a new set to compare with the input
def completeset(ar):
    _min=min(ar)
    _max=max(ar)
    if _max < 0:
        return ar
    if _min < 0:
        p = set()
        for x in ar:
            if x > 0:
                p.add(x)
        _min=min(p)
        _max=max(p)
    
    q = set()
    for x in range(_min,_max+1):
        q.add(x)
    return q

#get the elements missing from first array
def arr_subtract(a,b):
    if a == 0 or b == 0:
        return 0
    c = b&(b^a)
    return c if len(c) > 0 else max(a)

#problem A solution:
def missing_int(A):
    if A == 0:
        output = 1;
    else:
        output = min(A) if type(A) is set else A+1
    print("Smallest integer missing: ", output)

def ProblemA():
    a = set(prompt())
    b = arr_subtract(a,completeset(a))
    missing_int(b)