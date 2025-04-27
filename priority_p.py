#Priority Scheduling (Preemptive) Algorithm

#IMPORTANT: The code for this is 90% similar to SRTF algorithm,
#the only diff being that we need to sort the processes by priority instead of remaining time.
#so please refer to the SRTF code for the logic explanation and other details if you haven't already
#the 2 differences are marked with comments in the code below

num_processes = int(input("Enter number of processes: "))
arrival_times = list(map(int, input("Enter arrival times (space-separated): ").split()))
burst_times   = list(map(int, input("Enter burst times (space-separated):  ").split()))

#this is diff no. 1, we need to get the priorities from the user
priorities    = list(map(int, input("Enter priorities (space-separated):    ").split()))

remaining_times  = burst_times.copy()         
completion_times = [0] * num_processes          
turnaround_times = [0] * num_processes         
waiting_times    = [0] * num_processes         
current_time    = 0
completed_count = 0

while completed_count < num_processes:
    ready_queue = [
        i for i in range(num_processes)
        if arrival_times[i] <= current_time and remaining_times[i] > 0
    ]
    
    if not ready_queue:
        current_time += 1
        continue

    #this is diff no. 2, we need to pick the process with the highest priority (lowest number)
    proc_id = min(ready_queue, key=lambda i: priorities[i])

    remaining_times[proc_id] -= 1
    current_time             += 1

    if remaining_times[proc_id] == 0:
        completion_times[proc_id] = current_time
        turnaround_times[proc_id] = current_time - arrival_times[proc_id]
        waiting_times[proc_id] = turnaround_times[proc_id] - burst_times[proc_id]
        completed_count += 1

print("\nP#  Arrival  Burst  Priority  Completion  Turnaround  Waiting")
for i in range(num_processes):
    print(
        f"{i+1:>2}  "
        f"{arrival_times[i]:>7}  "
        f"{burst_times[i]:>5}  "
        f"{priorities[i]:>8}  "
        f"{completion_times[i]:>10}  "
        f"{turnaround_times[i]:>10}  "
        f"{waiting_times[i]:>7}"
    )
