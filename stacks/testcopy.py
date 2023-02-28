
x = input()
print("using just input method", x)
print("using just input method", x.split())
mylist= list(map(int, x.split()))

# 2 5 9 3 1 12 6 8 7
# print("Sys arguments", sys.argv[1])
# print("Sys arguments", sys.argv[1])

# for i in range(0, len(mylist), -1): -- incorrect
#     print(mylist[i])
# print("outside")

for i in range(len(mylist)-1,-1, -1):
    print(mylist[i])
print("outside")

input_list= list(map(int, input().split()))
mystack = list()
nge = list()
# initialize nge as we need directly access later indexes
for i in range(0, len(input_list)):
    nge.append(i)

print("printing tthe nge list")
for i in range (0, len(nge)):
    print(nge[i])
