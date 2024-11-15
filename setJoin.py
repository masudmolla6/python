# set1={"apple", "Orange", "lemon"}
# y = {1, 2, 3}
# mySet=set1.union(y)
# print(mySet)

# set1.update(y)
# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# newSet=set2.intersection(set1)
# newSet=set2 & set1
# set1.intersection_update(set2)
# print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3=set1.intersection(set2)
print(set3)

set6 = {"apple", "banana", "cherry"}
set7 = {"google", "microsoft", "apple"}
newSet2=set6-set7
set6.difference_update(set7)
set8=set6 ^ set7
set6.symmetric_difference_update(set7)
print(set6)
