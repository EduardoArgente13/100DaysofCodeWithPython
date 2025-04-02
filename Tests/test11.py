class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType] > 0:
            self.spaces[carType] -= 1
            return True
        else:
            return False

# Example usage:
parking_system = ParkingSystem(1, 1, 0)
print(parking_system.addCar(1))  # True
print(parking_system.addCar(2))  # True
print(parking_system.addCar(3))  # False
print(parking_system.addCar(1))  # False