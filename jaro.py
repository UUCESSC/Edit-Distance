from math import floor, ceil

# Jaro Similarity of two s
def jaro_distance(s1, s2):
	
	# If the s are equal
	if (s1 == s2):
		return 1.0

	# Length of two s
	len1 = len(s1)
	len2 = len(s2)

	# Maximum distance upto which matching
	# is allowed
	max_dist = floor(max(len1, len2) / 2) - 1

	# Count of matches
	match = 0

	# Hash for matches
	hash_s1 = [0] * len(s1)
	hash_s2 = [0] * len(s2)

	# Traverse through the first
	for i in range(len1):

		# Check if there is any matches
		for j in range(max(0, i - max_dist), 
					min(len2, i + max_dist + 1)):
			
			# If there is a match
			if (s1[i] == s2[j] and hash_s2[j] == 0):
				hash_s1[i] = 1
				hash_s2[j] = 1
				match += 1
				break

	# If there is no match
	if (match == 0):
		return 0.0

	# Number of transpositions
	t = 0
	point = 0

	for i in range(len1):
		if (hash_s1[i]):

			# Find the next matched character
			# in second
			while (hash_s2[point] == 0):
				point += 1

			if (s1[i] != s2[point]):
				t += 1
			point += 1
	t = t//2

	# Return the Jaro Similarity
	return (match/ len1 + match / len2 +
			(match - t) / match)/ 3.0

# Driver code
s1 = "martha"
s2 = "marhta"

# Prjaro Similarity of two s
print(1-round(jaro_distance(s1, s2),6))

