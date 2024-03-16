class Color:
    def __init__(self, red, green, blue):
        self.red = self.validate_color(red)
        self.green = self.validate_color(green)
        self.blue = self.validate_color(blue)

    def validate_color(self, value):
        if 0 <= value <= 255:
            return value
        else:
            print("Invalid color value. Value should be between 0 and 255.")
            return 0

    def get_red(self):
        return self.red

    def set_red(self, red):
        self.red = self.validate_color(red)

    def get_green(self):
        return self.green

    def set_green(self, green):
        self.green = self.validate_color(green)

    def get_blue(self):
        return self.blue

    def set_blue(self, blue):
        self.blue = self.validate_color(blue)

    def add_red(self, change):
        new_red = self.red + change
        if 0 <= new_red <= 255:
            self.red = new_red
        else:
            print("Red color value out of range (0-255).")

    def add_green(self, change):
        new_green = self.green + change
        if 0 <= new_green <= 255:
            self.green = new_green
        else:
            print("Green color value out of range (0-255).")

    def add_blue(self, change):
        new_blue = self.blue + change
        if 0 <= new_blue <= 255:
            self.blue = new_blue
        else:
            print("Blue color value out of range (0-255).")

    def __lt__(self, other):
        return self.red < other.get_red() and self.green < other.get_green() and self.blue < other.get_blue()

    def __eq__(self, other):
        return self.red == other.get_red() and self.green == other.get_green() and self.blue == other.get_blue()

    def __str__(self):
        return f"\"red\": {self.red}, \"green\": {self.green}, \"blue\": {self.blue}"


class AlphaColor(Color):
    def __init__(self, red, green, blue, alpha):
        super().__init__(red, green, blue)
        self.alpha = self.validate_alpha(alpha)

    def validate_alpha(self, value):
        if 0 <= value <= 1:
            return value
        else:
            print("Invalid alpha value. Value should be between 0 and 1.")
            return 0

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = self.validate_alpha(alpha)

    def update_color_by_alpha(self, alpha):
        self.set_red(self.get_red() * (1 - alpha))
        self.set_green(self.get_green() * (1 - alpha))
        self.set_blue(self.get_blue() * (1 - alpha))

    def __str__(self):
        return f"\"red\": {self.get_red()}, \"green\": {self.get_green()}, \"blue\": {self.get_blue()}, \"alpha\": {self.get_alpha()}"


color1 = Color(100, 150, 200)
color2 = Color(50, 100, 150)

print(color1 < color2)
print(color2 < color1)
print(color1 == color2)

print(color1)
print('--------------------------------------------')
alpha_color1 = AlphaColor(100, 150, 200, 0.5)
alpha_color2 = AlphaColor(50, 100, 150, 0.7)

print(alpha_color1)
print(alpha_color2)

alpha_color1.update_color_by_alpha(0.2)
alpha_color2.update_color_by_alpha(0.5)

print(alpha_color1)
print(alpha_color2)
