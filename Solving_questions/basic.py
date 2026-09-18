full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # Name validations
    if not isinstance(name, str):
        return 'The character name should be a string'
    if len(name) == 0:
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

    # Stats validations
    if not all(type(stat) is int for stat in (strength, intelligence, charisma)):
        return 'All stats should be integers'
    if min(strength, intelligence, charisma) < 1:
        return 'All stats should be no less than 1'
    if max(strength, intelligence, charisma) > 4:
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    # Output formatting
    str_line = f"STR {full_dot * strength}{empty_dot * (10 - strength)}"
    int_line = f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}"
    cha_line = f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"

    return f"{name}\n{str_line}\n{int_line}\n{cha_line}"

created_character = create_character("Aragorn", 3, 2, 2)
print(created_character)