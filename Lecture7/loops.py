# Loops 
# Python has two primitive loop commands:
    # while loops
    # for loops

# While
values = 11
while values > 10:
    print(values)
    values -= 1

# for
data = [1,2,3,4,4,5,5,5,6,"true"]
for x in data:
    print(x)

# range(start,end,step)
for x in range(4):
    print(x)
    x -=1

# pass - inside empty loops
for x in range(4):
    pass

# nested loops
data1 = ["priya","tr","hyuio","true"]
for names in data1:
    for x in names:
        print(x)
    print("\n")

# if elif else break continue - statements can be used with loop statements