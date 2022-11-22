import math

class quick_sort:    
    def hoare(self, list, start, end):
        i = start
        j = end
        pivot = math.floor((start + end) / 2)
        pivot_value = list[pivot]
        
        while True:
            while i < j and pivot_value[i]:
                i += 1
            while j < i and pivot_value[j]:
                j -= 1
            if i >= j:
                return j
        
    def master_partition(self, list, initial_partition, final_partition):
        if initial_partition >= final_partition:
            return
        else:
            new_partition = self.hoare(list, initial_partition, final_partition)
            self.master_partition(list, initial_partition, new_partition - 1)
            self.master_partition(list, new_partition + 1, final_partition)
            
    master_partition(list, 0, len(list)-1)
            
            
list = [22, 56, 1, 59, 38, 7, 15, 17, 33]
