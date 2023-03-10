from positional_data import FieldGroup


class Player:
    def __init__(self, name, field_group):
        self.name = name
        self.field_group = field_group

    def __str__(self):
        return f"{self.name}"

def generate_full_cardinals():
    players = [
        Player('Aziel', FieldGroup.OF),
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
