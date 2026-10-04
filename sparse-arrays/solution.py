from collections import Counter


def matchingStrings(stringList, queries):
    # Count how many times each string occurs.
    frequency = Counter(stringList)

    # Find the frequency of every query.
    # Counter returns 0 if the query does not exist.
    return [frequency[query] for query in queries]


# Read the number of strings.
n = int(input("Enter number of strings: "))

# Read the strings.
stringList = []

for i in range(n):
    stringList.append(input(f"Enter string {i + 1}: "))

# Read the number of queries.
q = int(input("Enter number of queries: "))

# Read the queries.
queries = []

for i in range(q):
    queries.append(input(f"Enter query {i + 1}: "))

# Calculate the frequencies.
results = matchingStrings(stringList, queries)

# Display the results.
print("Frequencies:")

for result in results:
    print(result)