# The syntax:
# string[start:stop:step]

# With start and stop value
a = "teri maa ka saki naka"
print(a[5:9])  # output- maa

txt = "Sometimes in life you have to let go in order to move ahead."
print(txt[2:4])  # output- me

# Only specifying start and keeping the stop colon and not providing the value makes it so it returns the remaining string to the end.
print(txt[10:])  # output- in life you have to let go in order to move ahead.

b="Suffering in present is a success in future."
# Only specifying the stop value/index and not specifying the start will make it so the substring will start from 0th index to the stop index.
print(b[:9])  # output- Sometimes

# Negative indexing also works. The logic is number line logic. As in, the negative number increment starts from the left side of zero.
# -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8
# So, according to this logic -1 is the end index.
print(b[-7:-1])  # output- future

# The third argument is a step value
# The step value allows you to take every step-th character.
# It takes the first character and then skips to taking the 2nd character
print(b[::2])# Output - Sfeigi rsn sascesi uue

# Reversing a string:
# We can reverse a string using -1 as a step value:
print(b[::-1])