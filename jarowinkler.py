def jaro_similarity(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    match_distance = max(len_s1, len_s2) // 2 - 1

    common_chars_s1 = []
    common_chars_s2 = []

    for i, char in enumerate(s1):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len_s2)

        if char in s2[start:end]:
            common_chars_s1.append(char)
            common_chars_s2.append(s2[start:end][s2[start:end].index(char)])

    m = len(common_chars_s1)
    if m == 0:
        return 0.0

    transpositions = sum(c1 != c2 for c1, c2 in zip(common_chars_s1, common_chars_s2)) // 2
    jaro_similarity = (m / len_s1 + m / len_s2 + (m - transpositions) / m) / 3
    return jaro_similarity


def jaro_winkler_similarity(s1, s2, p=0.1):
    jaro_sim = jaro_similarity(s1, s2)
    common_prefix_len = 0

    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 == c2:
            common_prefix_len += 1
        else:
            break

    jaro_winkler_sim = jaro_sim + (common_prefix_len * p * (1 - jaro_sim))
    return jaro_winkler_sim

string1 = "apple"
string2 = "applet"
jw_similarity = jaro_winkler_similarity(string1, string2)
print("Jaro-Winkler Distance:", 1-jw_similarity)
