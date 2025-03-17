print ("===================")
print ("Showing Odd Number Series")
print ("===================")
print ("")
# input from user to determine maximum number of series
n = int(input("Please input maximum value of series = "))
x = 0
i = 1 # looping
while i <= n:
# print the result on console
    print (i)
# set odd number for next iteration
i += 2
# calculate number of series
x += 1
print ("Number of Series ", x)