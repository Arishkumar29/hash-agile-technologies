class MajorityElementFinder:
    def _init_(self, arr):
        self.arr = arr

    def find_candidate(self):
        candidate = None
        count = 0
        for num in self.arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
    def is_majority(self, candidate):
        count = sum(1 for num in self.arr if num == candidate)
        return count > len(self.arr) // 2

    def find_majority_element(self):
        if not self.arr:
            return "Array is empty. No majority element."
        candidate = self.find_candidate()
        if self.is_majority(candidate):
            return f"The majority element is {candidate}."
        else:
            return "No majority element in the array."
def process_multiple_arrays(arrays):
    for i, arr in enumerate(arrays, 1):
        finder = MajorityElementFinder(arr)
        result = finder.find_majority_element()
        print(f"Array {i}: {result}")
arrays = [
    [3, 3, 4, 2, 4, 4, 2, 4, 4], 
    [1, 1, 2, 2, 3, 3, 4],        
    [5, 5, 5, 5, 5],              
    [],                           
    [2, 2, 2, 3, 3]              
]

process_multiple_arrays(arrays)