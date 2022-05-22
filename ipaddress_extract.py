import re

file= open("C:\\Users\GODSON\Desktop\SPRING 2022\Sociology\Terminologies.txt", mode="r" , encoding= "utf-8")
#print(file.read())

pattern= re.compile("[0-9]{3}\.[0-9]{3}\.12[0-9]{1}\.[0-9]{3}")
matches= pattern.findall(file.read())
print(matches)