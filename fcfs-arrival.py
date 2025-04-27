# FCFS CPU Scheduling Simulation with Arrival Times

num_processes = int(input("Enter number of processes: "))
arrival_times = list(map(int, input("Enter arrival times: ").split()))
burst_times   = list(map(int, input("Enter burst times: ").split()))

#combine arrival and burst times with process IDs
process_list = [
    (arrival_times[i], burst_times[i], i+1)
    for i in range(num_processes)
]

#sort by arrival time (earliest first)
process_list.sort(key=lambda x: x[0]) #x[0] is the arrival time


current_time      = 0    #simulated clock
total_waiting     = 0
total_turnaround  = 0


print("\nPID  Arrival  Burst  Waiting  Turnaround")
for arrival, burst, pid in process_list:
    if current_time < arrival:    #if the CPU is idle until this process arrives
        current_time = arrival

    waiting_time    = current_time - arrival
    turnaround_time = waiting_time + burst

    total_waiting    += waiting_time
    total_turnaround += turnaround_time

    print(f"{pid:>3}  {arrival:>7}  {burst:>5}  {waiting_time:>7}  {turnaround_time:>10}")

    current_time += burst

avg_wait    = total_waiting    / num_processes
avg_tat     = total_turnaround / num_processes

print(f"\nAverage Waiting Time:    {avg_wait:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
