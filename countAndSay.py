'''
For example:

If you have "1", the next line is "11".
If you have "11", the next line is "21".
If you have "111", the next line is "31".
If you have "1111", the next line is "41".

If you have "11222", the next line is "2132" ("11" becomes "21" and "222" becomes "32").
If you have "112225", the next line is "213215" ("11" becomes "21", "222" becomes "32", and "5" becomes "15").'''

    
from itertools import groupby
class Solution:
    @staticmethod
    def countAndSay(n):
        cas='1'
        for _ in range(n-1):
            cas = ''.join( [str(len(list(g))) + str(k) for k,g in groupby(cas)] )
        return cas

print( Solution.countAndSay(7) ) #13112221
   
'''
"1"
"11"
"21"
"1211"
"111221"
"312211"
"13112221"
"1113213211"
"31131211131221"
"13211311123113112211"
"11131221133112132113212221"
"3113112221232112111312211312113211"
"1321132132111213122112311311222113111221131221"
"11131221131211131231121113112221121321132132211331222113112211"
"311311222113111231131112132112311321322112111312211312111322212311322113212221"
'''
