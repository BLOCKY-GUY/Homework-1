name = input("Member name: ")
club = input("Club name: ")

member_number = 8
points = 9.5
is_active = True

print("Member Number:", member_number, "-> type:", type(member_number))
print("Points:", points, "-> type:", type(points))
print("Active:", is_active, "-> type:", type(is_active))

badge_code = name[0:3] + club[-1] + str(member_number)
print("Badge code:", badge_code)

print("===== CLUB BADGE =====")
print("Member: " + name)
print("Club: " + club)
print("Code: " + badge_code)
print("Points: " + str(points) + " | Active: " + str(is_active))