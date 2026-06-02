class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)

        for string in strs:
            letters = [0] * 26
            for s in string:
                letters[ord(s) - ord('a')] += 1
            collection[tuple(letters)].append(string)
        
        return list(collection.values())