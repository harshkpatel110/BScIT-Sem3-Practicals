import re
file=open("sample.txt","r")
text=file.read()
word=input("Enter word to search: ")
count=len(re.findall(word,text))
print("Occurrences =",count)
file.close()