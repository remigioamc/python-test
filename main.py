from person import Person
from rate import Rate

def main():
    people = map(lambda x: Person(x), read('people.in'))
    rated = Rate(people).rate_all()
    rated.sort(key=lambda x: x.rate, reverse=True)
    print_out(map(lambda x: x.id + " " + str(x.rate), people), 'people.out', 1000)

def read(file_name):
    with open(file_name) as file:
        return [line[:-2].split("|") for line in file.readlines()]

def print_out(data, out_file, quantity):
        with open(out_file, 'wt') as file:
            [file.write(x+'\n') for x in data[:quantity]]

if __name__ == "__main__":
    main()