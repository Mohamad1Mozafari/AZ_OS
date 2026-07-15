"""
CPU Scheduler Simulator with Round Robin Algorithm
==================================================
This program takes several processes from the user and calculates
their execution order on the CPU using the Round Robin algorithm.

The output includes:
    - Gantt Chart
    - Complete process table (AT, BT, CT, TAT, WT, RT)
    - Average waiting time and average turnaround time

Note: This program is written without using any external libraries
to keep the code as simple, readable, and understandable as possible.
"""


# ---------------------------------------------------------------------------
# Part 1: Round Robin Algorithm Core
# ---------------------------------------------------------------------------

def run_round_robin(processes, quantum):
    """
    Execute the Round Robin algorithm on a list of processes.

    processes: list of dictionaries with keys pid, arrival, burst
    quantum:   time quantum value

    Output: (gantt_chart, stats)
        gantt_chart -> list of (pid, start_time, end_time)
        stats       -> dictionary pid -> complete process information
    """

    # Sort processes by arrival time
    processes = sorted(processes, key=lambda p: p["arrival"])

    # Remaining burst time for each process
    remaining_burst = {p["pid"]: p["burst"] for p in processes}

    first_start_time = {}   # First time each process ran on CPU
    completion_time = {}    # Completion time for each process

    ready_queue = []                 # Queue of processes ready to run
    not_arrived_yet = processes[:]   # Processes that haven't arrived yet
    gantt_chart = []                 # Record each execution interval on CPU

    current_time = 0

    def move_arrived_processes_to_queue(time_now):
        """Add any process that has arrived by this moment to the ready queue."""
        nonlocal not_arrived_yet
        newly_arrived = [p for p in not_arrived_yet if p["arrival"] <= time_now]
        ready_queue.extend(newly_arrived)
        not_arrived_yet = [p for p in not_arrived_yet if p["arrival"] > time_now]

    # If no process arrives at time 0, advance time to the first arrival
    if not_arrived_yet:
        current_time = not_arrived_yet[0]["arrival"]
    move_arrived_processes_to_queue(current_time)

    # Main scheduling loop: continue until ready queue is empty
    while ready_queue:
        process = ready_queue.pop(0)
        pid = process["pid"]

        # Record first execution of the process (for Response Time calculation)
        if pid not in first_start_time:
            first_start_time[pid] = current_time

        # This process runs for at most one quantum
        run_time = min(quantum, remaining_burst[pid])
        start_time = current_time
        current_time += run_time
        remaining_burst[pid] -= run_time

        gantt_chart.append((pid, start_time, current_time))

        # Add processes that arrived during this execution to the queue
        move_arrived_processes_to_queue(current_time)

        if remaining_burst[pid] > 0:
            # Process not finished yet -> return to the end of queue
            ready_queue.append(process)
        else:
            # Process has finished
            completion_time[pid] = current_time

        # If queue is empty but there are processes that haven't arrived yet
        if not ready_queue and not_arrived_yet:
            current_time = not_arrived_yet[0]["arrival"]
            move_arrived_processes_to_queue(current_time)

    # Calculate final statistics for each process using the given formulas
    stats = {}
    for p in processes:
        pid = p["pid"]
        arrival = p["arrival"]
        burst = p["burst"]
        finish = completion_time[pid]

        turnaround_time = finish - arrival
        waiting_time = turnaround_time - burst
        response_time = first_start_time[pid] - arrival

        stats[pid] = {
            "AT": arrival,
            "BT": burst,
            "CT": finish,
            "TAT": turnaround_time,
            "WT": waiting_time,
            "RT": response_time,
        }

    return gantt_chart, stats


# ---------------------------------------------------------------------------
# Part 2: Output Display
# ---------------------------------------------------------------------------

def print_gantt_chart(gantt_chart):
    """Print the Gantt chart according to the project sample format."""
    print("================ Gantt Chart ================")

    bars = "| " + " | ".join(pid for pid, _, _ in gantt_chart) + " |"
    print(bars)

    # Time row: start time of the first interval + end times of all intervals
    times = [str(gantt_chart[0][1])]
    times += [str(end) for _, _, end in gantt_chart]
    print(" ".join(times))
    print()


def print_process_table(stats, process_order):
    """Print the complete process table according to the project sample format."""
    print("================ Process Table ================")
    print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}{'RT':<5}")

    for pid in process_order:
        s = stats[pid]
        print(f"{pid:<5}{s['AT']:<5}{s['BT']:<5}{s['CT']:<5}"
              f"{s['TAT']:<5}{s['WT']:<5}{s['RT']:<5}")
    print()


def print_averages(stats):
    """Print average waiting time and average turnaround time."""
    count = len(stats)
    avg_waiting = sum(s["WT"] for s in stats.values()) / count
    avg_turnaround = sum(s["TAT"] for s in stats.values()) / count

    print(f"Average Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")


# ---------------------------------------------------------------------------
# Part 3: User Input
# ---------------------------------------------------------------------------

def read_processes_from_user():
    """Get process information from the user through text input."""
    processes = []

    process_count = int(input("Enter the number of processes: "))

    for i in range(process_count):
        print(f"\n--- Process {i + 1} Information ---")
        pid = input("Process ID (e.g., P1): ")
        arrival = int(input("Arrival Time: "))
        burst = int(input("CPU Burst Time: "))

        processes.append({"pid": pid, "arrival": arrival, "burst": burst})

    quantum = int(input("\nEnter the Time Quantum: "))

    return processes, quantum


# ---------------------------------------------------------------------------
# Part 4: Main Execution
# ---------------------------------------------------------------------------

def main():
    processes, quantum = read_processes_from_user()
    process_order = [p["pid"] for p in processes]

    print()
    gantt_chart, stats = run_round_robin(processes, quantum)

    print_gantt_chart(gantt_chart)
    print_process_table(stats, process_order)
    print_averages(stats)


if __name__ == "__main__":
    main()