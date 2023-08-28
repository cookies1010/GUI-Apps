import psutil
import time
import matplotlib.pyplot as plt

# Global variables to store usage data
cpu_usage_data = []
ram_usage_data = []
disk_usage_data = []

def get_cpu_usage():
    return psutil.cpu_percent(interval=1, percpu=True)

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

if __name__ == "__main__":
    plt.ion()  # Turn on interactive mode for plotting

    fig, axes = plt.subplots(nrows=3, figsize=(10, 10))
    fig.suptitle('Resource Usage Monitor')  # Set the figure title

    for ax, label in zip(axes, ['CPU', 'RAM', 'Disk']):
        ax.set_ylabel('Usage (%)')
        ax.set_xlabel('Time (2 seconds interval)')
        ax.set_title(f'{label} Usage')

    plt.tight_layout()

    while True:
        cpu_usage = get_cpu_usage()
        ram_usage = get_ram_usage()
        disk_usage = get_disk_usage()

        cpu_usage_data.append(cpu_usage)
        ram_usage_data.append(ram_usage)
        disk_usage_data.append(disk_usage)

        # Update and redraw the plots
        for ax, usage_data, label in zip(axes, [cpu_usage_data, ram_usage_data, disk_usage_data], ['CPU', 'RAM', 'Disk']):
            ax.clear()
            ax.plot(usage_data, label=label)
            ax.legend()

        plt.pause(2)  # Pause to allow plot update
