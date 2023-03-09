class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

def generate(player_count):
    players = [
        Player('Aziel'),
        Player('Carter'),
        Player('Chad'),
        Player('Eli'),
        Player('Elijah'),
        Player('Grayson'),
        Player('Hoku'),
        Player('Julian'),
        Player('Kamuela'),
        Player('Koa'),
    ]
    return players
