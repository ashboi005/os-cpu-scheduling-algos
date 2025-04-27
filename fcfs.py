#First-Come, First-Served (FCFS) Scheduling Algorithm

#it reads the number of processes, unnecessary if not validating
num_processes = int(input())

#reads the burst times
burst_times = list(map(int, input().split()))

#OR YOU CAN USE THIS INSTEAD
#burst_times = [int(x) for x in input().split()]   
#this way is more Pythonic and readable but idk both ways work so whatever its upto you

#checks if num_processes is equal to the number of burst times, not needed if not taking in num_processes
if len(burst_times) != num_processes:
    raise ValueError(f"Expected {num_processes} burst times, but got {len(burst_times)}")

#OR BETTER YET YOU CAN ALSO USE THIS WHICH COMBINES THE BURST TIME INPUT AND VALIDATION
#burst_times = [int(input(f"Enter burst time for process {i+1}: ")) for i in range(num_processes)]

#initializes waiting time and turnaround time to zero
waiting_time = 0
turnaround_time = 0

#actual FCFS logic is here
print("Burst Time  Waiting Time  Turnaround Time")
for burst_time in burst_times:
    turnaround_time = waiting_time + burst_time   #turnaround time is the sum of waiting time and burst time
    print(f"{burst_time}           {waiting_time}             {turnaround_time}")
    waiting_time += burst_time     #waiting time for the next process is the sum of all previous burst times


