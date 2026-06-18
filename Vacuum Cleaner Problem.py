rooms = {"A":"Dirty", "B":"Dirty"}

for room in rooms:
    if rooms[room] == "Dirty":
        rooms[room] = "Clean"

print(rooms)
