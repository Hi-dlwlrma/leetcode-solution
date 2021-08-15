class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Solution 1
        case1 = word.upper()
        case2 = word.lower()
        case3 = word[0].upper() + word[1:].lower()
        
        if word == case1 or word == case2 or word == case3:
            return True
        else: return False

        
        # Solution 2
        # [A−Z]* matches one char from 'A' to 'Z'
        # [a-z]* matches one char from 'a' to 'z'
        # * represents repeat the pattern before it at least 0 times
        # | represents "or"
        # . can matches any char
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
        
            
