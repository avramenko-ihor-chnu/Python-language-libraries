import dbm

db = dbm.open("MyDB_made_wiht_dbm", 'r')
print(list(db.keys()))
db_keys = list(db.keys())
# for i in db_keys:
#     print(db[i])
for i in db_keys:
    print(db[i].decode())
