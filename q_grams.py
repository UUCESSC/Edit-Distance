def generate_qgrams(string, q):
    qgrams = []
    for i in range(len(string) - q + 1):
        qgram = string[i:i+q]
        qgrams.append(qgram)
    return qgrams

def find_common_qgrams(string1, string2, q):
    qgrams1 = generate_qgrams(string1, q)
    qgrams2 = generate_qgrams(string2, q)
    
    common_qgrams = set(qgrams1) & set(qgrams2)
    
    return common_qgrams

# Example usage:
string1 = "example"
string2 = "ample"
q = 2
result = find_common_qgrams(string1, string2, q)
print(f"Common {q}-grams between '{string1}' and '{string2}': {result}")