import json


def get_script_text(path):
    with open(path, 'r') as f:
        information = json.load(f)
    return information












if __name__ == '__main__':
    path = '../Joker.txt'
    script_text = get_script_text(path)
