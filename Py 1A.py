name = input("Enter your name: ")
age = int(input("Enter your age in years: "))
import datetime
year = datetime.datetime.now().year
if age<100:
    print(f"Hello {name}. You will turn 100 years old in the year {2026-age+100}.")
elif age==100:
    print(f"Hello {name}, you are 100 years old.")
elif age>100:
    print(f"Hello {name}, you already turned 100 years old {age-100} years ago.")