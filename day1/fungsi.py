smallest = None
print("Before:", smallest)
for itervar in [43, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
print(parts)

word = "bananana"
i = word.find("na")
print(i)