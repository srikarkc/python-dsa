# Permutation in String problem

Been thinking about this problem and initially did not understand the solution.

I get it now.

so say s1 = 'ab'

s2 = 'asdfasdfbasdfalk'

A permutation of s1 is in s2 'ba'. So, first we get the char counts of s1 and then compare with the char counts of s2 with sliding window of size s1. The sliding window size ensures that it is a permutation and not just the same characters with string s2.
