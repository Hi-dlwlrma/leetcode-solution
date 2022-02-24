class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        
        chars = "!?',;."
        for c in chars:
            paragraph = paragraph.replace(c, ' ')
        arr = paragraph.lower().split()
        
        counter = Counter(arr)
        mylist = counter.most_common()
        
        for elem in mylist:
            if elem[0] in banned:
                continue
            return elem[0]
