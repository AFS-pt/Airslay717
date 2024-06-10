import matplotlib.pyplot as plt 
import numpy as np 
import time 

# Placeholder functions for reading from the load cell and tachometer (this data is all simulated)
def read_load_cell(): 
    return np.random.uniform(0, 10) 

def read_tachometer(): 
    return np.random.uniform(1000, 5000) 

# Lists to store the data 
thrust_data = [] 
rpm_data = [] 
time_data = [] 

# Time duration for the test 
duration = 60  # seconds 
start_time = time.time() 

# Data acquisition loop 
while time.time() - start_time < duration: 
    thrust = read_load_cell() 
    rpm = read_tachometer() 

    thrust_data.append(thrust) 
    rpm_data.append(rpm) 
    time_data.append(time.time() - start_time) 

    # Adjustment the sleep time based on desired sampling rate 
    time.sleep(0.5) 
  
# Convert lists to numpy arrays for easier manipulation 
thrust_data = np.array(thrust_data) 
rpm_data = np.array(rpm_data) 
time_data = np.array(time_data) 

# Plotting the thrust vs RPM graph 
plt.figure(figsize=(10, 5)) 
plt.plot(time_data, thrust_data, label='Thrust (N)') 
plt.plot(time_data, rpm_data, label='RPM') 
plt.xlabel('Time (s)') 
plt.ylabel('Value') 
plt.title('Thrust and RPM over Time') 
plt.legend() 
plt.grid(True) 
plt.show()  
