import os, json, datetime

class Logger:
    @staticmethod
    def log(message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")

class Auto:
    def __init__(self, ID, doors, brand):
        self.ID = ID
        self.doors = doors
        self.brand = brand

class Bicikli:
    def __init__(self, ID, load_capacity, brand):
        self.ID = ID
        self.load_capacity = load_capacity
        self.brand = brand

def read_files(folder_path):
    vehicles = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as file:
                data = json.load(file)
                data["ID"] = file_name

                ID = data.get("ID", "")
                brand = data.get("marka", "")

                if data["type"] == "auto":
                    doors = data.get("ajtok_szama", 0)
                    vehicle = Auto(ID, doors, brand)
                elif data["type"] == "bicikli":
                    load_capacity = data.get("terhelhetoseg", 0)
                    vehicle = Bicikli(ID, load_capacity, brand)
                else:
                    raise ValueError(f"Unknown vehicle type: {data['type']}")
                
                vehicles.append(vehicle)
                Logger.log(f"Processed file: {file_name}")

    return vehicles

def main():
    print("Program is running...")
    folder_path = "data"
    vehicles = read_files(folder_path)

    print("\nVehicles:")
    for vehicle in vehicles:
        print("-" * 30)
        print(f"ID: {vehicle.ID}")
        print(f"Type: {'Auto' if isinstance(vehicle, Auto) else 'Bicikli'}")
        print(f"Brand: {vehicle.brand}")

        if isinstance(vehicle, Auto):
            print(f"Number of Doors: {vehicle.doors}")
        elif isinstance(vehicle, Bicikli):
            print(f"Load Capacity: {vehicle.load_capacity}")

    print("\nProgram finished.")

if __name__ == "__main__":
    main()


