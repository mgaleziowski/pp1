text="X-DSPAM-Confidence: 0.8475"
a=""
i=len(text)-1
while(i>=0):
    b=text[i]
    a+=b
    i-=1
pos=a.find(":")
text2=a[0:pos]
c=""
j=len(text2)-1
while(j>=0):
    d=text2[j]
    c+=d
    j-=1
print(float(c))
    
    


