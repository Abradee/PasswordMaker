import random
import string



adjectives = ['sleepy', 'slow', 'stinky', 'smelly', 'wet', 'hot', 'cold', 'warm', 'fat', 'yellow', 'green', 'red', 'blue', 'orange', 'fluffy', 'notfluffy', 'brave', 'sussy' 'bright', 'dark', 'heavy', 'light', 'smooth', 'rough', 'soft', 'hard', 'quick', 'slow', 'sharp', 'dull', 'strong', 'weak', 'tall', 'short', 'hot', 'cold', 'old', 'new']


nouns = ['Apple', 'Mom', 'Dad', 'Father', 'Human', 'Ball', 'Dragon', 'Panda', 'Duck', 'Peach', 'Waterbottle', 'Hammer', 'Gentle', 'Harsh', 'Clear', 'Cloudy', 'Clean', 'Dirty', 'Tiny', 'Huge', 'Brave', 'Cowardly', 'Smart', 'Dumb', 'Friendly', 'Hostile', 'Loud', 'Quiet', 'Happy', 'Sad', 'Fresh', 'Stale', 'Shiny', 'Dull', 'Graceful', 'Clumsy', 'Bitter', 'Sweet', 'Warm', 'Cool', 'Rich', 'Poor', 'Cat', 'Dog', 'House', 'Car', 'Tree', 'Book', 'Chair', 'Table', 'Phone', 'Computer', 'Window', 'Door', 'Flower', 'River', 'Mountain', 'Beach', 'City', 'Village', 'Road', 'Bridge', 'School', 'Office', 'Market', 'Store', 'Garden', 'Forest', 'Desert', 'Lake', 'Ocean', 'Island', 'Park', 'Museum', 'Library', 'Stadium', 'Hotel', 'Restaurant', 'Airport', 'Train', 'Bus', 'Bicycle']


print("Welcome to Password Maker")


adjective = random.choice(adjective)
noun = random.choice(nouns)
number = random.randrange(0, 1000)
special_char = random.choice(string.punctuation)
password = adjective + noun + str(number) + special_char


print('Your new password is: %s' % password)

