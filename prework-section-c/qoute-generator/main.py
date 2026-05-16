#!/bin/env/python
#a list of qoutes
import random
qoutes = [
        ("Imagination is more important than knowledge", "Albert Einstein"),
        ("I have a dream", "Martin Luther King"),
        ("It always seems impossible until it's done.", "Nelson Mandella"),
        ("Stay hungry, Stay foolish", "Steve Jobs"),
        ("Float like a butterfly, sting like a bee", "Muhammad Ali"),
        ("Be the change that you wish to see in the world", "Mahatma Gandhi"),
        ("Government of people, by the people, for the people", "Abraham Lincoln"),
        ("It does not matter how slowly you go as long as you do not stop", "Confucius"),
        ("I came, I saw, I conquered", "Julius Caesar")
        ]
qoute = random.choice(qoutes)

print(f"{qoute[0]} --{qoute[1]}")

