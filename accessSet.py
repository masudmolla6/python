# access item

thisset = {"apple", "banana", "cherry"}

print("apple" not in thisset)

# add item
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = ["apple", "banana", "cherry"]
tropical = {"pineapple", "mango", "papaya"}

tropical.update(thisset)
print(tropical)
