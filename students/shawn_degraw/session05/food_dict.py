food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

# Step 1
print("{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta".format(**food_prefs))

# Step 2
listcomp = [ {num, hex(num)} for num in range(16) ]
print(listcomp)

# Step 3
dictcomp = { num: hex(num) for num in range(16) }
print(dictcomp)

# Step 4
newdict = { samekey: food_prefs[samekey].count("a") for samekey in food_prefs }
print(newdict)

# Step 5a
s2 = { value for value in range(21) if not value % 2 }
s3 = { value for value in range(21) if not value % 3 }
s4 = { value for value in range(21) if not value % 4 }

print(s2)
print(s3)
print(s4)

# Step 5b
divisors = set([ 2, 3, 4 ])

trytwolist = [{value for value in range(21) if not value % divisor} for divisor in divisors]

print(trytwolist)