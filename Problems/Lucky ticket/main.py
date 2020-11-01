# Save the input in this variable
ticket = (input())
a = int(ticket[0])
b = int(ticket[1])
c = int(ticket[2])
d = int(ticket[-1])
e = int(ticket[-2])
f = int(ticket[-3])

# Add up the digits for each half
half1 = [a + b + c]
half2 = [d + e + f]

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
