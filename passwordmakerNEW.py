import random
import string

# Define lists of adjectives and nouns
adjectives = ['sleepy', 'slow', 'stinky', 'smelly', 'wet', 'hot', 'cold', 'warm', 'fat', 'yellow', 'green', 'red', 'blue', 'orange', 'fluffy', 'notfluffy', 'brave', 'sussy', 'bright', 'dark', 'heavy', 'light', 'smooth', 'rough', 'soft', 'hard', 'quick', 'slow', 'sharp', 'dull', 'strong', 'weak', 'tall', 'short', 'old', 'new']
nouns = ['Apple', 'Mom', 'Dad', 'Father', 'Human', 'Ball', 'Dragon', 'Panda', 'Duck', 'Peach', 'Waterbottle', 'Hammer', 'Gentle', 'Harsh', 'Clear', 'Cloudy', 'Clean', 'Dirty', 'Tiny', 'Huge', 'Brave', 'Cowardly', 'Smart', 'Dumb', 'Friendly', 'Hostile', 'Loud', 'Quiet', 'Happy', 'Sad', 'Fresh', 'Stale', 'Shiny', 'Dull', 'Graceful', 'Clumsy', 'Bitter', 'Sweet', 'Warm', 'Cool', 'Rich', 'Poor', 'Cat', 'Dog', 'House', 'Car', 'Tree', 'Book', 'Chair', 'Table', 'Phone', 'Computer', 'Window', 'Door', 'Flower', 'River', 'Mountain', 'Beach', 'City', 'Village', 'Road', 'Bridge', 'School', 'Office', 'Market', 'Store', 'Garden', 'Forest', 'Desert', 'Lake', 'Ocean', 'Island', 'Park', 'Museum', 'Library', 'Stadium', 'Hotel', 'Restaurant', 'Airport', 'Train', 'Bus', 'Bicycle']

print("Welcome to Password Maker")

# Get user inputs
num_adjectives = int(input("How many adjectives? "))
num_nouns = int(input("How many nouns? "))
num_numbers = int(input("How many numbers? "))
num_punctuation = int(input("How many punctuation marks? "))

# Generate password components
password = ''.join(random.choice(adjectives) for _ in range(num_adjectives))
password += ''.join(random.choice(nouns) for _ in range(num_nouns))
password += ''.join(str(random.randint(0, 9)) for _ in range(num_numbers))
password += ''.join(random.choice(string.punctuation) for _ in range(num_punctuation))

print('Your new password is: %s' % password)

