import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Skapa figuren och fyra underdiagram
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1)
fig.suptitle("Datorns resursanvändning i realtid (Windows)")

# Skapa listor för att lagra data
cpu_data, ram_data, disk_data, network_data, battery_data = [], [], [], [], []

# Uppdateringsfunktion för att hämta och plotta ny data
def update(frame):
    global network_data, battery_data

    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('C:\\').percent
    network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    
    # Kolla om batteriinformation finns
    battery = psutil.sensors_battery()
    battery_level = battery.percent if battery else None

    cpu_data.append(cpu_usage)
    ram_data.append(ram_usage)
    disk_data.append(disk_usage)
    network_data.append(network_usage)
    if battery_level is not None:
        battery_data.append(battery_level)

    # Begränsa datamängden till de senaste 50 värdena
    if len(cpu_data) > 50:
        cpu_data.pop(0)
        ram_data.pop(0)
        disk_data.pop(0)
        network_data.pop(0)
        if battery_level is not None:
            battery_data.pop(0)

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()

    ax1.plot(cpu_data, label="CPU-användning (%)", color="r")
    ax2.plot(ram_data, label="RAM-användning (%)", color="g")
    ax3.plot(disk_data, label="Diskutnyttjande (%)", color="b")
    ax4.plot(network_data, label="Nätverkstrafik (bytes)", color="m")
    
    if battery_level is not None:
        ax5.plot(battery_data, label="Batterinivå (%)", color="c")

    ax1.legend(loc="upper right")
    ax2.legend(loc="upper right")
    ax3.legend(loc="upper right")
    ax4.legend(loc="upper right")
    if battery_level is not None:
        ax5.legend(loc="upper right")

# Skapa animerad graf
ani = animation.FuncAnimation(fig, update, interval=1000)
plt.show()
