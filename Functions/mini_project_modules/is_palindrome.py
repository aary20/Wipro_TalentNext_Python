def is_palindrome(str6):
    start=0
    end=len(str6)-1
    while start<end:
        if str6[start]!=str6[end]:
            return False
        start+=1
        end=end-1
    return True