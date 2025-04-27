#Shortest Job First (SJF) Scheduling Algorithm

num_processes = int(input("Enter number of processes: "))

#best method acc to me as explained in fcfs so ill be using this only
burst_times = [
    int(input(f"Enter burst time for process {i+1}: "))
    for i in range(num_processes)
]

#sorting as we have to run the processes with least burst time first
burst_times.sort()

#init the total waiting time and elapsed time to zero
total_waiting_time = 0
elapsed_time = 0    

#actual SJF logic is here
for burst_time in burst_times:
    #this is so that when a job starts running, the waiting time is the sum of all previous burst times (i.e. the elapsed time)
    total_waiting_time += elapsed_time
    
    #this is when the job is actually running, so we add the burst time to the elapsed time
    elapsed_time += burst_time

#calculate averages as demanded by the question
average_waiting_time = total_waiting_time / num_processes
average_turnaround_time = elapsed_time / num_processes

print(f"Average Waiting Time: {average_waiting_time}")
print(f"Average Turnaround Time: {average_turnaround_time}")


"""
IMPORTANT: FCFS schedules by arrival order, whereas non-preemptive SJF schedules by shortest burst-time first. 
this is the key difference. so this means you can technically reuse the exact FCFS logic loop 
after sorting the burst times, with the only addition being that you need to calculate 
the total waiting time and elapsed time in the loop, and then after the loop, 
compute average waiting and turnaround times as you normally would.
here is how the code would look like if you wanted to use the same loop as FCFS:
"""

# num_processes = int(input("Enter number of processes: "))

# burst_times = [
#     int(input(f"Enter burst time for process {i+1}: "))
#     for i in range(num_processes)
# ]

# burst_times.sort()

# waiting_time = 0
# total_waiting_time    = 0
# total_turnaround_time = 0

# print("Burst  Wait  Turnaround")

# for burst_time in burst_times:
#     turnaround_time = waiting_time + burst_time   #(same as fcfs)

#     print(f"{burst_time:5d} {waiting_time:5d} {turnaround_time:11d}")

#     total_waiting_time    += waiting_time   #(this part is new)
#     total_turnaround_time += turnaround_time   #(this part is new)

#     waiting_time += burst_time   #(same as fcfs)

# average_waiting_time    = total_waiting_time    / num_processes
# average_turnaround_time = total_turnaround_time / num_processes

# print(f"\nAverage Waiting Time:    {average_waiting_time}")
# print(f"Average Turnaround Time: {average_turnaround_time}")

