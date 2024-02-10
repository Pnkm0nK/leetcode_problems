def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    letters_s, letters_t = {}, {}
    for i in range(len(s)):
        if s[i] not in letters_s:
            letters_s[s[i]] = 0
        if t[i] not in letters_t:
            letters_t[t[i]] = 0
        letters_s[s[i]] += 1
        letters_t[t[i]] += 1
    for key in letters_s:
        if letters_s[key] != letters_t[key]:
            return False
    return True


s1 = "anagram"
s2 = "nagaram"
print(isAnagram(s1, s2))