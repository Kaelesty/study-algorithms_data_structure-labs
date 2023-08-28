from Array import Array

SCALE_FACTOR = 1,247


class CarArray(Array):
    
    def insertionSort(self):
        sorted = []
        toSort = self.elems
        while len(toSort) != 0:
            elem = toSort[0]
            for i in range(len(sorted)):
                if i + 1 == len(sorted):
                    sorted += [elem]
                    break
                elif i == 0 and elem.vin < sorted[0].vin:
                    sorted = [elem] + sorted
                    break
                elif sorted[i - 1].vin < elem.vin <= sorted[i].vin:
                    sorted.insert(i, elem)
                    break
            if len(sorted) == 0:
                sorted = [elem]
            toSort = toSort[1:]
        self.elems = sorted

    def combSort(self):
        shift = len(self.elems) - 1
        cursor = 0
        toSort = self.elems
        while shift != 0:
            try:
                if toSort[cursor].averageSpeed < toSort[cursor + shift].averageSpeed:
                    toSort[cursor], toSort[cursor + shift] = toSort[cursor + shift], toSort[cursor]
                cursor += 1
            except IndexError:
                shift -= 1
                cursor = 0
                continue
        self.elems = toSort

