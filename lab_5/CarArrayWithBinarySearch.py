from lab_4.CarArray import CarArray
from lab_4.Array import Array

class CarArrayWithBinarySearch(CarArray):

    def binarySearch(self, key):
        self.checkSorting()

        def recursiveBinary(key, array):
            if len(array) == 0:
                return None
            middleIndex = (len(array) // 2)
            if array.get(middleIndex).vin > key:
                return recursiveBinary(key, array.subArray(middleIndex, len(array) - 1))
            elif array.get(middleIndex).vin < key:
                return recursiveBinary(key, array.subArray(0, middleIndex))
            return array.get(middleIndex)

        return recursiveBinary(key, Array(self.elems[::]))



    def checkSorting(self):
        unsorted = self.elems[::]
        self.insertionSort()
        for i in range(len(unsorted)):
            if unsorted[i].vin != self.elems[i].vin:
                raise RuntimeError("Array is not sorted")

