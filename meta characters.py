import re
pattern = r"colo.r"

if re.match(pattern,"colour"):
    print("match1")

pattern = r"^colo.r$"

if re.match(pattern,"colour"):
    print("match2")

pattern = r"a*"

if re.match(pattern,"colour"):
    print("match3")

pattern = r"a+"

if re.match(pattern,"acolour"):
    print("match4")

pattern = r"[a-z][A-Z][0-9]"

if re.match(pattern,"cA6olour"):
    print("match5")

pattern = r"[aeiou]"

if re.match(pattern,"a6olour"):
    print("match6")