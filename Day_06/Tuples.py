# Create an empty tuple
empty_tuple = ()

# Tuple containing names of sisters and brothers
sisters = ("Anu", "Meera")
brothers = ("Arjun", "Rahul")

# Join brothers and sisters
siblings = brothers + sisters
print("My siblings:", siblings)

# Number of siblings
print("Number of siblings:", len(siblings))

# Add father and mother
family_members = siblings + ("Father", "Mother")
print("Family members:", family_members)