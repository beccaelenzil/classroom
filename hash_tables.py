def is_permutation(string1, string2):
    
    freq_hash = {}
    
    for string in [string1, string2]:
        for char in string:
            if char in freq_hash:
                freq_hash[char]+=1
            else:
                freq_hash[char] = 1
                
    for key in freq_hash:
        if freq_hash[key] == 1:
            return False
            
    return True

print(is_permutation("heelo", "ehllo"))