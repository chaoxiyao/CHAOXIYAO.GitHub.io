text = input("请输入文字: ")
character_counts = {}

# Count the occurrences of each character
for char in text:
    if char in character_counts:
        character_counts[char] += 1
    else:
        character_counts[char] = 1

# Find characters that appear at least twice
repeated_characters = [char for char, count in character_counts.items() if count >= 2]

print("出现过两次的字: ", repeated_characters)
