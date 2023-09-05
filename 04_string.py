name = "Nicolas"
last_name = 'Molina Monroy'
print(name)
print(last_name)

full_name = name +" "+ last_name
print(full_name)

quote = "I'm Nicolas"
print(quote)

quote2 = 'she said "Hello"'
print(quote2)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1',template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3',template)

age = 24
final_template = f"Hola mi nombre es {name}, mi apellido es {last_name} y mi edad es {age}"
print(final_template)