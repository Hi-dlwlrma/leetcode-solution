class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u']
        
        mylist = sentence.split()
        
        ans = ''
        for index, word in enumerate(mylist):
            if word[0].lower() not in vowel:
                word = word[1:] + word[0]
            word += 'ma' + 'a'*(index+1)
            ans += word + ' '
        return ans[:-1]
                     
