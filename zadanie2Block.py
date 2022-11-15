def f(a,s):
    block = [[] for i in range(len(a))]
    size = int(max(a)/len(a))+1
    for i in range(len(a)):
        block[a[i]//size].append(a[i])
    for i in range(len(block)-1,-1,-1):
        if len(block[i]) > 1:
            f(block[i],s)
        else: s += block[i]
    return s[::-1]
a = [1,4,56,7,403,563,0,465]
print(f(a,[]))