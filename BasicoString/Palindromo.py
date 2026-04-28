def isPalindrome(self, s:str) -> bool:

    
    hi = len(s) - 1
    lo = 0

    while lo < hi:
        if not s[lo].isalnum() or  s[lo]== " ":
            lo+=1
            continue
        elif not s[hi].isalnum() or s[hi] == " ":
            hi-=1
            continue


        if not s[lo].lower() == s[hi].lower():
            return False
        lo += 1
        hi -= 1

    return True