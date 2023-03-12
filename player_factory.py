from positional_data import FieldGroup


class Player:
    def __init__(self, name, field_group):
        self.name = name
        self.field_group = field_group
        self.bench_count = 0
        self.consecutive_innings = 0

    def __str__(self):
        return f"{self.name}"

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash((self.name, self.field_group))


def generate_full_cardinals():
    players = [
        Player('Azriel', FieldGroup.OF),
        Player('Carter', FieldGroup.IF),
        Player('Chad', FieldGroup.OF),
        Player('Eli', FieldGroup.OF),
        Player('Elijah', FieldGroup.IF),
        Player('Grayson', FieldGroup.IF),
        Player('Hoku', FieldGroup.OF),
        Player('Julian', FieldGroup.OF),
        Player('Kamuela', FieldGroup.IF),
        Player('Koa', FieldGroup.OF),
        Player('Mason', FieldGroup.IF),
        Player('Peyton', FieldGroup.IF),
        Player('Rhaeden', FieldGroup.IF),
        Player('Roman', FieldGroup.OF),
    ]
    return players


def format_raw_input(raw_input):
    raw_input = raw_input.lower()
    raw_input = raw_input.replace(" ","")
    return list(map(str, raw_input.split(',')))


def generate_available_players(raw_input):
    missing_players = format_raw_input(raw_input)
    available_players = generate_full_cardinals()
    if len(missing_players) < 1:
        return available_players
    for name in missing_players:
        player = next((p for p in available_players if p.name.lower() == name), None)
        available_players.remove(player)

    return available_players
