challenge1 = ["Thirty","Days","Of","Python"]
result1 =' '.join(challenge1)
print(result1)

challenge2 = ["Coding","For","All"]
result2 = ' '.join(challenge2)
print(result2)

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

result3 = company[0:6]
print(result3)

print(company.find("Coding"))
sub = "Coding"
print(company.index(sub))
print("Coding" in company)

print(company.replace("Coding", "Python"))
text = "Python for Everyone"
print(text.replace("Everyone", "All"))

print(company.split())
web = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(web.split(","))

First_character = company[0]
print(First_character)
print(len(company) - 1)
print(company[10])

text = "Python For Everyone"
acronym = text[0] + text[7] + text[11]
print(acronym)

print(company[0] + company[7] + company[11]) 

print(company.index("C"))
print(company.index("F"))

text2 = "Coding For All People"
print(text2.rindex("l"))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))
print(sentence.rindex("because"))

phrase = "because because because"
start = sentence.find(phrase)
end = start + len(phrase)
print(sentence[:start] + sentence[end:])

print(company.startswith("Coding"))
print(company.endswith("Coding"))

text3 = "   Coding For All      "

print(text3.strip())

challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge3 = 'thirty_days_of_python'
print(challenge3.isidentifier())

list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' # '.join(list1)
print(result)

print("I am enjoying this challenge.\n I just wonder what is next.")

print('Name\tAge\tCountry\tCity') 
print('Asabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
formatted_string = 'The area of a circle with radius %d is %.2f meters square.'%(radius,area)
print(formatted_string)

a=8
b=6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b }= {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')
