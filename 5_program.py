l=["Harry","Soham","Sachin","Rahul"]
search_string="Soham"

if search_string.lower() in [item.lower() for item in l]:
    print("Found")
else:
    print("Not Found")