def timeConversion(s):
    # Extract AM or PM from the end of the string.
    period = s[-2:]

    # Extract and convert the hour to an integer.
    hour = int(s[:2])

    if period == "AM":
        # 12 AM becomes 00 in 24-hour format.
        if hour == 12:
            hour = 0

    else:
        # For PM, add 12 unless the hour is already 12.
        if hour != 12:
            hour += 12

    # Keep minutes and seconds unchanged.
    # Format the hour using two digits.
    return f"{hour:02d}{s[2:-2]}"


# Read the 12-hour time.
time = input("Enter time in 12-hour format: ")

# Convert and display the result.
result = timeConversion(time)

print("24-hour format:", result)    