"""
شبیه‌ساز زمان‌بندی پردازنده با الگوریتم Round Robin
======================================================
این برنامه چند فرآیند را از کاربر می‌گیرد و با استفاده از الگوریتم
Round Robin (نوبتی) ترتیب اجرای آن‌ها روی CPU را محاسبه می‌کند.

خروجی برنامه شامل موارد زیر است:
    - نمودار گانت (Gantt Chart)
    - جدول کامل فرآیندها (AT, BT, CT, TAT, WT, RT)
    - میانگین زمان انتظار و میانگین زمان برگشت

نکته: این برنامه بدون استفاده از هیچ کتاب‌خانه‌ی آماده‌ای نوشته شده است
تا کد تا حد امکان ساده، خوانا و قابل فهم باقی بماند.
"""


# ---------------------------------------------------------------------------
# بخش اول: هسته‌ی الگوریتم Round Robin
# ---------------------------------------------------------------------------

def run_round_robin(processes, quantum):
    """
    اجرای الگوریتم Round Robin روی لیستی از فرآیندها.

    processes: لیستی از دیکشنری‌ها با کلیدهای pid, arrival, burst
    quantum:   مقدار کوانتوم زمانی

    خروجی: (gantt_chart, stats)
        gantt_chart -> لیستی از (pid, start_time, end_time)
        stats       -> دیکشنری pid -> اطلاعات کامل فرآیند
    """

    # فرآیندها را بر اساس زمان ورود مرتب می‌کنیم
    processes = sorted(processes, key=lambda p: p["arrival"])

    # زمان باقی‌مانده از هر فرآیند برای اجرا
    remaining_burst = {p["pid"]: p["burst"] for p in processes}

    first_start_time = {}   # اولین باری که فرآیند روی CPU اجرا شده
    completion_time = {}    # زمان پایان کامل هر فرآیند

    ready_queue = []                 # صف فرآیندهای آماده‌ی اجرا
    not_arrived_yet = processes[:]   # فرآیندهایی که هنوز نرسیده‌اند
    gantt_chart = []                 # ثبت هر بازه‌ی اجرا روی CPU

    current_time = 0

    def move_arrived_processes_to_queue(time_now):
        """هر فرآیندی که تا این لحظه رسیده را وارد صف آماده می‌کند."""
        nonlocal not_arrived_yet
        newly_arrived = [p for p in not_arrived_yet if p["arrival"] <= time_now]
        ready_queue.extend(newly_arrived)
        not_arrived_yet = [p for p in not_arrived_yet if p["arrival"] > time_now]

    # اگر در زمان صفر فرآیندی نرسیده باشد، زمان را به اولین ورود می‌بریم
    if not_arrived_yet:
        current_time = not_arrived_yet[0]["arrival"]
    move_arrived_processes_to_queue(current_time)

    # حلقه‌ی اصلی زمان‌بندی: تا وقتی صف آماده خالی نشده ادامه می‌دهیم
    while ready_queue:
        process = ready_queue.pop(0)
        pid = process["pid"]

        # ثبت اولین اجرای فرآیند (برای محاسبه‌ی Response Time)
        if pid not in first_start_time:
            first_start_time[pid] = current_time

        # این فرآیند حداکثر به اندازه‌ی یک کوانتوم اجرا می‌شود
        run_time = min(quantum, remaining_burst[pid])
        start_time = current_time
        current_time += run_time
        remaining_burst[pid] -= run_time

        gantt_chart.append((pid, start_time, current_time))

        # فرآیندهایی که در طول این اجرا رسیده‌اند را به صف اضافه می‌کنیم
        move_arrived_processes_to_queue(current_time)

        if remaining_burst[pid] > 0:
            # فرآیند هنوز تمام نشده -> به انتهای صف برمی‌گردد
            ready_queue.append(process)
        else:
            # فرآیند تمام شده است
            completion_time[pid] = current_time

        # اگر صف خالی شد ولی فرآیند دیگری هنوز نرسیده، زمان را جلو می‌بریم
        if not ready_queue and not_arrived_yet:
            current_time = not_arrived_yet[0]["arrival"]
            move_arrived_processes_to_queue(current_time)

    # محاسبه‌ی آمار نهایی هر فرآیند بر اساس فرمول‌های داده‌شده
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
# بخش دوم: نمایش خروجی‌ها
# ---------------------------------------------------------------------------

def print_gantt_chart(gantt_chart):
    """چاپ نمودار گانت مطابق فرمت نمونه‌ی پروژه."""
    print("================ Gantt Chart ================")

    bars = "| " + " | ".join(pid for pid, _, _ in gantt_chart) + " |"
    print(bars)

    # ردیف زمان‌ها: زمان شروع اولین بازه + زمان پایان همه‌ی بازه‌ها
    times = [str(gantt_chart[0][1])]
    times += [str(end) for _, _, end in gantt_chart]
    print(" ".join(times))
    print()


def print_process_table(stats, process_order):
    """چاپ جدول کامل فرآیندها مطابق فرمت نمونه‌ی پروژه."""
    print("================ Process Table ================")
    print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}{'RT':<5}")

    for pid in process_order:
        s = stats[pid]
        print(f"{pid:<5}{s['AT']:<5}{s['BT']:<5}{s['CT']:<5}"
              f"{s['TAT']:<5}{s['WT']:<5}{s['RT']:<5}")
    print()


def print_averages(stats):
    """چاپ میانگین زمان انتظار و میانگین زمان برگشت."""
    count = len(stats)
    avg_waiting = sum(s["WT"] for s in stats.values()) / count
    avg_turnaround = sum(s["TAT"] for s in stats.values()) / count

    print(f"Average Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")


# ---------------------------------------------------------------------------
# بخش سوم: دریافت ورودی از کاربر
# ---------------------------------------------------------------------------

def read_processes_from_user():
    """دریافت اطلاعات فرآیندها از کاربر از طریق ورودی متنی."""
    processes = []

    process_count = int(input("تعداد فرآیندها را وارد کنید: "))

    for i in range(process_count):
        print(f"\n--- اطلاعات فرآیند شماره {i + 1} ---")
        pid = input("شناسه فرآیند (مثلاً P1): ")
        arrival = int(input("زمان ورود (Arrival Time): "))
        burst = int(input("زمان اجرای CPU (Burst Time): "))

        processes.append({"pid": pid, "arrival": arrival, "burst": burst})

    quantum = int(input("\nمقدار Time Quantum را وارد کنید: "))

    return processes, quantum


# ---------------------------------------------------------------------------
# بخش چهارم: اجرای اصلی برنامه
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