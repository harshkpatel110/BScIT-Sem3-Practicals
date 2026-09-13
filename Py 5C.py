def starts_with(text, ch):
    return text.startswith(ch)
string=input("Enter a string: ")
character=input("Enter a character: ")
if starts_with(string, character):
    print("The string starts with", character)
else:
    print("The string does not start with", character)
#OR:
check_starts_with = lambda text, ch: text.startswith(ch)
string_value = input("Enter a string: ")
character = input("Enter a character: ")
print(check_starts_with(string_value, character))