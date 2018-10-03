sheep = [5, 7, 300, 90, 24, 50, 75]
print("Hello, ",end='')
print("my name is Hung and these are my ship sizes")
print(sheep)
for i in range(1,4):
    print("MONTH",i,":")
    for n in range(len(sheep)):
        sheep[n] += 50
    print("One month has passed, now here is my flock \n",sheep)
    index = sheep.index(max(sheep))
    sheep[index] = 8
    print("Now my biggest sheep has size",max(sheep),"let's shear it")
    print("After shearing, here is my flock \n",sheep)