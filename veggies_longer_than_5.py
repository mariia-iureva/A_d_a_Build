#first option
veggies = ["carrot", "yam", "zucchini", "spinach"]
for i in range(len(veggies)):
  if len(veggies[i]) > 5:
    print(f"I love {veggies[i]}")


#second option
veggies = ["carrot", "yam", "zucchini", "spinach"]

for veggie in veggies:
  if len(veggie) > 5:
    print(f"I love {veggie}")
# your code goes here