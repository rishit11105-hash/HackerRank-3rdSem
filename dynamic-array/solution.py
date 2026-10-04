def dynamicArray(n, queries):
    # Create n empty sequences.
    sequences = [[] for _ in range(n)]

    # Stores the result of the previous type-2 query.
    last_answer = 0

    # Store all type-2 query results.
    answers = []

    # Process every query.
    for query in queries:
        query_type, x, y = query

        # Determine which sequence should be accessed.
        index = (x ^ last_answer) % n

        if query_type == 1:
            # Append y to the selected sequence.
            sequences[index].append(y)

        elif query_type == 2:
            # Select an element from the selected sequence.
            sequence = sequences[index]

            # Calculate the required position.
            last_answer = sequence[y % len(sequence)]

            # Store the result.
            answers.append(last_answer)

    return answers


# Read n and the number of queries.
n, q = map(int, input("Enter n and number of queries: ").split())

# Read all queries.
queries = []

for i in range(q):
    query = list(map(int, input(f"Enter query {i + 1}: ").split()))
    queries.append(query)

# Process the queries.
results = dynamicArray(n, queries)

# Display the results.
print("Answers:")

for answer in results:
    print(answer)