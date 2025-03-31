import shelve
db = shelve.open("MyDB_made_with_shelve")
for key in db:
    print(key,"=>",db[key])
db.close()
