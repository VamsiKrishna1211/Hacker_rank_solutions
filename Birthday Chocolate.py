
#Uncomment the below for custom input

#n = int(input().strip())

#s = list(map(int, input().rstrip().split()))

#d,m = map(int, input().rstrip().split())

def birthday(n, s, d, m):
    ans=0
    for i in range(0,n):
        if(sum(s[i:i+m])==d):
            ans+=1
    return ans
#start of test Cases

#Test case 1
#result = 0
n=6
s=[1, 1, 1, 1, 1, 1]
d,m=map(int, [3, 2])
print("test case 1")
print(birthday(n,s,d,m))

#Test case 2
#result = 2
n=5
s=[1, 2, 1, 3, 2]
d,m=map(int, [3, 2])
print("Test case 2")
print(birthday(n,s,d,m))

