def levenshtein_distance(str1, str2):
    m, n = len(str1), len(str2)

    # Initialize a matrix to store distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1, # Deletion
                dp[i][j - 1] + 1, # Insertion
                dp[i - 1][j - 1] + cost # Substitution
            )

    # The bottom-right cell contains the Levenshtein distance
    return dp[m][n]

# Example usage:
string1 = "kitten"
string2 = "sitting"

result = levenshtein_distance(string1, string2)
print(f"The Levenshtein distance between '{string1}' and '{string2}' is: {result}")

