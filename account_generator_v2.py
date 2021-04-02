# your code goes here
import random

names = ["ROSIE MARTINEZ", "JOE LIU",	"SALLY SUE", "BOB JOHNSON", "DELIA AGHO"]
id_numbers = []
emails = []
short_ids = []

def generate_id():
  r = random.randint(111111, 999999)
  return r


for name in names:
  id = generate_id()
  id_numbers.append(id)

for name, id in zip (names,id_numbers):
    email = f"{name[0]}{name.split()[1]}{str(id)[3:]}@example.org"
    emails.append(email)


for i in range(len(names)):
  print(f"name: {names[i]}")
  print(f"id: {id_numbers[i]}")
  print(f"email: {emails[i]}\n")