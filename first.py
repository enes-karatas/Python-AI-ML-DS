# -*- coding: utf-8 -*-
"""first.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lpIM6_6qSLZvlgk_106fVrQj5a58HATC
"""

print('Hello again world')

2+4

print("Hey , this is our new python experience",4,'you')
print("Hey , this is our new python experience "+str(4)+' you')

print('Python is more'+'functional then java')
print('Python is more '+'functional then java')

price = 750;
brand = "Apple";
color = "Silver";
print("Price for the" ,brand,"is",price)
print("Colour for the"+brand+"is"+color)
print("Colour for the "+brand+" is "+color)

phone_price = 1100;
pc_price = 2249.99;
total_price = phone_price+pc_price;
print('Total cost for your shop is',total_price)

#List

brand_list = ['Apple', 'Razer','Toyota','Casio','Samsung'];
print(brand_list)

print('Hey','python')
print('Hey','python',sep='')

print('hey '+str(7))

brand='Lexus';
price= 32000;
print('Price of the ',brand,'car is',str(price))

is_correct= True
print(is_correct)

print(type(is_correct))
print(type(brand))

apple_device_price = 1000
discount_rate = 0.3

price_with_discount = apple_device_price - apple_device_price*discount_rate
print('$'+str(price_with_discount))

# List are storage in Python similar to Java
# We use [ ] to define lists

brand_list = ["apple",'razer',"toyota",'rolex','mercedes ']
price_list = [ 1100,2300, 22000, 45000,200, 3300]

print('Brand List : ',brand_list)
print('Price List : ',price_list)
print('1111111111111111')
print(len(brand_list))
print('Max price in the list is :' , max(price_list), "and minimum price in the list is :",min(price_list))
print('2222222222222222')
print(brand_list[1])
print(brand_list[0:2])
print(price_list[2:5])
print('33333333333333')
print(price_list[2:6])
print(price_list[2:7]) # even though we go beyond the list length we can see the all elements from begining point to the end
print(price_list[2 : len(price_list)-1]) # By using len function I can go to end of the list in proper way
print(price_list[-1]) # to be able to see last element of the list we simply put -1 so we reach to the end of the list
print('4444444444444')


brand_list.pop(-1) # .pop() removes the item from list with given index inside, with -1 here last item was removed from list which is mercedes
print(brand_list)
brand_list.pop(2) # list already lost last item above, now it lost index 2 item which is toyota
print(brand_list)

brand_list.append('audi') # .append() add items to the list , it will be added to the end of the list automatically
print(brand_list)

brand_list[1] = 'boeing' # I can re-assign any value in the list by specifying its index, in here 2nd element became boeing from razer, item will be replaced no shifting in the list
print(brand_list)

# Tuple is also storage place like list but its immutable, its defined and fixed at the begining, not strectable like list, Its very similar to Array in Java
# We use ( ) to define Tuples

storage = (32,64,128,256)
print(storage)
print(type(storage))
print(storage[2]) # we can also reach specific items in Tuple by giving its index

# storage[2]=44 = this will give an error because Tuples are immutbale and we cannot rech and delete its items like we did in lists

mix = [22,34,"enes"] # we can put different types of data in same list
print(mix)

# Dictionaries are like Map in java, we store items in key,value format
# We use { } to define Dict

newDict = {'brand':'Apple' , 'price':300 , 'RAM (in GB)' : 128 , "Storage (in TB)" : 1}
print(newDict)
type(newDict)
print('-------------')
# Keys are unique like in Java
# We call key to see value as below

print(newDict['price'])

# We can do re-assignment value to  Values in dict  dsdsdsdds
newDict['brand'] = "Samsung"

print(newDict)

#print(brand_list)

# We can add list as a value as below
newDict = {'brand':brand_list , 'price':300 , 'RAM (in GB)' : 128 , "Storage (in TB)" : 1}
print(newDict)

print('-------------------')

# To be able to see keys and values we have .keys() .values() functions in Python

print(newDict.keys())
print(newDict.values())

print('-------------------')

# To be able to reach one of the values we can give index, see below
print(newDict['brand']) # gonna be ['apple', 'boeing', 'rolex', 'audi']
print(newDict['brand'][2]) # gonna be rolex

# We can update the value with .update() function , .update( {key : new value} )
newDict.update({'price':700})
print(newDict)
print('(++++++++)')

# We can also remove items with .pop() in Dictionary
newDict.pop('RAM (in GB)') # 'RAM (in GB)' key removed from dict with her values
print(newDict)

# if - else

cost = 3000
budget = 10000

if cost < budget:
  print('Affordable')
elif cost > budget: # Make sure there is no space before elif, it gives an error idk why lol
    print('Not affordable')

# We can use input to take values from user

inputed_budget = int(input("Enter your budget please : "))

