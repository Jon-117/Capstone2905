import datetime


# Part 1

current_month_text = datetime.date.today().strftime('%B')
print(current_month_text)

name = input("What is your name? \n")
print(f"Hello, {name}! There are {len(name)} letters in your name.")
birthmonth = input("What is your birth month?\n")

if birthmonth == current_month_text:
    print(f"Happy birthmonth, {name}!")
