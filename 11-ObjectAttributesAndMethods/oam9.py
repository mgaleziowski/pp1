import random

class Arrays():
    @staticmethod
    def a(n):
        array=[]
        for r in range(n):
            array.append(n)
        return array
    def b(l,m,n):
        array=[]
        for i in range(l):
            array.append(random.randint(m,n))
        return array
    def c(array,m,n):
        count=0
        for i in array:
            if(i>=m and i<=n):
                count+=1
        return count



    
