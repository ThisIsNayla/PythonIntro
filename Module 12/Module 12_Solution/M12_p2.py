# Program that that reads the file "gutendex.json", extracts information about a book's title,
# author, downloads, and URL, and save it to "books.txt"
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

import json

file = open("gutendex.json")
info = json.load(file)

bookFile = open("books.txt","w")

lst = info["results"]

for i in lst:
   id = str(i["id"])
   title = i["title"]
   author = i["authors"][0]["name"]
   downloads = i["download_count"]
   url = "https://www.gutenberg.org/files/"+id+"/"+id+"-0.txt"
   
   bookFile.write(f"Title: \"{title}\"\n")
   bookFile.write(f"Author: {author}\n")
   bookFile.write(f"Downloads: {downloads}\n")
   bookFile.write(f"URL: {url}\n\n")
   
file.close()
bookFile.close()