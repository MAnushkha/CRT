'''s = "python programming"
print(s.capitalize())
print(s.title())
s = s.title()
print(s)
'''
#Reverse a string w/o using built-in functions or slicing 
#intput: abc Output: cba
def Reverse_string1(s):
   res = ""
   for ch in s:
      res = ch + res
   return res

def is_palindrome(s):                                      
    return Reverse_string1(s) == s 
print(is_palindrome("abc"))
print(is_palindrome("madam"))

#Anagram 
s1 = "paces"
s2 = "space"

def frequency_count(s):
   d = {}
   for ch in s:
      if ch not in d:
            d[ch] = 1
      else:
          d[ch] += 1
    return d
def Anagrams(s1, s2):
    return frequency_count(s1) == frequency_count(s2)
print(Anagrams("paces", "space")) #True
print(Anagrams("abc","aabbcc"))   #False