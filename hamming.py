def hamming_distance(str1, str2):
    # Make sure the strings are of equal length
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")

    # Calculate Hamming distance
    distance = sum(c1 != c2 for c1, c2 in zip(str1, str2))
    return distance

# Example usage:
string1 = "karate"
string2 = "karuse"

result = hamming_distance(string1, string2)
print(f"The Hamming distance between '{string1}' and '{string2}' is: {result}")