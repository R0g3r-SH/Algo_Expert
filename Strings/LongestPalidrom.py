import string


def longestPalindromicSubstring(string):
    #
    longest = ""
    for start in range(len(string)):
        for end in range(start, len(string)):
            substr = string[start:end]
            longest = substr if len(substr) > len(
                longest) and isPalindrome(substr) else longest
    return longest


def isPalindrome(string):
    l = 0
    r = len(string)-1

    while l < r:
        if string[l] != string[r]:
            return False

        l += 1
        r -= 1
    return True


string = "abaxyzzyxf"
print(longestPalindromicSubstring(string))
