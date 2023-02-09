class Solution:
    def isValid(self, s: str) -> bool:
        a=['(','[','{']
        b=[')',']','}']
        c=[]
        for i in s:
            if i in a:
                c.append(i)
            elif i in b:
                pos=b.index(i)
                if(len(c)>0 and c[len(c)-1]==a[pos]):
                    c.pop()
                else:
                    return 0
        if(len(c)==0):
            return 1
        else:
            return 0
