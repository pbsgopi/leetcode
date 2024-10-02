class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(list(set(arr)))
        b={}
        for i in range(len(a)):
            b[a[i]]=i+1
        for i in range(len(arr)):
            arr[i]=b[arr[i]]
        return arr