# Define a class named TV
class TV:
    # Constructor method that initializes the atributes of tv
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1  # Default channel is 1
        self.volume = 50  # Default volume is 50
        self.inches = None  # Placeholder for screen size, can be set in subclasses
        self.price = None  # Placeholder for price, can be set in subclasses
        self.on = False  # TV is initially turned off
    # Method to dec vol
    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
    # Method to inc vol
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
    # Method to set channels
    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
    # Method to reset the tv 
    def reset_tv(self):
        self.channel = 1
        self.volume = 50
    # Method to power on
    def toggle_power(self):
        self.on = not self.on

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

# Example usage of TV class
tv = TV("Panasonic")
print(tv.status())  # Output: Panasonic at channel 1, volume 50
tv.increase_volume()
tv.set_channel(8)
print(tv.status())  # Output: Panasonic at channel 8, volume 51
tv.reset_tv()
print(tv.status())  # Output: Panasonic at channel 1, volume 50

# Inherited a TV class named LedTV
class LedTV(TV):
    # Constructor method that initializes the additional atributes of tv
    def __init__(self, brand, inches, price, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.inches = inches
        self.price = price
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
    # Method to display details 
    def display_details(self):
        return f"{self.brand} LED TV: {self.inches} inches, ${self.price}, {self.refresh_rate}Hz Refresh Rate"

#  Inherited a TV class named PlasmaTV
class PlasmaTV(TV):
    # Constructor method that initializes the additional atributes of tv
    def __init__(self, brand, inches, price, energy_usage, lifespan, viewing_angle, backlight):
        super().__init__(brand)
        self.inches = inches
        self.price = price
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.viewing_angle = viewing_angle
        self.backlight = backlight
    # Method to display details
    def display_details(self):
        return f"{self.brand} Plasma TV: {self.inches} inches, ${self.price}, {self.viewing_angle} Viewing Angle"


# Example usage of LedTV and PlasmaTV subclasses
led_tv = LedTV("Sony", 55, 1500, "Slim", "Low", "10 years", 120)
plasma_tv = PlasmaTV("Samsung", 60, 2000, "High", "12 years", "160°", "Yes")

# Output: Sony at channel 1, volume 50
print(led_tv.status()) 
# Output: Sony LED TV: 55 inches, $1500, 120Hz Refresh Rate 
print(led_tv.display_details())  

# Output: Samsung at channel 1, volume 50
print(plasma_tv.status())  
# Output: Samsung Plasma TV: 60 inches, $2000, 160° Viewing Angle
print(plasma_tv.display_details())  
