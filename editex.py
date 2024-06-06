def editex_distance(s1, s2, substitution_cost=1, transposition_cost=1):
    m, n = len(s1), len(s2)

    # Initialize the distance matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the matrix using dynamic programming
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                cost = 0 if s1[i-1] == s2[j-1] else substitution_cost
                dp[i][j] = min(dp[i-1][j] + 1,           # Deletion
                               dp[i][j-1] + 1,           # Insertion
                               dp[i-1][j-1] + cost)      # Substitution

                if i > 1 and j > 1 and s1[i-1] == s2[j-2] and s1[i-2] == s2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-2][j-2] + transposition_cost)  # Transposition

    return dp[m][n]

# Example usage
word1 = "kitten"
word2 = "sitting"

distance = editex_distance(word1, word2)
print(f"Editex Distance between '{word1}' and '{word2}': {distance}")
