class DiagonalDiff:

    def diagonalDifference(self,li):
        primaryDiagonal = 0
        secondaryDiagonal = 0
        for i in range(len(li)):
            for j in range(len(li[i])):
                if(i == j):
                    primaryDiagonal += li[i][j]
                if(i + j == len(li[i])-1):
                    secondaryDiagonal += li[i][j]
        difference = abs(primaryDiagonal - secondaryDiagonal)
        return difference

d = DiagonalDiff()
li = [[11,2,4],[4,5,6],[10,8,-12]]

print(d.diagonalDifference(li))


