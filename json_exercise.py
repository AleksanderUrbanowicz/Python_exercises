import random
import json
import os_exercise


def get_test_data():
    json_string = os_exercise.read_text_file(test_file_name)
    return json.loads(json_string)


def save_data_from_dict(data_dict):
    with open('new'+test_file_name, 'w') as f:
        json.dump(data_dict, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    test_file_name = 'JSONTest.json'
    config_file_name = 'config.json'

    # JSON       Python
    # object     dict
    # array      list
    # true       True
    # false      False
    # null       None

    data = get_test_data()
    for state in data['states']:
        state['area'] = random.randrange(100)
        print(state['area'])
    save_data_from_dict(data)
    new_string = json.dumps(data, indent=2, sort_keys=True)
    print(new_string)
