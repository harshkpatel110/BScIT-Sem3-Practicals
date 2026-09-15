import re
file=open("sample.html","r")
html=file.read()
links=re.findall(r'href="(.*?)"',html)
for link in links:
    print(link)
file.close()