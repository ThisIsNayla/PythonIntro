# Program reads the file "temperatures.txt" and prints the date and the minimum, maximum, 
# and average temperatures. 
# 
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

dict = {}

try:
   file = open("temperatures.txt")
except:
   print("File open error.")
   exit()
   
date = file.readline()

for i in file:
   # Extract time value
   time = int(i[0:2])
   # Extract temperature value
   temp = float(i[i.find(",")+1:])
   # Add time, temperature to dictionary
   dict[time] = temp

# Create list of night-time temperatures
pm = []
for i in range(0,7,1):
   pm.append(dict[i])

for i in range(20,24,1):
   pm.append(dict[i])

# Find lowest temperature
low = min(pm)

# Create list of day-time temperatures
am = []
for i in range(7,20,1):
   am.append(dict[i])

# Find highest temperature
high = max(am)

# Find average temperature
avg = sum(dict.values())/len(dict)

# Display results
print(date, end="")
print("Temp. Low =",low)
print("Temp. High =", high)
print(f"Temp. Avg. = {avg:.1f}")