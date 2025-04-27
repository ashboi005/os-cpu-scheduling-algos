#Shortest Remaining Time First (SRTF) CPU Scheduling Simulation
#This is a preemptive version of Shortest Job First (SJF) scheduling.
#It allows a process to be interrupted if a new process arrives with a shorter remaining time.

#read num_processes, arrival times and burst times from user input
num_processes = int(input("Enter number of processes: "))

arrival_times = list(
    map(int, input("Enter arrival times: ").split())
)

burst_times = list(
    map(int, input("Enter burst times (space-separated):  ").split())
)

#later will be used to track how much time is left for each process, orignally same as burst times
remaining_times = burst_times.copy()

#empty lists to store the completion, turnaround and waiting times for each process
#these will be filled in as the processes are completed
completion_times = [0] * num_processes     # when each process finishes
turnaround_times = [0] * num_processes     # completion − arrival
waiting_times    = [0] * num_processes     # turnaround − burst

#simulated clock to execute procceses one unit of time at a time
current_time    = 0

#count of how many processes have finished executing
completed_count = 0

#main logic for the SRTF algorithm
#loop that will run until all processes are completed
while completed_count < num_processes:

    #look for all processes that have arrived (arrival_times[i] ≤ current_time)
    #AND still need execution i.e CPU time (remaining_times[i] > 0)
    ready = [
        i for i in range(num_processes)
        if arrival_times[i] <= current_time and remaining_times[i] > 0
    ]

   #if no processes are ready (arrived yet) increment the current time and continue to the next iteration
    if not ready:
        current_time += 1
        continue


    #but assuming there are process(es) ready to run then from the ready list we
    #have to pick the process with the smallest remaining time
    proc_id = min(ready, key=lambda i: remaining_times[i])
    #ready list holds the indices, which are one by one put into remaining_times[i] untill the smallest is found
    #the min fucntion returns the index of the process with the smallest remaining time (from the ready list)
    #proc_id is the index of the process with the smallest remaining time

    #now that we have located the process with the smallest remaining time, we can execute it

    #we assume a process atleast has 1 unit of time to execute, before it is preempted
    #so we decrement the remaining time of the selected process by 1
    #and increment the current time by 1 to simulate the passage of time
    remaining_times[proc_id] -= 1
    current_time += 1

    #if assuming that unit of execution finished the process (remaining becomes 0):
    #we enter this if statement to record the completion time and calculate turnaround and waiting times and increment the count of completed processes
    #else we just continue to the next iteration of the loop (which can be the next process or the same one again)
    if remaining_times[proc_id] == 0:
        completion_times[proc_id] = current_time   #record the completion time
        turnaround_times[proc_id] = current_time - arrival_times[proc_id] #turnaround = completion - arrival
        waiting_times[proc_id]    = turnaround_times[proc_id] - burst_times[proc_id] #waiting = turnaround - burst
        completed_count += 1 #increment the count of completed processes

#after all processes are completed and we wxit the loop, we can calculate the average waiting and turnaround times
print("\nProcess  Arrival  Burst  Completion  Turnaround  Waiting")
for i in range(num_processes):
    print(
        f"{i+1:>3} "
        f"{arrival_times[i]:>8} "
        f"{burst_times[i]:>6} "
        f"{completion_times[i]:>11} "
        f"{turnaround_times[i]:>12} "
        f"{waiting_times[i]:>8}"
    )

#these weird integers are just for formatting the output to make it look nice and readable
#the >3 means right align the number in a field of 3 characters, and so on for the other numbers
