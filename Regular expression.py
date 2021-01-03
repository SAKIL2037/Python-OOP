import re

pattern = r"Colour"
text = "Red is a Colour, I love red Colour"
if re.match(pattern,text):
    print("Match")
else:
    print("No Match")

if re.search(pattern, text):
    print("Match")
else:
    print("No Match")

print(re.findall(pattern,text))

match = re.search(pattern,text)

if match:
    print(match.start())
    print(match.end())
    print(match.span())

print(re.sub(pattern,"color",text))
print(re.sub(pattern,"color",text,count=1))

