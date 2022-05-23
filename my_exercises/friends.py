# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to `nearby_friends.txt`

friends = input('Input 3 friends separated by space: ').split()
f = open('people.txt', 'r')
people = f.read().splitlines()
f.close()
nearby = [friend for friend in friends if friend in people]

f = open('nearby_friends.txt', 'w')
for friend in nearby:
    print(f'Your nearby friend: {friend}')
    f.write(friend+'\n')
f.close()
