# MINI PROJECT: CONTACT BOOK

# STEP 1: Build the Contact Book Structure

contacts = [ {"name": "James Omondi", "phone": "0712345678", "skill": "welding", "city": "Nairobi"}, {"name": "Sandra Weru", "phone": "0723456789", "skill": "tiling", "city": "Mombasa",}, {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"}, {"name": "Grace Achieng", "phone": "075678901", "skill": "copywriting", "city": "Kisumu"}, {"name": "Brian Kamau", "phone": "0756789012", "skill": "upholstery", "city": "Nairobi"},]

print ("Contacts stored:", len (contacts))
print (contacts [0])

# STEP 2: Display All Contacts

contacts = [{"name": "James Omondi", "phone": "0712345678", "skill": "welding", "city": "Nairobi"}, {"name": "Sandra Weru", "phone": "0723456789", "skill": "tiling", "city": "Mombasa"}, {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"}, {"name": "Grace Achieng", "phone": "0745678901", "skill": "copywriting", "city": "Kisumu"}, {"name": "Brian Kamau", "phone": "0756789012", "skill": "upholstery", "city": "Nairobi"}]

print ()
print ("==== CONTACT BOOK ====")
for i, contact in enumerate (contacts): 
    print (f"\n{i+1}, {contact['name']}")
    print (f" Phone : {contact['phone']}")
    print (f" Skill : {contact ['skill']}")
    print (f" City : {contact ['city']}")

# STEP 3: Search for a Contact

contacts = [{"name": "James Omondi", "phone": "0712345678", "skill": "welding", "city": "Nairobi"}, {"name": "Sandra Weru", "phone": "0723456789", "skill": "tiling", "city": "Mombasa"}, {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"}, {"name": "Grace Achieng", "phone": "0745678901", "skill": "copywriting", "city": "Kisumu",}, {"name": "Brian Kamau", "phone": "0756789012", "skill": "upholstery", "city": "Nairobi"},]

search_name = "Grace Achieng"
found = False

(print)
for contact in contacts: 
    if contact["name"] == search_name:
        print ()
        print ("Contact found:")
        print (f" Name : {contact['name']}")
        print (f" Phone : {contact['phone']}")
        print (f" Skill : {contact['skill']}")
        print (f" City : {contact['city']}")
        found = True
        break

if not found: 
    print ("No contact found with name:", search_name)

# STEP 4: Search by City

contacts = [ {"name": "James Omondi", "phone": "0712345678", "skill": "welding", "city": "Nairobi"}, {"name": "Sandra Weru", "phone": "0723456789", "skill": "tiling", "city": "Mombasa"}, {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"}, {"name": "Grace Achieng", "phone": "07345678901", "skill": "copywriting", "city": "Kisumu"}, {"name": "Brian Kamau", "phone": "0756789012", "skill": "upholstery", "city": "Nairobi"},]

print ()
search_city = "Nairobi"
print (f"Contacts in {search_city}:")

for contact in contacts:
    if contact ["city"] == search_city:
        print (f"{contact ['name']} |{contact ['skill']} |{contact ['phone']}")

# STEP 5: Add a New Contact

contacts = [{"name": "James Omondi", "phone": "0712345678", "skill": "welding", "city": "Nairobi"}, {"name": "Sandra Weru", "phone": "0723456789", "skill": "teiling", "city": "Mombasa"},]

print ()
print ("Before:", len(contacts), "contacts")

# Add a new contact
new_contact = {
    "name": "Kevin Mwangi", 
    "phone": "0767890123", 
    "skill": "beekeeping", 
    "city": "Nakuru"}
contacts.append (new_contact)

print ("After:", len (contacts), "contacts")
print ("Last contact:", contacts [-1])

# FULL PROJECT: Put It All Together
# RUN THE FULL PROJECT

contacts = [
    {"name": "James Omondi",
    "phone": "0712345678",
    "skill": "welding",
    "city": "Nairobi"},
    {"name": "Sandra Weru",
    "phone": "0723456789",
    "skill": "tiling",
    "city": "Mombasa"},
    {"name": "Patrick Njiru",
    "phone": "0734567890",
    "skill": "phone repair",
    "city": "Nairobi"},
    {"name": "Grace Achieng",
    "phone": "0745678901",
    "skill": "copywriting",
    "city": "Kisumu"},
    {"name": "Brian Kamau",
    "phone": "0756789012",
    "skill": "upholstery",
    "city": "Nairobi"},
]

# Add one more contact
contacts.append ({
    "name": "Kevin Mwangi",
    "phone": "0767890123",
    "skill": "beekeeping",
    "city": "Nakuru"
})

# Display all contacts
print ()
print ("===== CONTACT BOOK =====")
for i, contact in enumerate (contacts):
    print (f"\n{i+1}. {contact ['name']}")
    print (f" Phone : {contact ['phone']}")
    print (f" Skill: {contact ['skill']}")
    print (f" City: {contact ['city']}")

# Search by city
print ("\n===== NAIROBI CONTACTS =====")
for contact in contacts: 
    if contact ["city"] == "Nairobi":
        print (f"{contact['name']} | {contact['skill']}")

# Summary
print (f"\nTotal contacts: {len(contacts)}")