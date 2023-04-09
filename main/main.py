from utils import load_data, formatted_data, sorted_data

JSON_OPERATION = 'operations.json'


def main():
    data = load_data(JSON_OPERATION)
    data = sorted_data(data)

    for i in range(5):
        print(formatted_data(data[i]))


if __name__ == '__main__':
    main()
