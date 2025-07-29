# wordlist_generator.py

import itertools

chars = input("Enter base characters (like abc123): ")
min_length = int(input("Enter minimum password length: "))
max_length = int(input("Enter maximum password length: "))

filename = "wordlist.txt"
with open(filename, "w") as f:
    for length in range(min_length, max_length + 1):
        for combo in itertools.product(chars, repeat=length):
            f.write(''.join(combo) + '\n')

print(f"\nWordlist saved as {filename}")
