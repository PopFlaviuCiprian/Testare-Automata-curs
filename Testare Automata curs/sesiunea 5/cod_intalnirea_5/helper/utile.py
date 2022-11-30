def say_hi_name(name):
    print(f"Hi! My name is {name}")

# cand functia va fi apelata, in acest caz se poate apela si fara age
# iar age va lua by default valoarea 15
def say_hi_name_and_age(name, age=15):
    print(f"Hi! My name is {name} and I'm {age} years old")