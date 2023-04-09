from utils import load_data, formatted_data, sorted_data


def main():
    data = load_data()
    data = sorted_data(data)

    for i in range(5):
        print(formatted_data(data[i]))


if __name__ == '__main__':
    main()
