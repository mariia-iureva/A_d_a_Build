
print ("Welcome to our very special Mad movie rental. Please input some information below.")
"""
Our Madlib program takes several words as an input from user and replaces original words in famous movie titles and descriptions
"""
# taking user input and storing it in variables. We'll be reusing all of them in different sentences below.
name = input("Please, enter your name:")
adjective = input("an adjective:")
time = input("your favorite time of day:")
color = input("your favorite color:")
animal = input("the funniest animal:")
relative = input("the wisest family member:")
number = input("your lucky number:")
country = input("country for next vacation:")

print(f"Dear {name.capitalize()}, we’re very happy to have you here. \nIn Mad Movie Rental we use your subconsciousness and imagination to help you choose a movie \nthat will be a {adjective} fit for your {time}.\n\nIf you like bright colors, we can recommend:\n")
print(f"1) Men in {color.capitalize()} (1997), - adventures of secret agents from top secret government bureau \nthat interacts with alien civilizations.\n2) {color.capitalize()} Riding Hood (2011), - a little girl’s walk through the dark scary forest \nand a horrible {color} {animal} chasing her on her way to her {relative}’s.\n3) {number} shades of {color}(2015) – a very romantic one where a girl meets a boy \nand they play with each other in the {color} room\n")
print(f"If you are more into animals, try our selection:\n")
print(f"1) {animal.capitalize()}man(2022), dark avenger and his butler fight evil in Gotham city.\n2) The {animal} of Wall Street (2013), - actually no animals involved, just money and lots of trading.\n3) Kungfu – {animal.capitalize()} (2008) – it’s about one brave {animal} learning Kunfu with his friends.\n")
print("If you prefer mistic numbers try these:\n") 
print(f"1) {number} billboards outside Ebbing, Missouri (2017) - A {relative} personally challenges the local authorities \nto solve the family member's murder.\n2) {number} angry men (1957) – {number} jurors decide the fate of an accused young man.\n3) The {number} Musketeers (2011) -  The {adjective}-headed young D'Artagnan along with {number} Musketeers \nmust unite to save the throne of {country} and prevent the war in Europe.\n")
print(f"Thank you, {name.capitalize()}, for playing with us!")

