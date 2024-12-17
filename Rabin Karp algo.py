def rabin_karp(text, pattern, prime=101):
    """Rabin-Karp string matching algorithm."""
    n = len(text)
    m = len(pattern)
    pattern_hash = 0
    text_hash = 0
    h = 1  # h will be pow(d, m-1) % prime

    d = 256  # Number of characters in the input alphabet

    # Compute the value of h = (d^(m-1)) % prime
    for i in range(m - 1):
        h = (h * d) % prime

    # Compute the initial hash values for the pattern and first window of text
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if the current hash values of pattern and text match
        if pattern_hash == text_hash:
            # Check for character match (to avoid false positive)
            if text[i:i + m] == pattern:
                print(f"Pattern found at index {i}")

        # Compute the hash value for the next window of text
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime

            # We might get negative values, convert it to positive
            if text_hash < 0:
                text_hash = text_hash + prime


def kmp_search(text, pattern):
    """Knuth-Morris-Pratt string matching algorithm."""
    n = len(text)
    m = len(pattern)

    # Preprocess the pattern to create the LPS array
    lps = [0] * m
    j = 0  # index for pattern

    compute_lps(pattern, m, lps)

    i = 0  # index for text
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def compute_lps(pattern, m, lps):
    """Helper function to compute the LPS (longest prefix suffix) array."""
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def boyer_moore(text, pattern):
    """Boyer-Moore string matching algorithm."""
    n = len(text)
    m = len(pattern)

    # Preprocess the pattern to create the bad character heuristic table
    bad_char = [-1] * 256

    for i in range(m):
        bad_char[ord(pattern[i])] = i

    shift = 0
    while shift <= n - m:
        j = m - 1

        # Keep reducing j while characters of pattern and text match
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        # If the pattern is present at current shift, print the index
        if j < 0:
            print(f"Pattern found at index {shift}")

            # Shift the pattern to align the next character in text
            shift += (m - bad_char[ord(text[shift + m])] if shift + m < n else 1)
        else:
            # Shift the pattern such that the bad character in text aligns with the last occurrence in pattern
            shift += max(1, j - bad_char[ord(text[shift + j])])


if __name__ == "__main__":
    text = "ABAAABCDABCABC"
    pattern = "ABC"

    print("Rabin-Karp Algorithm:")
    rabin_karp(text, pattern)

    print("\nKnuth-Morris-Pratt (KMP) Algorithm:")
    kmp_search(text, pattern)

    print("\nBoyer-Moore Algorithm:")
    boyer_moore(text, pattern)
