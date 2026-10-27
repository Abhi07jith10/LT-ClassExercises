# Write a function that accepts a total number of seconds and returns the equivalent hours, minutes, and
# remaining seconds.
# Example: 3,725 seconds → 1 hour, 2 minutes, 5 seconds.

def convert_seconds(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")

convert_seconds(3725)  # 1 hour(s), 2 minute(s), 5 second(s)
