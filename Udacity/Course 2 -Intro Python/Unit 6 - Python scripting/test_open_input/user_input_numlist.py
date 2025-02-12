scientist_dict = {}

def create_scientist_dict():
    my_dict = {}
    try:
        with open('scientists.txt', 'r') as file:
            for line in file:
                kvp = line.split(':')
                my_dict[kvp[0]] = kvp[1]
            return my_dict
    except FileNotFoundError as fnf:
        print(f'Couldn\'t find the file!: {fnf}')
    except Exception as e:
        print(f'This is the exception: {e}')


def get_scientist_name(sci_dict):
    try:
        while True:
            full_name = input('Please enter a first and last name: ')
            upper_first = full_name[0].upper()
            sci_name = sci_dict.get(upper_first)
            if sci_name == None:
                print('A scientist with that first initial is not found. Try again.')
                continue
            else:
                print(sci_name)
                break
    except Exception as e:
        print(f'This is the exception: {e}')

def main():
    scientist_dict = create_scientist_dict()
    get_scientist_name(scientist_dict)

if __name__ == '__main__':
    main()