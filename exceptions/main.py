# Exception - ZeroDivisonError, kad skaitli dala uz 0
#skaitlis = 5 / 0
#print(skaitlis)

# piemers manis definetajam Exception
class InvalidAgeException(Exception):
    "Tiek izsaukts, kad ievaditais skaitlis mazaks par 18"
    pass
number = 18
try:
    input_num = int(input("Ievadi skaitli: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Pilngadigs")
        
except InvalidAgeException:
    print("Iznenums: neatbilstosais vecums")