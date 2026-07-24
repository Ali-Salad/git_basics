# # # # chalange 1
# # # calculating rikaab tax driver 
# # tax_drivers = 20
# # cars =20
# # daily_rent = 10
# # Total_tax_cost = cars * daily_rent
# # print(cars)
# # print(daily_rent)
# # print(Total_tax_cost)

# # # chalange 2
# # a = 2
# # b = 4
# # c = a*b
# # print(a*b)

# # chalange 3
# name = "abdurahman"
# print(len(name))
# print(name.count("a"))
# print(name.find("1"))
# print(name.upper())
# print(name.lower())
# print(name.capitalize())

# chalange 4
name = input ("enter your name:")
hours = int(input("enter your hours :"))
rate= float(input("enter your rate :"))

print(f"Employee:{name}")
print(f"Hours:{hours}")
print(f"Rate:{rate}/hrs")


gross_pay = hours * rate;
print(f"gorss_pay:{gross_pay}")
tax_percentage = 22 / 100
tax= gross_pay * tax_percentage
print(f"tax 22%:{tax} ")

net = gross_pay - tax
print(f"net:{net}")