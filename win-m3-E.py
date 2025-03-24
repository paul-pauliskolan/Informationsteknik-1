import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Skapa figuren och tre underdiagram
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.suptitle("Datorns resursanvändning i realtid (Windows)")

# Skapa listor för att lagra data
cpu_data, ram_data, disk_data = [], [], []

# Uppdateringsfunktion för att hämta och plotta ny data
def update(frame):
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('C:\\').percent  # Windows-anpassad sökväg

    cpu_data.append(cpu_usage)
    ram_data.append(ram_usage)
    disk_data.append(disk_usage)

    if len(cpu_data) > 50:
        cpu_data.pop(0)
        ram_data.pop(0)
        disk_data.pop(0)

    ax1.clear()
    ax2.clear()
    ax3.clear()

    ax1.plot(cpu_data, label="CPU-användning (%)", color="r")
    ax2.plot(ram_data, label="RAM-användning (%)", color="g")
    ax3.plot(disk_data, label="Diskutnyttjande (%)", color="b")

    ax1.legend(loc="upper right")
    ax2.legend(loc="upper right")
    ax3.legend(loc="upper right")

# Skapa animerad graf
ani = animation.FuncAnimation(fig, update, interval=1000)

# Visa grafen
plt.show()
