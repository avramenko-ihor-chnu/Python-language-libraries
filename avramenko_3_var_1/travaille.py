# Файл travaille.py: робота з БД
import dbm

db=dbm.open('persondb', 'r') # відкрити сховище **ЗАМІНИВ 'n' (створити нову) на 'r' (читання)
k=len(db) # у сховищі маємо три ‗рядки-записи‘
print(list(db.keys())) # keys – це заголовок
a=list(db.keys())
while k>0: # звернення до записів БД
    f1=db[a[k-1]].decode()
    print(f1); k-=1
print()
for key in db: # Ітерації, витягання, виведення
    print(key, '=>', db[key])
print()
for key in sorted(db):
    print(key, '=>', db[key]) # Ітерації через відсортований
    # список ключів
db.close() # закрити після внесення змін
