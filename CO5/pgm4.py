# write a programme to read specific columns of a given csv file and print the content of the column

import csv

header = ["place", "name", "age"]
with open("city.csv", "w") as file:
    write = csv.DictWriter(file, fieldnames=header)
    write.writeheader()
    write.writerow({"place": "malappuram", "name": "murshid", "age": 21})
    write.writerow({"place": "perinthalmanna", "name": "lijas", "age": 26})
    write.writerow({"place": "elamkulam", "name": "vaishnav", "age": 22})
    write.writerow({"place": "kaliakav", "name": "niranjan", "age": 19})
with open("city.csv", "r") as file:
    read = csv.DictReader(file)
    n = input("Enter the column name you want(place,name,age):")
    for i in read:
        print(i[n])
