import pymongo 

dbclient = pymongo.MongoClient("mongodb://<user>:<password>@<hostname>:<port>/")

breach2019 = dbclient["breach2019"]
users = breach2019["users"]

users.drop() 
users = breach2019["users"]

breach_file = open("Finland.txt")

i = 0

for line in breach_file:
    line_splitted = line.split(':')
    
    user = {
        "phone": line_splitted[0],
        "fb": line_splitted[1],
        "first_name": line_splitted[2],
        "last_name": line_splitted[3],
        "gender": line_splitted[4],
        "homeplace": line_splitted[5],
        "birthplace": line_splitted[6],
        "other2": line_splitted[7],
        "other3": line_splitted[8],
        "other4": line_splitted[9],
        "other5": line_splitted[10],
        "other6": line_splitted[11]
    }
    users.insert_one(user)

    i += 1
    print("Lisätty:", i/1381569,"Nro:", i)
