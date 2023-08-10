class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        #print(sorted(v))
        v=sorted(v)
        a,b=v[0],v[-1]
        k=""
        for i in range(min(len(a),len(b))):
            if a[i]!=b[i]:
                return k
            k=k+a[i]
        return k