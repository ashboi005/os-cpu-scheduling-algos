# CPU Scheduling Algorithms

This repository contains Python implementations of various CPU scheduling algorithms commonly studied in Operating Systems courses along with their explanations.

## Implemented Algorithms

*   **First-Come, First-Served (FCFS):** [`fcfs.py`](fcfs.py)
*   **FCFS but with Arrival Times:** [`fcfs-arrival.py`](fcfs-arrival.py)
*   **Shortest Job First (SJF) (Non-Preemptive):** [`sjf.py`](sjf.py)
*   **Shortest Remaining Time First (SRTF) (Preemptive SJF):** [`srtf.py`](srtf.py)
*   **Priority Scheduling (Non-Preemptive):** [`priority_np.py`](priority_np.py)
*   **Priority Scheduling (Preemptive):** [`priority_p.py`](priority_p.py)
*   **Round Robin (RR):** [`round_robin.py`](round_robin.py)

## Usage

Each algorithm is implemented in its own Python file. To run a specific algorithm simulation:

1.  Navigate to the project directory in your terminal.
2.  Execute the desired Python script:
    ```bash
    python <algorithm_file_name>.py
    ```
    For example:
    ```bash
    python fcfs.py
    ```
3.  Follow the prompts to enter the required inputs (number of processes, burst times, arrival times, priorities, time quantum, etc., as applicable to the chosen algorithm).

The script will then output the scheduling results, typically including waiting times and turnaround times for each process, along with their averages.