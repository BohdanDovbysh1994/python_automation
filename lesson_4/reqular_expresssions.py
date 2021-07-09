import re

text = """John Dow marta Stuard
href="https://pythonru.com/primery/primery-primeneniya-regulyarnyh-vyrazheniy-v-python"

asdl;fkja;sdkjf

So
La
Bla

Names {name: John, age: 23}

    """

print(re.findall("[A-Za-z]+", text))
