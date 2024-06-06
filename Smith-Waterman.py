def smith_waterman(sequence1, sequence2, match_score=2, mismatch_score=-1, gap_penalty=-1):
    # Initialize the scoring matrix with zeros
    matrix = [[0] * (len(sequence2) + 1) for _ in range(len(sequence1) + 1)]

    # Fill in the scoring matrix
    for i in range(1, len(sequence1) + 1):
        for j in range(1, len(sequence2) + 1):
            match = matrix[i-1][j-1] + (match_score if sequence1[i-1] == sequence2[j-1] else mismatch_score)
            delete = matrix[i-1][j] + gap_penalty
            insert = matrix[i][j-1] + gap_penalty
            matrix[i][j] = max(0, match, delete, insert)

    # Find the maximum score in the matrix
    max_score = 0
    max_i, max_j = 0, 0
    for i in range(len(sequence1) + 1):
        for j in range(len(sequence2) + 1):
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_i, max_j = i, j

    # Trace back to find the local alignment
    alignment1, alignment2 = '', ''
    i, j = max_i, max_j
    while i > 0 and j > 0 and matrix[i][j] > 0:
        current_score = matrix[i][j]
        diagonal = matrix[i-1][j-1]
        up = matrix[i-1][j]
        left = matrix[i][j-1]

        if current_score == diagonal + (match_score if sequence1[i-1] == sequence2[j-1] else mismatch_score):
            alignment1 = sequence1[i-1] + alignment1
            alignment2 = sequence2[j-1] + alignment2
            i -= 1
            j -= 1
        elif current_score == up + gap_penalty:
            alignment1 = sequence1[i-1] + alignment1
            alignment2 = '-' + alignment2
            i -= 1
        elif current_score == left + gap_penalty:
            alignment1 = '-' + alignment1
            alignment2 = sequence2[j-1] + alignment2
            j -= 1

    return alignment1, alignment2

# Example usage
sequence1 = "AGCACACA"
sequence2 = "ACACACTA"

alignment1, alignment2 = smith_waterman(sequence1, sequence2)
print("Sequence 1:", alignment1)
print("Sequence 2:", alignment2)
