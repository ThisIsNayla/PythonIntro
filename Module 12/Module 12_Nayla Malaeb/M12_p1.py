# In the Module 12 slides, we learned how to process XML data that was entered as a string using 
# the triple quotes operator. However, it is more common to read XML data stored in a file. 
 
# Python's xml.etree.ElementTreemodule includes a parse() function that takes the name of an 
# XML file as an argument and returns a corresponding parse tree. A parse tree is a data structure 
# that Python uses to find data stored in XML format. The getroot() function returns the root of 
# the tree, which represents the starting point for extracting data using the find()function.
 
# The following shows how to print the data from the multiple XML node example assuming the 
# data is stored in the file "data.xml". Study this code and compare it to the code in the slides. A 
# copy of "data.xml" is available on the course web site for reference.

# import xml.etree.ElementTree as ET 

# tree = ET.parse("data.xml") 
# stuff = tree.getroot() 

# lst = stuff.findall("users/user") 
# print("User count:", len(lst)) 
# for item in lst: 
# 	print("Name:", item.find("name").text) 
# 	print("Id:", item.find("id").text) 
# 	print("Attribute:", item.get("x"))
	 
# Now that you have learned how to extract data from an XML file, we will look at a problem that 
# data scientists encounter daily. The XML file "europe.xml" contains data on 50 European 
# countries. In addition to a country's name, the data includes its area (in km2), capital city, 
# population, and gross domestic product (GDP) per capita in US dollars. 
 
# Write a Python program M12_p1.pythat reads the XML file and prints the top 10 European 
# economies and highest population densities, respectively. A country's economy is reported in 
# billions of US dollars and is the product of the GDP per capita by the population size. A country's 
# population density is the quotient of the population by the area. All results should be reported 
# to a precision of two decimal points.
 
# Example: 
# Top 10 Economies in Europe:
# <country>: <size of the 1st largest economy in billions of US dollars> 
# <country2>: <size of the 2nd largest economy in billions of US dollars> 
# <country3>: <size of the 3rd largest economy in billions of US dollars>
# ...
# Top 10 Population Densities in Europe:
# < country>: <1st largest population density in persons/km2> 
# < country>: <2nd largest population density in persons/km2> 
# <country3>: <3rd largest population density in persons/km2>
# …

import xml.etree.ElementTree as ET

tree = ET.parse("europe.xml")
root = tree.getroot()

countries = root.findall("country")

gdp_list = []
density_list = []

for country in countries:
	name = country.get('name', '')
	area = float(country.find('area').text)
	capital = country.find('capital').text
	population = float(country.find('population').text)
	gdppc = float(country.find('gdppc').text)

	gdp = gdppc * population / 1e9
	gdp_list.append((name, gdp))

	density = population / area
	density_list.append((name, density))

top_economies = sorted(gdp_list, key=lambda x: x[1], reverse=True)[:10]
top_densities = sorted(density_list, key=lambda x: x[1], reverse=True)[:10]

print("\nTop 10 Economies in Europe:")
for country in top_economies:
	print(f"{country[0]}: ${country[1]:.2f}B")

print("\nTop 10 Population Densities in Europe:")
for country in top_densities:
	print(f"{country[0]}: {country[1]:.2f}/km2")