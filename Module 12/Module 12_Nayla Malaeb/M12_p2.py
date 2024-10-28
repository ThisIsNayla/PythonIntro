import json

with open('gutendex.json', 'r', encoding='utf-8') as file:
    info = json.load(file)

with open('books.txt', 'w', encoding='utf-8') as book_file:
    for book in info['results']:
        book_id = book['id']
        title = book['title']
        author = book['authors'][0]['name'] if book['authors'] else 'Unknown Author'
        downloads = book['download_count']
        url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"

        book_file.write(f'Title: "{title}"\n')
        book_file.write(f'Author: {author}\n')
        book_file.write(f'Downloads: {downloads}\n')
        book_file.write(f'URL: {url}\n\n')
    book_file.close()    

books_file_path = 'books.txt'  

with open(books_file_path, 'r', encoding='utf-8') as book_file:
    for line in book_file:
        ascii_line = line.encode('ascii', 'ignore').decode()
        print(ascii_line, end='')    
book_file.close()