
# Kevin Chen
# 13/09/17
# chatbot.py
# to make a chatbot which can answer some basic questions

person = input("Hello there! My name is Kbot. What is your name ?")

print('hello', person, "it is great to meet you.")

where = input("Where are you from?")

print(where, "feel like an amazing city to live in.", "my lucky number is 6")

number = input("What's your favourite number?")

print("wow,", number, "is so close to my lucky number")

car = input("I want to buy a car, can you give me a suggestion?")

print(car, "that's sounds like a good suggestion!")

price = float(input("how much does it cost?"))

rate = float(input("What is a reasonable yearly interest rate on a beautiful car like that?"))

years = float(input("if you had to take out a loan to buy the car, how many years would you take the loan out for?"))

monthly_rate = rate/100/12

monthly_payment = (monthly_rate*price)/(1-((1+monthly_rate)**-12*years))

print(monthly_payment)
