import os
os.system('cls')

v1= [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]


#1 - 
# for i in range(0, 5, 1):
#     v2[i] = v1[i]

# print(v2)


# 2- 
aux = 0 # Define o inicio do vetor1
for i in range(5, 0, -1):
    v2[aux] = v1[i-1]
    aux += 1

print(v1, v2)    