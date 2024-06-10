import time 
import random 

class DataAcquisitionSystem: 

    def __init__(self): 
        self.load_cell_data = [] 
        self.tachometer_data = [] 

    def read_load_cell(self): 
        # Simulate reading from load cell 
        thrust = random.uniform(0, 25)  # Thrust in kg 
        return thrust 

    def read_tachometer(self): 
        # Simulate reading from tachometer 
        rpm = random.uniform(0, 20000)  # RPM 
        return rpm 

    def acquire_data(self, duration): 
        start_time = time.time() 
        while (time.time() - start_time) < duration: 
            thrust = self.read_load_cell() 
            rpm = self.read_tachometer() 
            self.load_cell_data.append(thrust) 
            self.tachometer_data.append(rpm) 
            print(f"Thrust: {thrust} kg, RPM: {rpm}") 
            time.sleep(1)  # Simulate 1 second delay between readings 

    def save_data(self): 
        with open('data.csv', 'w') as file: 
            file.write('Thrust (kg), RPM\n') 
            for thrust, rpm in zip(self.load_cell_data, self.tachometer_data): 
                file.write(f"{thrust}, {rpm}\n") 

# Usage 
data_system = DataAcquisitionSystem() 
data_system.acquire_data(10)  # Acquire data for 10 seconds 
data_system.save_data() 
