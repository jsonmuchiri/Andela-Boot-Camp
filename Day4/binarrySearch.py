class BinarySearch(list):
    def __init__(self, x, y):
        # x------Length of list to create
        # y------difference between consecutive values
        self.length = x
        
        for a in range(y, (x*y)+1, y):
            self.append(a)
        #self
    def search(self,search_value):
        solution = {}
        count = 0
        mini= 0
        maxi= self.length
        while mini  <maxi:
            count = count+1
            midpoint = mini + (maxi-mini)//2

            if search_value==self[midpoint]:
                break
            elif search_value > self[midpoint]:
                if mini==midpoint:
                    solution['count'] = 0
                    solution['index'] =- 1
                    return solution
                mini = midpoint
            elif search_value<self[midpoint]:
                maxi= midpoint
        solution['count'] = count
        solution['index'] = midpoint
        return solution

        
#a=BinarySearch(40,1)
#print(a.search(20))

#b=BinarySearch(50,6)
#print(b.search(6))