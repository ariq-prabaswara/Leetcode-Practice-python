def isSubsequence(s, t):
    s_pos = 0
    if len(s) == 0:
        return True
    else:
        for i in range(len(t)):
            if s[s_pos] == t[i]:
                s_pos += 1
                if s_pos+1 > len(s):
                    return True
    return False 

print(isSubsequence("afi","abhofpsi"))

print(isSubsequence("aif","abhofpsi"))