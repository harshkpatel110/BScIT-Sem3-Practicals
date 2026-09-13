def starts_with(text,ch):
    return text.startswith(ch)
thestring=input("Enter a string: ")
character=input("Enter a character to check if the above string starts with it: ")
if starts_with(thestring,character):
    print(f"The string \"{thestring}\" starts with the character '{character}'.")
else:
    print(f"The string \"{thestring}\" does not start with the character '{character}'.")
#OR:
check_starts_with = lambda text, ch: text.startswith(ch)
thestring=input("Enter a string: ")
character=input("Enter a character to check if the above string starts with it: ")
if(check_starts_with(thestring,character)):
    print(f"The string \"{thestring}\" starts with the character '{character}'.")
else:
    print(f"The string \"{thestring}\" does not start with the character '{character}'.")