

"""una clase que se puede usar para represntar un coche"""

class Car:      #clase base
    """intento de representar un coche"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """devuelve un nombre descriptivo con el formato adecuado"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """imprime una frase con el kilometraje del coche"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """configura el kilometraje con el valor dado"""
        """rechaza el cambio si se intenta retroceder el cuentakilometros"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("No esta permitido retroceder el cuentakilometros.")
            
    def increment_odometer(self, miles):
        """añade una cantidad dada al cuentakilometros"""
        self.odometer_reading += miles
        
class Battery:
    """intento de modelar una bateria para un coche electrico"""
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"Este coche tiene una bateria de {self.battery_size} kWh.")
        
    def get_range(self):
        if self.battery_size == 75:
            range = 269
        elif self.battery_size == 100:
            range = 315
        print(f"Este tiene una autonomia de {range} millas a plena carga.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
coche = ElectricCar('seat', '600', 1965) 
coche.get_descriptive_name()
print(coche.get_descriptive_name())  
ElectricCar.self.battery.upgrade_battery(100)

        
        
        
        
        
        
        
        
        
        