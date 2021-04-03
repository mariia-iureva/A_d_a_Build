# your code goes here
import random

# hardcoded names in comment below
# names = ["ROSIE MARTA MARTINEZ", "JOE PETER LIU",	"SALLY SUE", "BOB JOHNSON", "DELIA AGHO"]
# empty list for names for user input


student_data = []

# names = []
id_numbers = []
# emails = []

# id generator function
def generate_id():
  r = random.randint(111111, 999999)
  return r

for i in range(5):
  one_student_dict = {
    "name": None,
     "id": None,
     "email": None,
  }
  # prompts the user for 5 names
  name = input("Please, enter first and last name: ")
  one_student_dict["name"] = name
  # generate id, add new id to an id list to check duplicates, add id to dictionary
  id = generate_id()
  if id not in id_numbers:
    id_numbers.append(id)
    one_student_dict["id"] = id
  #create email
  # for the first name containing two words 
  # create a special list with each part of name as a separated item
  name_list = name.split()
  #  if a name list is bigger than 2 items, we need to create short name string
  # containing initials
  if len(name_list) > 2:
      short_name = ""
      for n in name_list[0:2]:
        short_name += n[0]
      email = f"{short_name}{name.split()[-1]}{str(id)[3:]}@example.org"
  #  if a name contains two items (one name, one last name, than
  # there are no complications)
  else:
    email = f"{name[0]}{name.split()[-1]}{str(id)[3:]}@example.org"
  one_student_dict["email"] = email
  student_data.append(one_student_dict)


# final output
for i in range(len(student_data)):
  print(student_data[i])
  

