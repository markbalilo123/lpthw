
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 50)

def my_func(num1, num2):
	print(f"my num is {num1} my num2 is {num2}")
	print("Awitize!")

my_func(1762, 288.0)

n1 = 76
n2 = 829

my_func(n1, n2)
my_func(n1 + n2, n2 + n1)
my_func(n1 + 70, n2 + 84)

my_func("Awituze", 78)
my_func("Awitufuu", "ajjsjsj")
my_func(272827267727272728/2+7, 82727272727/2+7)

my_func(181888.90, 82261266.7)

my_func(n2/n1, n1/n2)
m = "loweer"
h = "higher"
my_func(m + h, h + m)
