# Program that that reads the XML file "europe.xml" and prints the top 10 European economies 
# and highest population densities, respectively. 
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut


import xml.etree.ElementTree as ET

tree = ET.parse("europe.xml")
data = tree.getroot()

lst = data.findall("country")
   
country = dict()
for item in lst:
   area = float(item.find("area").text)
   capital = item.find("capital").text
   population = float(item.find("population").text)
   gdppc = float(item.find("gdppc").text)
   economy = population * gdppc
   popdensity = population/area
   dataList = [area, capital, population, gdppc, economy, popdensity]
   country[item.get("name")] = dataList
   
econSize = list()
density = list()
for k, v in list(country.items()):
   econSize.append((v[4],k))
   density.append((v[5],k))
   
econSize.sort(reverse=True)
density.sort(reverse=True)

print("\nTop 10 Economies in Europe:")
for i in range(10):
   print(f"{econSize[i][1]}: ${econSize[i][0]/1000000000.0:.2f}B")
   
print("\nTop 10 Population Densities in Europe:")
for i in range(10):
   print(f"{density[i][1]}: {density[i][0]:.2f}/km2")