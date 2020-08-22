# read and prepare n, m, and p
n = int(input("Number of jobs: "))
m = int(input("Number of machines: "))
pStr = input("Processing times: ")

p = pStr.split(' ')
for i in range(n):
    p[i] = int(p[i])
    
# machine loads and job assignment
loads = [0] * m
assignment = [0] * n

# in iteration j, assign job j to the least loaded machine
for j in range(n):
    
    # find the least loaded machine
    leastLoadedMachine = 0  # 比較的值
    leastLoaded = loads[0]  # 假設比較的值是第0台
    for i in range(1, m):
        if loads[i] < leastLoaded:
            leastLoadedMachine = i
            leastLoaded = loads[i]
            
    # schedule a job
    loads[leastLoadedMachine] += p[j]   # 把作業給最閒的機器做
    assignment[j] = leastLoadedMachine + 1  # 第j個job assign給誰要記起來
    
    # to check the process
    print(str(p[j]) + ": " + str(loads))
    
# the result
print("Job assignment: " + str(assignment))
print("Machine laods: " + str(loads))  