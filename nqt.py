n=int(input())
sum=0
counter=1
previouselement=int(input())
sum=previouselement
for i in range(1,n):
    num=int(input())
    if num==previouselement:
        sum+=num+1
        previouselement=num+1
    else:
        sum+=num
        previouselement=num
    counter+=1
try:
    num=input()
    counter+=1
    print("Wrong Input")
except:
    if counter!=n :
        print("Wrong Input")
    else:
        print(sum)
