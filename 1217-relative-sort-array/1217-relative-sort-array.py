class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic={}
        for i in arr1:
            if dic.get(i) is None:
                dic[i]=1
            else:
                dic[i]+=1
        res=[]
        for j in arr2:
            res+=[j]*dic[j]
        extra=[]
        for k in set(arr1)-set(arr2):
            extra+=[k]*dic[k]
        return res+sorted(extra)