def dice_coefficient(set1, set2):
    intersection = len(set1.intersection(set2))
    dice = (2.0 * intersection) / (len(set1) + len(set2))
    return dice

# Example usage
set1 = {"The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"}
set2 = {"A", "quick", "brown", "dog", "jumps", "over", "the", "lazy", "fox"}

# Calculate Dice coefficient
dice_coef = dice_coefficient(set1, set2)

print(f"Dice Coefficient: {dice_coef}")
