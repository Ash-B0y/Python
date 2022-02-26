# Python program to check if two strings
# are anagrams of each other

# Function to check whether two strings are anagram of
# each other


def anagram(str1, str2):
    # If two strings have different size
    if len(str1) != len(str2):
        return False

        # To store the xor value
    value = 0

    for i in range(0, len(str1)):
        value = value ^ ord(str1[i])
        value = value ^ ord(str2[i])
    return value == 0


# Driver code
str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
if anagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")