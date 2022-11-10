import time
n = int(input())
m = [int(input()) for i in range(n)]
k = int(input())
start_time = time.time()
counter = 0
for i in range(len(m)):
    if m[i] > k:
        continue
    for j in range(i,len(m)):
        if m[i]+m[j] == k:
            counter+=1
print(counter)
print("--- %s seconds ---" % (time.time() - start_time))
