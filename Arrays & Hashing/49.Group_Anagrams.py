def groupAnagrams(strs):
    sorted_words = []
    # sort all words to then check if they are equal or not. Equal words are anagrams
    for word in strs:
        sorted_words.append(sorted(list(word)))
    groups = []
    anagrams = {}
    # use dict to group the words by anagrams
    for i, word in enumerate(sorted_words):
        word = str(word)
        if word not in anagrams:
            anagrams[word] = [strs[i]]
        else:
            anagrams[word].append(strs[i])
    # after forming such dict return values of all keys as one array
    answer = []
    for key in anagrams:
        answer.append(anagrams[key])
    return answer


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))