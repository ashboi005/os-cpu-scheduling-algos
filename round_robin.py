#Round Robin CPU Scheduling Algorithm

num_processes, time_quantum = map(
 int,
 input("Enter number of processes and time quantum: ").split()
)

burst_times = list(
 map(int, input("Enter burst times (space-separated): ").split())
)

remaining_times = burst_times.copy()     #how much time each process still needs
current_time    = 0                      #simulation clock
waiting_times   = [0] * num_processes    #will record each process’s waiting time

#main logic for the Round Robin algorithm
while any(remaining_times):   #i.e untill remaining_times is not empty 
 for index in range(num_processes):
     if remaining_times[index] > 0:   #if the process still has time left
         slice_time = min(remaining_times[index], time_quantum)  
         #we do this because time quantum can be greater than the remaining time of the process, 
         #so it calcuates the minimum of the two and assigns it to slice_time 
         # because below we are using it to increment the current time and decrement the remaining time.
         
         #in other algos we do it one unit of time at a time but here since a time quanutm is given,
         #we can assume that the process is running for the entire time quantum or until it finishes, whichever is smaller
         #so we can do it in one go instead of one unit at a time
         current_time    += slice_time    
         remaining_times[index] -= slice_time
         
         #if it just finished, record its waiting time
         #else just continue to the next process in the loop
         if remaining_times[index] == 0:
             waiting_times[index] = current_time - burst_times[index]

#calculate totals and averages
total_waiting_time    = sum(waiting_times)
total_turnaround_time = sum(burst_times[i] + waiting_times[i] for i in range(num_processes))
average_waiting_time    = total_waiting_time    / num_processes
average_turnaround_time = total_turnaround_time / num_processes

#display the results in a table format
print("\nProcess  Burst_Time  Waiting_Time  Turnaround_Time")
for i in range(num_processes):
 tat = burst_times[i] + waiting_times[i]
 print(
     f"{i+1:^7}{burst_times[i]:^12}"
     f"{waiting_times[i]:^14}{tat:^17}"
 )

print(f"\nAverage Waiting Time:    {average_waiting_time}")
print(f"Average Turnaround Time: {average_turnaround_time}")
