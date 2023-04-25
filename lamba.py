people = [
    {"name":"harry" , "house":"griffindor"},
    {"name":"bruce" , "house":"wayne manor"},
    {"name":"peter" , "house":"quohag"}
]
#telling the sort function to sort by name 


people.sort(key=lambda person: person["name"])
print(people)