import random
import string
adjectives = ['sleepy', 'slow', 'stinky', 'smelly', 'wet', 'hot', 'cold', 'warm', 'fat', 'yellow', 'green', 'red', 'blue', 'orange', 'fluffy', 'notfluffy', 'brave', 'sussy', 'floopy', 'sus']
nouns = ['apple', 'mom', 'dad', 'father', 'human', 'ball', 'dragon', 'panda', 'duck', 'peach', 'waterbottle', 'hammer', 'amongus']
print("Welcome to Password Maker")
print("Generating new password...")
adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(30, 10000)
special_char = random.choice(string.punctuation)
password = adjective + noun + str(number) + special_char
print('Your new password is: %s' % password)

