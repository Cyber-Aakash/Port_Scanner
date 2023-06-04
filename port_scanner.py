import socket
import argparse
import signal
import sys
from threading import Thread, Lock
from queue import Queue
from datetime import datetime
import time
from colorama import init, Fore

init()
green = Fore.GREEN
gray = Fore.LIGHTBLACK_EX
reset =  Fore.RESET

N_Threads = 100
queue = Queue()
lock = Lock()

space = ' '


def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        sock.connect((host,port))
        
    except:
        pass
    else:
        with lock:
            service = socket.getservbyport(port,"tcp")
            status = "Open"
            print(f"{green}{port:3} {space*7} {status} {space*7} {service}{reset}")
    finally:
        sock.close()
        

def scan_thread():
    global queue
    while True:
        worker = queue.get()
        scan_port(worker)
        queue.task_done()


print("\n[*] Scanning Started at %s....\n"%(time.strftime("%H:%M:%S")))

start_time = datetime.now()

def signal_handler(signal,frame):
    print("\n\n[*]User Requested Interrupt")
    print("[*]Application Stopped.")
    sys.exit(0)
    
signal.signal(signal.SIGINT,signal_handler)

def main(host,ports):
    print("\n[*] Host : ",host)
    hostbyname = host
    IP = socket.gethostbyname(hostbyname)
    print("\n[*] IP Address : ",IP)
    print("\n","Port", space*5, "Status", space*5, "Services", "\n")
    try:
        global queue
        for p in range(N_Threads):
            p = Thread(target=scan_thread)
            p.daemon = True
            p.start()
                
        for worker in ports:
            queue.put(worker)
            
        queue.join()
        
    except Exception as e:
        print("An error occurred : ",str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Port Scanner by TheAJ")
    parser.add_argument("host",help="Host to Scan.")
    parser.add_argument("--ports","-p",dest="port_range", default="1-65535",help="Port range to scan, default is 1-65535 (all ports)")
    parser.add_argument("--threads","-t",dest="threads",default="100",help="By default thread is 100 you can edit using --threads option")
    args = parser.parse_args()
    host,port_range,threads = args.host, args.port_range, args.threads
    
    start_port, end_port =  port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)
    ports = [p for p in range(start_port, end_port)]

    
    main(host,ports)
    

stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("\n\n[*] Scanning Completed at %s....\n"%(time.strftime("%H:%M:%S")))
print("[*] Scan Time : ",total_time_duration)
print("[*] Scan Completed Successfully.")