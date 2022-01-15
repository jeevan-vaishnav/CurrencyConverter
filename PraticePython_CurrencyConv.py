from ctypes.wintypes import PINT
from locale import currency


with open("currency.txt") as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]


amount = int(input("Enter amount:\n"))
print("enter the name of currency you want to convert this amount to? Available Options:\n :")
[print(item) for item in currencyDict.keys()]
currency = input("Enter enter of these values : \n")
print(
    f" {amount} INR is eqaul to  {amount * float(currencyDict[currency])} {currency} ")
