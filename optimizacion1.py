import time

with open('books_published_last_two_years.txt') as f:
    recent_books = f.read().split('\n')
    
with open('all_coding_books.txt') as f:
    coding_books = f.read().split('\n')

print("This cell will take a while to run (30+ seconds)!")

# Con ciclos
start = time.time()
recent_coding_books = []

for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)

print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

# Con conjuntos
start = time.time()
recent_coding_books = set(coding_books).intersection(recent_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

# Con listas
start = time.time()
recent_coding_books = [x for x in coding_books if x in recent_books]
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))