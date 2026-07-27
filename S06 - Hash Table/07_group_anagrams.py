def group_anagrams(words):
    """
    Group anagrams using a hash table keyed by the sorted string.

    - For each word, compute its canonical key by sorting characters.
    - Insert the word into the dictionary under that key.
    - Return all grouped lists.

    Time: O(N * K log K)
    Space: O(N * K)
    """
    groups = {}  # key: sorted string, value: list of anagrams

    for w in words:
        key = "".join(sorted(w))  # canonical key
        if key not in groups:
            groups[key] = []
        groups[key].append(w)

    return list(groups.values())


# Declaring variable values
if __name__ == "__main__":
    words = ["eat", "ant", "tea", "tan", "abt", "ate", "nat", "bat", "tab"]

    # Canonical sorted keys for each word
    print(f"Canonical sorted keys for each word:")
    for w in words:
        key = "".join(sorted(w))
        print(f"{w} → {key}")

    # Test Instantiation
    print("\nInput:", words)
    print("\nGrouped anagrams:")

    result = group_anagrams(words)
    for group in result:
        print(group)


# Expected Output

# Canonical sorted keys for each word:
# eat → aet
# ant → ant
# tea → aet
# tan → ant
# abt → abt
# ate → aet
# nat → ant
# bat → abt
# tab → abt

# Input: ["eat", "ant", "tea", "tan", "abt", "ate", "nat", "bat", "tab"]

# Grouped anagrams:
# ['eat', 'tea', 'ate']
# ['ant', 'tan', 'nat']
# ['abt', 'bat', 'tab']
