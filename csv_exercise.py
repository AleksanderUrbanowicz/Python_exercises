import os, random, string, csv
import os_exercise

names = ['John', 'Chris', 'Elliot', 'Carla', 'Perry']
surnames = ['Dorian', 'Turk', 'Reed', 'Espinoza', 'Cox']


def fill_csv_file(path_to_dir, file, lines):
    try:
        os.chdir(path_to_dir)
    except FileNotFoundError:
        os_exercise.create_dir(path_to_dir)
    os_exercise.create_file(path_to_dir, file)
    with open(file, 'w+') as f:
        print(f.name)
        entry = ['name', 'surname', 'code', 'age']
        header = ','.join(entry)
        f.write(header + '\n')
        for x in range(lines):
            name = random.choice(names)
            surname = random.choice(surnames)
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            age = random.randrange(100)
            entry = [name, surname, code, str(age)]
            line = ','.join(entry)
            print(line)
            f.write(line + '\n')


def read_csv_file(delimit=','):
    try:
        os.chdir(dir_path)
    except FileNotFoundError:
        os_exercise.create_dir(dir_path)
        os.chdir(dir_path)

    if not os.path.isfile(file_name):
        fill_csv_file(dir_path, file_name)

    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimit)
        fieldnames = ['name', 'age']
        # csv_dict_reader = csv.DictReader(csv_file, delimiter=delimit)
        with open('newCsvFile.txt', 'w') as new_file:
            # fieldnames = ['name', 'age']
            csv_writer = csv.writer(new_file, delimiter='\t')

            for line in csv_reader:
                csv_writer.writerow(line)

        # for entry in csv_dict_reader:
        #     print(entry)


if __name__ == "__main__":
    dir_path = os.path.join(os.environ.get('HOME'), 'Desktop/Test/')
    file_name = 'testCsvFile.txt'
    fill_csv_file(dir_path, file_name, 20)
    read_csv_file()
