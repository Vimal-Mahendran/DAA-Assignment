def split_message(message, limit):
    parts = []
    total_parts = (len(message) + limit - 1) // limit
    for i in range(total_parts):
        start = i * limit
        end = min((i + 1) * limit, len(message))
        part = f"{message[start:end]}<{i+1}/{total_parts}>"
        parts.append(part)
    return parts

# Example 1
message1 = "this is really a very awesome message"
limit1 = 9
output1 = split_message(message1, limit1)
print(output1)

# Example 2
message2 = "short message"
limit2 = 15
output2 = split_message(message2, limit2)
print(output2)
