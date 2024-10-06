class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1 = sentence1.split()
        l2 = sentence2.split()
        n1 = len(l1)
        n2 = len(l2)
        if n1 > n2:
            n1, n2 = n2, n1
            l1, l2 = l2[:], l1[:]

        i = 0
        while i < n1 and l1[i] == l2[i]:
            i += 1
        while i < n1 and l1[i] == l2[n2 - n1 + i]:
            i += 1

        return i == n1