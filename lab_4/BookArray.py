from Array import Array

class BookArray(Array):

    def countSort(self):
        k = max(list(map(lambda x: x.isbn, self.elems)))
        A = self.elems
        B = [None for i in range(len(self.elems))]
        P = [0 for i in range(k + 1)]

        for elem in A:
            P[elem.isbn] += 1

        P = [sum(P[:i-1]) for i in range(len(P))]
        P = [0] + P[:-1]

        for i in range(len(A)):
            B[P[A[i].isbn]] = A[i]
            P[A[i].isbn] += 1

        self.elems = B

    def mergeSort(self):
        self.elems = self.mergeSortRecursive(self.elems)

    def mergeSortRecursive(self, toSort):
        if len(toSort) in (0, 1):
            return toSort
        leftPart = self.mergeSortRecursive(toSort[:len(toSort) // 2])
        rightPart = self.mergeSortRecursive(toSort[len(toSort) // 2:])

        result = []
        while True:
            if len(leftPart) != 0:
                leftElem = leftPart[0]
            else:
                leftElem = None

            if len(rightPart) != 0:
                rightElem = rightPart[0]
            else:
                rightElem = None

            if leftElem is None and rightElem is None:
                break

            if leftElem is None:
                result += [rightElem]
                rightPart = rightPart[1:]
            elif rightElem is None:
                result += [leftElem]
                leftPart = leftPart[1:]
            else:
                if rightElem.publisher < leftElem.publisher:
                    result += [rightElem]
                    rightPart = rightPart[1:]
                else:
                    result += [leftElem]
                    leftPart = leftPart[1:]
        return result
