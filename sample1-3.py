arr1 = {}
for i in range(1,101):
    arr1[i]=0

for j in range(2,101):
    for i in range(j,101):
        if i % j == 0:
            arr1[i]=arr1[i]^1

for i in range(1,101):
    if arr1[i] == 0:
        print("TRUE",i)