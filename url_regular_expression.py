import re

file= open("C:\\Users\GODSON\Desktop\SPRING 2022\Sociology\Terminologies.txt", mode="r" , encoding= "utf-8")
#print(file.read())


pattern = re.compile("https?://[a-z[^ ]+.com")
matches = pattern.findall(file.read())
print(matches)
