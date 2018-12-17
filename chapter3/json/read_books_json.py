
import json

with open("books.json", "rt") as file:
    books = json.load(file)
	
print(books)

print(type(books))



    
