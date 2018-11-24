sheep = [5, 7, 300, 90, 24, 50, 75]
index = sheep.index(max(sheep))
print("Hello, ",end='')
print("my name is Hung and these are my ship sizes")
print(sheep)
sheep[index] = 8
print("Now my biggest sheep has size",max(sheep),"let's shear it")
print("After shearing, here is my flock \n",sheep)