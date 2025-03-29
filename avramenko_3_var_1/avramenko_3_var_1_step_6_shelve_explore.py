import shelve
db = shelve.open("MyDB")
for key in db:
    print(key,"=>",db[key])
db.close()
