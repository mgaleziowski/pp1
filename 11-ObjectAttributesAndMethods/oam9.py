import random

class Arrays():
    @staticmethod
    def a_gen(n):
        b=[]
        for r in range(n):
            b.append(n)
        return b
    def b_gen(l,m,n):
        b=[]
        for r in range(l):
            b.append(random.randint(m,n))
        return b
    def c_gen(array,m,n):
        count=0
        for i in array:
            if(i>=m and i<=n):
                count+=1
        return count


    
