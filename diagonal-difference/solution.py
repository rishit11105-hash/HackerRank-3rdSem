def diagonalDifference(arr):
    # Get the size of the square matrix.
    n = len(arr)

    # Store the sums of the two diagonals.
    primary_sum = 0
    secondary_sum = 0

    # Traverse the matrix once.
    for i in range(n):
        # Primary diagonal: arr[i][i]
        primary_sum += arr[i][i]

        # Secondary diagonal: arr[i][n - 1 - i]
        secondary_sum += arr[i][n - 1 - i]

    # Return the absolute difference between the two sums.
    return abs(primary_sum - secondary_sum)


# Read the size of the matrix.
n = int(input("Enter matrix size: "))

# Read the matrix.
arr = []

for i in range(n):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    arr.append(row)

# Calculate and display the answer.
result = diagonalDifference(arr)

print("Diagonal Difference:", result)