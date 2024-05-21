import os
print("Welcome to my calendar calculator. ")
def days_in_month(year, month):
    no_of_days = 0 
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                for days in month_days:
                    if month == 2:
                        no_of_days = 29
                    elif month in [4, 6, 9, 11]:
                        no_of_days = 30
                    else:
                        no_of_days = 31
                return f"{year} is a leap year with {no_of_days} days in {month}."
            else:
                for days in month_days:
                    if month == 2:
                        no_of_days = 28
                    elif month in [4, 6, 9, 11]:
                        no_of_days = 30
                    else:
                        no_of_days = 31
                return f"{year} is not a leap year with {no_of_days} days in {month}."
        else:
            for days in month_days:
                if month == 2:
                    no_of_days = 29
                elif month in [4, 6, 9, 11]:
                    no_of_days = 30
                else:
                    no_of_days = 31
            return f"{year} is a leap year with {no_of_days} days in {month}."
    else:
        for days in month_days:
            if month == 2:
                no_of_days = 28
            elif month in [4, 6, 9, 11]:
                no_of_days = 30
            else:
                no_of_days = 31
        return f"{year} is not a leap year with {no_of_days} days in {month}"
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
range_of_year = list(range(1, 10000))
range_of_month = list(range(1, 13))
check_calender = False
while not check_calender:
    year = int(input("Enter a year: "))
    proceed = False
    while not proceed: 
        if year in range_of_year:
            proceed = True
        else:
            prompt1 = input("Please enter a correct input for the year: ")
            year = int(prompt1)
    month = int(input("Enter a month: "))
    step_2 = False
    while not step_2:
        if month in range_of_month:
            step_2 = True
        else:
            prompt2 = input("Please enter the correct month in the range of 1 to 12 only: ")
            month = int(prompt2)
    calender = days_in_month(year, month)
    print(calender)
    check_again = input("Do you still want to check another date? answer 'yes' or 'no': ")
    if check_again == 'no':
        check_calender = True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
       
