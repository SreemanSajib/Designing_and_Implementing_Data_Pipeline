

from devices import SmartLight, SmartThermostat, SmartLock


home_devices = []

def perform_operation(device_list):
    
    if not device_list:
        print("No devices found in the system.")
        return

    print("\n#### Operating All Devices ####")
    for device in device_list:
        device.operate()
    print("###############################")

while True:
    print("\n--- Smart Home Menu ---")
    print("1 - Add Smart Device")
    print("2 - Operate Devices")
    print("0 - Exit")

    choice = input("Option select: ")

    try:
        if choice == '1':
          
            print("\nSelect Device Type: 1-Light, 2-Thermostat, 3-Lock")
            dev_type = input("Choice: ")
            name = input("Enter device name: ")

            if dev_type == '1':
                level = int(input("Enter brightness (0-100): "))
                home_devices.append(SmartLight(device_name=name, brightness=level))
                print(f"Light '{name}' is added .")
            
            elif dev_type == '2':
                temp = int(input("Enter target temperature: "))
                home_devices.append(SmartThermostat(device_name=name, temperature=temp))
                print(f"Thermostat '{name}' is added")
            
            elif dev_type == '3':
                home_devices.append(SmartLock(device_name=name))
                print(f"Lock '{name}' is added")
            
            else:
                print("Invalid device type selection.")

        elif choice == '2':
            
            perform_operation(home_devices)

        elif choice == '0':
            
            print("Exiting Smart Home System. Good bye!")
            break
        
        else:
            
            print("Invalid menu choice. Try again!")

    except ValueError:
        
        print("Error: Invalid input format. Please enter numbers where required.")
    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")
