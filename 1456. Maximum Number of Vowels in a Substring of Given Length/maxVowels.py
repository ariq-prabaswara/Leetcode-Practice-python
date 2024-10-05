# Sliding Window Problem

def maxVowels(s, k):
    vowels = "aeiou"
    max_vowel = 0
    count = 0
    start_i = 0 # Left pointer
    end_i = 0 # Right pointer
    
    while end_i < len(s):
        # Open Window
        if end_i - start_i < k:
            if s[end_i] in vowels:
                count +=1
            end_i +=1
        
        # Close Window
        else:
            if s[start_i] in vowels:
                count -=1
            start_i +=1  
        
        # Update max_count
        if count > max_vowel:
            max_vowel = count
    return max_vowel

s = "aeioubofsijjdahfasimaawqhjfassdaioundaalnfsadjkdskkaaiaogios"
k = 10
print(maxVowels(s,k))