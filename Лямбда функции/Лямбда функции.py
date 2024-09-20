def mult(a, b):
    return a * b


print(mult(10, 5))

# _______________________________


def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good Moning")

print(morning_greeting('Daniil'))
# Good Moning, Daniil!

evening_greering = greeting("Good Evening")

print(evening_greering('Daniil'))
# Good Evening, Daniil!

afternoon_greeting = greeting("Good Afternoon")

print(afternoon_greeting('Daniil'))
# Good Afternoon, Daniil!
