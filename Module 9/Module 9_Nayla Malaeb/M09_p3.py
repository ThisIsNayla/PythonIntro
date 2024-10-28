# 	3. The file temperatures.txt contains temperature readings over a 24-hour period. 
# The first line contains a date, and the remaining 24 lines contain the time expressed in 24-hour 
# format and the corresponding measured temperature separated by a comma.
	
# Write a program M9_p3.py that reads temperatures.txt and prints the date and the minimum, maximum, 
# and average temperatures. Your program must use a dictionary. The minimum temperature should be 
# calculated from temperatures gathered from 0:00 to 06:00 and 20:00 to 23:00, respectively. 
# The maximum temperature should be calculated from temperatures gathered from 7:00 to 19:00. 
# A sample temperatures.txt file is provided on the course web site for reference.

# Example: 
# Sunday, July 10, 2022 
# Temp. Low = 24.0 
# Temp. High = 30.0 
# Temp. Avg. = 26.7

with open("temperatures.txt", "r") as file:
    lines = file.readlines()
    date = lines[0].strip()
    temperatures = [float(line.split(',')[1].strip()) for line in lines[1:]]

low = temperatures[0:6] + temperatures[20:24]
high = temperatures[7:20]

print(date)
print(f"Temp. Low = {min(low):.1f}")
print(f"Temp. High = {max(high):.1f}")
print(f"Temp. Avg. = {sum(temperatures) / len(temperatures):.1f}")