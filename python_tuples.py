import math


# Calculate the area and circumference of a circle

radius = input("Enter the Radius \n")

r = int(radius)

# Circumference
c = round(2 * math.pi * r,4)

# area
a = round(math.pi * r ** 2,4)

mydimentions = list((c,a))

# for item in mydimentions:
	# print(item)

for i in range(len(mydimentions)):
	print(mydimentions[i])