def compareTriplets(a, b):
    # Initialize scores for Alice and Bob.
    alice_score = 0
    bob_score = 0

    # Compare the three corresponding elements.
    for i in range(3):

        if a[i] > b[i]:
            # Alice gets one point.
            alice_score += 1

        elif a[i] < b[i]:
            # Bob gets one point.
            bob_score += 1

        # Equal values give no points.

    # Return Alice's score followed by Bob's score.
    return [alice_score, bob_score]


# Read Alice's scores.
a = list(map(int, input("Enter Alice's scores: ").split()))

# Read Bob's scores.
b = list(map(int, input("Enter Bob's scores: ").split()))

# Compare the scores.
result = compareTriplets(a, b)

# Display the result.
print("Alice's score:", result[0])
print("Bob's score:", result[1])