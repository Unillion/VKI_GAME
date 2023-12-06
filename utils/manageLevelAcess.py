
def write_completed_lvl(path2):
    file = open(path2, 'r')
    content = file.read()
    numbers = [int(s) for s in content.split() if s.isdigit()]

    if numbers:
        first = numbers[0]
        new_content = content.replace(str(first), str(first + 1), 1)
        file = open(path2, 'r+')
        file.write(new_content)

def get_level(path2):
    file = open(path2, 'r')
    content = file.read()
    numbers = [int(s) for s in content.split() if s.isdigit()]
    if numbers:
        first = numbers[0]
        return first