cost = 1000

if inputed_budget >= cost:
  print("Program affordable")
elif inputed_budget< cost:
  print("Program NOT affordable")
else:
    print("Error")

#print(type(inputed_budget))

# To be able to check if the user put not a int value we have below logic

inputed_budget = input("Enter your budget please: ")

try:
    inputed_budget = int(inputed_budget)
except ValueError:
    print('Enter a valid number')
    exit()

cost = 1000

if inputed_budget >= cost:
    print("Program affordable")
elif inputed_budget < cost:
    print("Program NOT affordable")
else:
    print("Error")

# Note from AI

# The code you provided seems mostly correct, but there's a logic issue with the condition for checking if the inputted budget is an integer. Let me explain:
# In Python, when you use input() function, it always returns a string. Therefore, even if the user enters a number, it will be received as a string.
# Then you try to convert this string to an integer using int(). However, if the user enters something that can't be converted to an integer (like letters),
# it will raise a ValueError before the if statement is executed, so the condition type(inputed_budget) != int won't ever be true.

inputed_budget = int(input("Enter your budget please : "))

cost = 1000

if type(inputed_budget) != int :
 print('Enter a valid number')

if inputed_budget >= cost:
  print("Program affordable")
elif inputed_budget< cost:
  print("Program NOT affordable")
else:
    print("Error")

memory = int(input("Enter the memory : "))

if memory == 32:
  print('Price is $700')
elif memory == 64:
  print('Price is $900')
else:
  print("We only have 32GB and 64GB options")

# range() function returns immutable sequence of numbers

print(range(6))

print(list(range(6))) # 0 dan 6 ya kadar yazdir

print(list(range(2,6))) # 2 den 6 ya kadar yazdir

print(list(range(2,16,4))) #2 den 16 ya 4 er arttir

# for

# for iterator_var in sequence
#     statements(s)
newList = []
newList2 = []

for i in range(0,10,1): # its like for(i=0, i<10, i++) in Java, start from 0 to the 10 and increased by 1
  newList.append(i)

for j in range(0,10,2):
  newList2.append(j)

  print(newList)
  print(newList2)

# Lets create a price list with discounts

price = 900

for discount_rate in range(0,21,5):

    discounted_price = price * (discount_rate/100)

print("Price with ",discount_rate,"discount is ",discounted_price)

# Lets create a price list with discounts

price = 900

for discount_rate in range(0,21,5):

    discount = price * (discount_rate/100)

    discounted_price = price - discount
    print("Price with ",discount," discount is ",discounted_price)

"""VERY IMPORTANT NOTE

Looks like python is very sensitive about line positioning both in x and y axis, to be able to feel like stay in the parantesys stay in same line
Check above codes, almost same codes will give you different output
"""

# Lets create a price list with discounts with While Loops

price = 900

i = 5

while i<=20:

    discount = price * (i/100)

    discounted_price = price - discount
    print("Price with ",discount," discount is ",discounted_price)

    i+=5 # incrementin i with 5, i = i + 5

sum = 0

for i in range(1,5):
    sum = sum + i
print(sum)

# List Comprehensions

discounted_price_list = [700,800,750,300]
within_budget = []

budget = int(input("Enter your budget in dollars : "))

for i in discounted_price_list: # We're iterating in discounted_price_list
  if i <= budget: # if entered price is less than budget then we can afford it, Yes
    within_budget.append("Yes")
  else:  # Else we cannot afford it , No
    within_budget.append("No")

print(within_budget)

"""We can put above implementation in different way in very less lines, its beautiful, check below"""

# List Comprehensions

discounted_price_list = [700,800,750,300]

new_budget = int(input("Enter your budget in dollars : "))

within_budget_new = ["Yes" if i <= new_budget else "No" for i in discounted_price_list]
# We put for loop and if condition inside of the empty list(within_budget_new ),
# once loop executed list is started to fill inside, amazing!!

print(within_budget_new)

"""**Writing a Functions**"""

# In Python we can create our own functions , its like methods in Java

# write a function

def display_iphone_attributes():

  """
  This function displays
  the stored attributes of
  the Apple iPhone
  """

  # store the pricec in dollars (in dollars) of the mobile in variable 'price'
  price = 900
  # store the RAM (in GB) of the mobile in variable 'ram'.
  ram = 4
  #store the internal storage (in GB) og the mobile in variable 'storage'.
  store = 128
  #display the details
  print(
      "The Apple iPhone has ",
      ram,
      " GB RAM and ",
      store,
      " GB internal storage and it costs $",
      price,
      sep="",
  )

# To be able to call functions we simply call their name with paranthesis

display_iphone_attributes()

# Lets make our function more dynamic (method variables in Java)

