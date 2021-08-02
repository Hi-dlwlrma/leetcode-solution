class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # solution 1
        r_dict, m_dict = {}, {}
        r_dict = {s: ransomNote.count(s) for s in set(ransomNote)}
        m_dict = {s: magazine.count(s) for s in set(magazine) if s in r_dict}
        
        if len(r_dict) != len(m_dict):
            return False
        for key, val in r_dict.items():
            if m_dict[key] < val:
                return False
        return True

        # solution 2
        # from collections import Counter
        # if (Counter(ransomNote) & Counter(magazine)) == Counter(ransomNote):
        #     return True
        # else:
        #     return False
