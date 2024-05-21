def format_name(first_name, last_name):
    return f"my name is {first_name.title()} {last_name.title()}"

print(format_name(input("Enter your first name: "), input("Enter last name: ")))