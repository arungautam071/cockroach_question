#first_cockroach----->===================Road============<-----second_cockroach

rod_size=100
first_cockroach = 0
second_cockroach = rod_size
time=0
while(second_cockroach!=first_cockroach):
    first_cockroach+=1
    time+=1
    second_cockroach-=2
    if(time%5==0):
        second_cockroach+=1
    if(time%10==0):
        first_cockroach-=2
    if(second_cockroach<=first_cockroach):
        break
print("Total time to meet: ", time)
print("Distance travel by first cockroach: ",first_cockroach)
print("Distance travel by second cockroach: ",second_cockroach)