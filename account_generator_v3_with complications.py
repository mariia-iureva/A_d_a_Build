# your code goes here
import random

# hardcoded names in comment below
# names = ["ROSIE MARTA MARTINEZ", "JOE PETER LIU",	"SALLY SUE", "BOB JOHNSON", "DELIA AGHO"]
# empty list for names for user input
names = []
id_numbers = []
emails = []


# id generator function
def generate_id():
  r = random.randint(111111, 999999)
  return r

# a loop for requirement 2 that prompts the user for 5 names
for i in range(5):
  name = input("Please, enter first and last name: ")
  names.append(name)

# option for reading names from a file
# with open('C:/coding/ADA_build/names.txt') as f:
    # names = f.read().splitlines()

# create an id list with non duplicated items
for i in range(len(names)):
  number = 0
  id = generate_id() 
  if id not in id_numbers:
      id_numbers.append(id)

# create an emails list
for name, id in zip (names,id_numbers):
  # for the first name containing two words 
  # create a special list with each part of name as a separated item
    name_list = name.split()
    name_list_count = len(name_list)
  #  if a name list is bigger than 2 items, we need to create short name string
  # containing initials
    if name_list_count > 2:
      short_name = ""
      for n in name_list[0:2]:
        short_name = short_name + n[0]
      email = f"{short_name}{name.split()[-1]}{str(id)[3:]}@example.org"
  #  if a name contains two items (one name, one last name, than
  # there are no complications)
    else:
       email = f"{name[0]}{name.split()[-1]}{str(id)[3:]}@example.org"
    emails.append(email)

# final output
for i in range(len(names)):
  print(f"name: {names[i]}")
  print(f"id: {id_numbers[i]}")
  print(f"email: {emails[i]}\n")
  


