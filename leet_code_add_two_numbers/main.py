# Given a string s, find the length of the longest
# substring
#  without repeating characters.

s = 'pwwkew'
s_list = []

for item in s:
    s_list.append(item)

s_set = set(s_list)

print(s_set(2))

