# -- Defining sets --

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

# -- Adding to a set --

art_friends.add("Jen")

print(art_friends)

# -- No duplicate items --

art_friends.add("Jen")

print(art_friends)  # Same as before, "Jen" was not added twice

# -- Removing from a set --

science_friends.remove("Charlie")

print(science_friends)
