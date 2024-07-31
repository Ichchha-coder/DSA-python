def search(lits,n):
    i=0
    while i<len(list):
        if list[i]==n:
            return True
        i=i+1
    return False

list=[3,6,7,1,2]
n=4
if search(list,n):
    print("Found")
else:
    print("Not found")