def display_iphone_attributes_with_input(brand, price, ram, storage):

  """
  This function displays
  the stored attributes of
  the Apple iPhone
  """

  print(
      "The ", brand ," has ",
      ram,
      " GB RAM and ",
      storage,
      " GB internal storage and it costs $",
      price,
      sep="",
  )

display_iphone_attributes_with_input("samsung",880, 64, 1024)

# Lets wrote a new function with return value

def dis_price(discount):
  """
  This function takes the discount
  percentage as input and
  returns the discounted price of an Apple iPhone
  """

  price = 900
  discounted_price = price - price * (discount/100)
  #return to discounted price
  return discounted_price

dis_price(10)
print(dis_price(10)) # Basically does 10% discount to 900

# WE can assign to function to variable Since we retun the value at the end of the function, thats powerful
dp_20 = dis_price(20)
print(dp_20)
#Basically does 10% discount to 900

# Lambda function

# Put some stuff here to explain Lambda

def say(message, times):
  print(message*times)

say("hi",2)

# args and kwargs
# arg -> arguments
# kwargs -> keyword arguments
# Note : args should be defined before kwargs, kwargs once parametre olarak verilirse python hata veriyor

def total_amount (price1, price2, price3, price4, price5):
  total = price1 + price2 + price3 + price4 + price5

  return total


# Args Python da guclu bir olay, mesela normalde java da herhangi bir parametre kullanmak istedigimizde yukaridaki gibi
# method parameters kismina tek tek koymamiz gerekir
# Python da args kullanarak bunu esnek girisli yapabiliyoruz , mesela asagida oldugu gibi parameter kismina *args koyuyoruz
# ve args icin bir for loop yaratiyoruz, boylece parametre ici esnek oluyor. ister 2 ister 150 tane parametre koyalim dinamik olarak kabul ediyor
def total_amount_with_args(*args):

  total_args = 0 # total_args a basta deger atamazsak hata veriyor, int mi string mi anlamiyor sanirim ve loop a sokamiyor
  for args in args:
    total_args+=args

  return total_args

print(total_amount(1,2,3,4,5))

print(total_amount_with_args(1,2,3))

def total_price (*args_total_prices):
  total_price_new = 0
  for args_TOTAL in args_total_prices:
    total_price_new += args_TOTAL

  return total_price_new

tax_rate = 0.07

print(total_price(1,2,3,4,5,6))
print("Total price is :",total_price(1,2,3,4))
print("Total amount of this shop is :",total_price(700,850,1249,449,270),"+ tax")
#print("Tax rate :",tax)
print("Total amount of this shop + tax is :",total_price(700,850,1249,449,270)+total_price(700,850,1249,449,270)*tax_rate)

# We can add other parameter next to args but we should call them by their name once we wanna use them, see below
# We also should put *args first while defining function before other parameters, otherwise python will give an error

def total_price (*args_total_prices , discount=0.0):
  total_price_new = 0
  for args_TOTAL in args_total_prices:
    total_price_new += args_TOTAL

  return total_price_new - discount

tax_rate = 0.07

print("Total amount with discount is : ", total_price(100,200,300,discount=49))

def customer_net_spend(*prices,discount=0.0,**kwargs):

  total = 0

  for price in prices:
    total+=price

  total_discounted_price = total - discount - kwargs["cashback"]
  # Burada kwargs i dictionary(map) olarak atadik,

  net_spend = total_discounted_price - kwargs["cashback"]

  return net_spend

additionals = {"cashback":5}
#additional dictionary si ile cashback key'ine 5 value'sunu atadik
print(
    "Customer net spent (during last day of 5 seasons):",
    customer_net_spend(700,599,600,discount=0.05,**additionals)
)

def order_summary(*prices, **additionals):
  """
  This function takes the prices of phones ordered
  and any other cost additions/subtractions ,
  and returns the total amount , net spend,
  and reward points earned for the others.
  """

  total = 0;

  for price in prices:
    total += price

  net_spend = total - additionals["discount"] * additionals["cashback"]


  if total >= 10000:
    reward_points = 300
  elif total >= 5000:
    reward_points = 200
  elif total >= 2000:
    reward_points = 100
  else:
    reward_points = 0

  # in Python we can return multiple things
  # Python returns this values as Tuple
  return total, net_spend , reward_points

additionals = {"discount":0.05 , "cashback":5}

# We can return multiple objects in Python and we can store them in multiple objects as well

tt, ns, rp = order_summary(700,599,750,**additionals)
print(

      "Customer order summary:\n",
      "\nTotal amount:",
      tt,
      "\nTotal discounted amount:",
      ns,
      "\nReward points earned:",
      rp,
)

"""Notes:

Note : args should be defined before kwargs, kwargs once parametre olarak verilirse python hata veriyor

def fun(A, B=30), in here Argument A is positional arguments but Argument B has a default value specified, so it is a keyword argument.

"""

