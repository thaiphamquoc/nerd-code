class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for i in xrange(0, len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start + 1:
                print "found new sub palindrome with len {} at index {}".format(max_len, i)
                start = i - ((max_len - 1) // 2)
                end = i + (max_len // 2)

        return s[start:end + 1]
    
    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while (L >= 0 and R < len(s) and s[L] == s[R]):
            L -= 1
            R += 1
            
        return R - L - 1
        
def main():
    s = 'cbbd'
    sol = Solution()    
    print sol.longestPalindrome(s)

if __name__ == '__main__':
    main()
