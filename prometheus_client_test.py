import prometheus_client as prom
import time as t
import psutil
import socket as so

RAM = prom.Gauge(so.gethostname() + "_memory_used_precent", '')
CPU = prom.Gauge(so.gethostname() + "_cpu_used_precent", '')
total_ram = prom.Gauge(so.gethostname() + "_total_ram", 'pc total ram')
used_ram = prom.Gauge(so.gethostname() + "_used_ram", 'pc used ram')
CPU_Temp = prom.Gauge(so.gethostname() + "_cpu_temp", 'temp')

def get_ram():
    ramu = psutil.virtual_memory()[2]
    RAM.set(ramu)


def get_total_ram():
    ramt = psutil.virtual_memory()[0]/1024/1024/1024
    total_ram.set(ramt)


def get_used_ram():
    ramud = psutil.virtual_memory()[3]/1024/1024/1024
    used_ram.set(ramud)


def get_cpu():
    cpuu = psutil.cpu_percent(interval=1, percpu=True)
    cpul = sum(cpuu) / len(cpuu)
    CPU.set(cpul)

def get_temp():
    temd = psutil.sensors_temperatures()
    teml = (temd['cpu_thermal'])
    temls = str(teml)
    temls1 = temls.replace("(",'')
    temls2 = temls1.replace(")",'')
    temls3 = temls2.replace("[shwtemplabel='', current=",'')
    temp = temls3.replace(", high=None, critical=None]",'')
    CPU_Temp.set(temp)


def Main():
    
    while True:
        get_ram()
        get_total_ram()
        get_used_ram()
        get_cpu()
        get_temp()
        t.sleep(1)


if __name__ == '__main__':
    prom.start_http_server(7070)
    Main()
