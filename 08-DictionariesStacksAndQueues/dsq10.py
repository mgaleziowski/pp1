ar=[ 
{
"country":"Poland",
"population":"38m"
},
{
"country":"USA",
"population":"300m"
},
{
"country":"Australia",
"population":"34m"
},
{
"country":"Germany",
"population":"39m"
},
{
"country":"Canada",
"population":"34m"
}
]
i=0
while(i<5):
    for k,v in ar[i].items():
        print(v,end=" ")
    print()
    i+=1