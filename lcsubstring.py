def LCSubStr(X, Y, m, n):

	LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

	# To store the length of
	# longest common substring
	result = 0

	# Following steps to build
	# LCSuff[m+1][n+1] in bottom up fashion
	for i in range(m + 1):
		for j in range(n + 1):
			if (i == 0 or j == 0):
				LCSuff[i][j] = 0
			elif (X[i-1] == Y[j-1]):
				LCSuff[i][j] = LCSuff[i-1][j-1] + 1
				result = max(result, LCSuff[i][j])
			else:
				LCSuff[i][j] = 0
	return result


# Driver Code
X = 'GeeksforGeeks'
Y = 'GeeksQuiz'

m = len(X)
n = len(Y)

print('Length of Longest Common Substring is',
	LCSubStr(X, Y, m, n))


