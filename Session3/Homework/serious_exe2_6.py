sheep = [5, 7, 300, 90, 24, 50, 75]
print("Hello, ",end='')
print("my name is Hung and these are my ship sizes")
print(sheep)
index = sheep.index(max(sheep))
sheep[index] = 8
print("Now my biggest sheep has size",max(sheep),"let's shear it")
print("After shearing, here is my flock \n",sheep)
for i in range(1,3):
    print("MONTH",i,":")
    for n in range(len(sheep)):
        sheep[n] += 50
    print("One month has passed, now here is my flock \n",sheep)
    index = sheep.index(max(sheep))
    sheep[index] = 8
    print("Now my biggest sheep has size",max(sheep),"let's shear it")
    print("After shearing, here is my flock \n",sheep)
print("MONTH 3 :")
for n in range(len(sheep)):
    sheep[n] += 50
print("One month has passed, now here is my flock \n",sheep)
sum=0
for i in sheep:
     sum = sum + i
print("My flock has size in total :",sum)
print("I would get",sum,"* 2 $ = ",sum*2,"$")
