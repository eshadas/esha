fruits=["apple","banana","cherry"]
print(fruits)
z=fruits.count("cherry")
print(z)
print(type(z))
fruits.update("apple")
fruits.remove("banana")
print(fruits)
fruits.add("orange")
fruits.append("orange")
print(fruits)
print(len(fruits))
fruits.insert(1, "mango")
print(fruits)
for x in fruits:
    print(x)
if "apple" in fruits:
    print("yes, 'apple' is in the fruits list")
 

