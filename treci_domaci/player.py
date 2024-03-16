class Player:
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_health(self):
        return self.health

    def set_health(self, health):
        if 0 <= health <= 100:
            self.health = health


class Enemy:
    def __init__(self, x, y, width, height, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.damage = damage

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        if 0 <= damage <= 100:
            self.damage = damage


def check_collision(player, enemy):
    player_x, player_y = player.get_x(), player.get_y()
    player_width, player_height = player.get_width(), player.get_height()
    enemy_x, enemy_y = enemy.get_x(), enemy.get_y()
    enemy_width, enemy_height = enemy.get_width(), enemy.get_height()

    if (player_x < enemy_x + enemy_width and
            player_x + player_width > enemy_x and
            player_y < enemy_y + enemy_height and
            player_y + player_height > enemy_y):
        return True
    else:
        return False


def decrease_health(player, enemy):
    if check_collision(player, enemy):
        player.set_health(player.get_health() - enemy.get_damage())


player1 = Player(100, 100, 50, 50, 100)
enemy1 = Enemy(200, 200, 30, 30, 20)
enemy2 = Enemy(150, 150, 40, 40, 30)

decrease_health(player1, enemy1)
print("Player's health after collision with enemy1:", player1.get_health())
decrease_health(player1, enemy2)
print("Player's health after collision with enemy2:", player1.get_health())
