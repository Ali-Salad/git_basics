name = "Hodan"
age = 22
city = "oslo"
course = "python"
paid = True 

print("name:" + name)
print(f"Age:{age}")
print(f"city:{city}")
print(f"course:{course}")
print(f"paid:{paid}")

user inputs 
Age = int(input("how old are you:"))
print(f"you are {Age} years old")
print(Age + 1)

chalange 2
price = 10
quantity= int(input("how many cases ?"))
subtotal = price * quantity
tax_percentage = 25 / 100
tax = subtotal * tax_percentage
total = subtotal + tax

print(f"subtotal:{subtotal}")
print(f"tax 25% :{tax}")
print(f"total :{total}")

pizza_price = 10 
drink_price = 5
pizza_quantity = 3
drink_quantity = 2
tip_percentage =10 / 100 
pizza_total = pizza_price * pizza_quantity
drink_total = drink_price *drink_quantity
subtotal = pizza_total +drink_total
tip = subtotal * tip_percentage
total = subtotal+ tip

print(f"pizzas:{pizza_total}")
print(f"dinks:{drink_total}")
print(f"tip 10% :{tip}")
print(f"total:{total}")

name = "Alisalad"
print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize())

message = "i study css"
print(message.replace("css", "python"))

city = "     hargeysa      "
print(city.strip())


state = "hiiraan"
print(state[0])

print(state.find("l"))
print(state.find("n"))

print(city.count("a"))
print(name.count("b"))
print(message.count("s"))
print(state.count("a"))

# chalange 3
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




























