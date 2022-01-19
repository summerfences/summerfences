# this program will tell you how old you are

print("Enter the year you were born: ")
year = input()

print("Press one if your birthday has passed this year: ")
bday = input()

if int(bday) == 1 :
    age = 2021 - int(year)

elif int(bday) != 1 :
    age = 2020 - int(year)

print(f"You are {age} years old.")
