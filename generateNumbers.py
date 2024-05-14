import random

# Generate 1000 random integers between 0 and 4999
requests = [random.randint(0, 4999) for _ in range(1000)]

# Write the requests to input.txt
with open('generateNumbers.txt', 'w') as file:
    for request in requests:
        file.write(f"{request}\n")
