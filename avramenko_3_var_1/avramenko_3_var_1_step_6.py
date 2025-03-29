from avramenko_3_var_1_step_5 import Audytoriya, Lekciyna, Computerna, Vykladatska
#    LEKCIYNA
lekciyna_1 = Lekciyna(1, 10)

#    COMPUTERNA
computerna_2 = Computerna(2, 20)

#    VYKLADATSKA
vykladatska_3 = Vykladatska(3, 30)
import shelve
db = shelve.open("MyDB")
for object in (lekciyna_1,computerna_2,vykladatska_3):
    db[object.name] = object
db.close()
