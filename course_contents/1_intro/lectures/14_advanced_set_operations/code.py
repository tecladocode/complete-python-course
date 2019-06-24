art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

# -- Difference --
# Gives you members that are in one set but not the other.

art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)

print(art_but_not_science)
print(science_but_not_art)

# -- Symmetric difference --
# Gives you those members that aren't in both sets
# Order doesn't matter with symmetric_difference

not_in_both = art_friends.symmetric_difference(science_friends)

print(not_in_both)

# -- Intersection --
# Gives you members of both sets

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

# -- Union --
# Gives you all members of all sets, but of course without duplicates

all_friends = art_friends.union(science_friends)
print(all_friends)
