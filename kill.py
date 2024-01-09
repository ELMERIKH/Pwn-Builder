import psutil
import time
import threading

def terminate_process_by_name(process_name, duration):
    start_time = time.time()
    
    while time.time() - start_time < duration:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                pid = process.info['pid']
                
                p = psutil.Process(pid)
                p.terminate()
                print(f"Terminated process '{process_name}' with PID {pid}")
        
        # Adjust the sleep interval as needed
        time.sleep(1)  # Sleep for 1 second before checking again

# Run the 

def terminate_after_timeout(process_name, timeout):
    time.sleep(timeout)
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            pid = process.info['pid']
            try:
                p = psutil.Process(pid)
                p.terminate()
                print(f"Terminated process '{process_name}' with PID {pid}")
            except psutil.NoSuchProcess:
                print(f"Process '{process_name}' with PID {pid} not found")

MAX_RUNNING_TIME = 200

# Create threads for each function
terminate_process_by_name('Taskmgr.exe',180)


terminate_process_thread_2 = threading.Thread(target=terminate_process_by_name, args=('mmc.exe',180))
terminate_process_thread_2.start()

terminate_after_timeout_thread = threading.Thread(target=terminate_after_timeout, args=('007.exe', MAX_RUNNING_TIME))
terminate_after_timeout_thread.start()

# Wait for all threads to finish
