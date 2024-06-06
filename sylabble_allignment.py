import nltk
nltk.download("cmudict")
def get_syllables(word):
    syllables = []
    phones = nltk.corpus.cmudict.dict().get(word.lower())
    if phones:
        for phone_list in phones:
            syllables.extend(phone_list)
    return syllables

def align_syllables(word1, word2):
    syllables1 = get_syllables(word1)
    syllables2 = get_syllables(word2)

    min_len = min(len(syllables1), len(syllables2))
    
    alignment = list(zip(syllables1[:min_len], syllables2[:min_len]))

    return alignment

# Example usage:
word1 = "water"
word2 = "waiter"
alignment_result = align_syllables(word1, word2)

print(f"Syllable alignment between '{word1}' and '{word2}':")
for pair in alignment_result:
    print(f"{pair[0]:<10} {pair[1]:<10}")