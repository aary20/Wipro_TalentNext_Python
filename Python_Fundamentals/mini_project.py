
# Mini Project 1
'''
Create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
Sample Output:
How far would you like to travel in miles? 2500
I suggest Super-Car to your destination
'''

distance = int(input("Distance you want to travel in miles:" ))

if distance < 3:
    print("You can ride a bicycle.")
elif distance > 3 and distance < 300:
    print("You can use a motorcycle.")
else:
    print("I suggest Super-Car to your destination")
    

# Mini Project 2
'''
Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour.
you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
Write a python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How much days can I operate one server with $918?
'''

hourly_charges = 0.51

daily_cost = hourly_charges * 24
weekly_cost = daily_cost * 7
monthly_cost = daily_cost * 30

budget = 918
days_operated = budget / daily_cost

print(f"Cost to operate one server per day: ${daily_cost}")
print(f"Cost to operate one server per week: ${weekly_cost}")
print(f"Cost to operate one server per month: ${monthly_cost}")
print(f"Days I can operate one server with $918: {days_operated:.2f} days")