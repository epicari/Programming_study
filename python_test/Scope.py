#
# HackerRank Tutorials Day 14: Scope
# 
#
#

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = abs(max(a) - min(a))

# End of Difference class
if __name__ == "__main__":
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)