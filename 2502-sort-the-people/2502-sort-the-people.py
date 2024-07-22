class Solution(object):
    def sortPeople(self, names, heights):
        length = len(heights)
        mymap = {}
        for i in range(length):
            mymap[heights[i]] = names[i]
        heights.sort(reverse=True)
        res = []
        for height in heights:
            res.append(mymap[height])
        return res