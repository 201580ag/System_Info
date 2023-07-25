import subprocess

def get_cpu_info():
    output = subprocess.check_output(["wmic", "cpu", "get", "name"]).strip()
    print("CPU: " + output.decode())

def get_gpu_info():
    output = subprocess.check_output(["dxdiag", "/t", "dxdiag.txt"])
    with open("system_info.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if "Card name" in line:
            print("GPU: " + line.strip())

def get_ram_info():
    output = subprocess.check_output(["wmic", "memorychip", "get", "capacity"]).strip()
    print("RAM: " + output.decode())

def get_battery_info():
    output = subprocess.check_output(["powercfg", "/batteryreport"])
    with open ("battery-report.html", "r", encoding='UTF8') as f:
        lines = f.readlines()
    for line in lines:
        if "Design capacity" in line:
            print("Battery: " + line.strip())

def main():
    get_cpu_info()
    get_gpu_info()
    get_ram_info()
    get_battery_info()

if __name__ == "__main__":
    main()
