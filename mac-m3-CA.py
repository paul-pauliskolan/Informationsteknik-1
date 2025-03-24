import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil

# Skapa en figur med fyra delgrafer
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 10))
fig.suptitle("Datorns resursanvändning i realtid")

# Listor för att lagra data
cpu_data = []
ram_data = []
disk_data = []
network_data = []

def update(frame):
    global network_data

    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    cpu_data.append(cpu_usage)
    ram_data.append(ram_usage)
    disk_data.append(disk_usage)
    network_data.append(network_usage)

    # Begränsa listans storlek till 50 punkter
    if len(cpu_data) > 50:
        cpu_data.pop(0)
        ram_data.pop(0)
        disk_data.pop(0)
        network_data.pop(0)

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()

    ax1.plot(cpu_data, label="CPU-användning (%)", color="r")
    ax2.plot(ram_data, label="RAM-användning (%)", color="g")
    ax3.plot(disk_data, label="Diskutnyttjande (%)", color="b")
    ax4.plot(network_data, label="Nätverkstrafik (bytes)", color="m")

    ax1.legend(loc="upper right")
    ax2.legend(loc="upper right")
    ax3.legend(loc="upper right")
    ax4.legend(loc="upper right")

    ax1.set_ylabel("CPU (%)")
    ax2.set_ylabel("RAM (%)")
    ax3.set_ylabel("Disk (%)")
    ax4.set_ylabel("Nätverk (bytes)")

    ax4.set_xlabel("Tid")

# Starta animationen
ani = animation.FuncAnimation(fig, update, interval=1000)
plt.show()
