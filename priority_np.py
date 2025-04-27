#Priority Scheduling (Non-Preemptive) Algorithm

num_processes = int(input("Enter number of processes: "))

process_list = []   #gathering all the processes in a list including their burst times and priorities
for index in range(num_processes): 
    burst_time, priority = map(
        int,
        input(f"Enter burst time and priority for process {index+1}: ").split()
    )
    #this returns a tuple of (burst_time, priority) for each process


    #adding the process id to the afformentioned tuple to make the final process list
    process_id = index + 1  #process ID starts from 1
    process_list.append((process_id, burst_time, priority))

#sorting the list by priority (ascending order)
#the process with the highest priority (lowest number) will be executed first
sorted_by_priority = sorted(process_list, key=lambda proc: proc[2])   #here we used 2 because the priority is the 3rd element in the tuple (index 2), if you are using a different logic to store the processes, you may need to change this index accordingly

#displayes the sorted processes in a table format
print("\nProcessID  BurstTime  Priority")
for process_id, burst_time, priority in sorted_by_priority:
    print(f"{process_id:^10}{burst_time:^11}{priority:^9}")
