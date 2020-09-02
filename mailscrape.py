import re
text = "sangeeth1-23sj@gmail.com random  alan@gmail.net string"

pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

result = pattern.search(text)
result = pattern.findall(text)

print(result)

