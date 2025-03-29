import dbm

from avramenko_3_var_1_step_5 import Audytoriya, Lekciyna, Computerna, Vykladatska
#    LEKCIYNA
lekciyna_301 = Lekciyna(301, 310)
lekciyna_302 = Lekciyna(302, 320)
lekciyna_303 = Lekciyna(303, 330)

#    COMPUTERNA
computerna_202 = Computerna(202, 220)
computerna_207 = Computerna(207, 270)
computerna_403 = Computerna(403, 430)

#    VYKLADATSKA
vykladatska_3 = Vykladatska(3, 30)

db = dbm.open("MyDB_made_wiht_dbm", 'n')
for object in (lekciyna_301,lekciyna_302,lekciyna_303,computerna_202,computerna_207,computerna_403,vykladatska_3):
    print(object)
    db[object.nomer]=str(object)
print(len(db))
db.close
