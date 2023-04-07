import json


def operations_data():
    with open("operations.json", 'r', encoding="utf-8") as file:
        raw_json = file.read()
        all_operations = json.loads(raw_json)

    max_data = []
    for operation in all_operations:
        if "date" in operation:
            if operation["state"] == "EXECUTED":
                data_operations = operation['date']
                max_data.append(data_operations)
            else:
                continue
        else:
            continue

    sorted_data = sorted(max_data)
    last_operations = 1
    user_need_operation = int(input("Сколько последних выполненных операций показать? "))
    while True:
        if user_need_operation == 0:
            break
        else:
            for operation in all_operations:
                if "date" in operation:
                    if operation['date'] in sorted_data[-last_operations]:
                        print('')
                        name_to = f"{''.join(i for i in operation['to'].split(' ')[:-1])} " \
                                  f"**{''.join(i for i in operation['to'].split(' ')[-1][-4:])}"
                        summ_amount = operation['operationAmount']['amount']
                        currency_name = operation['operationAmount']['currency']['name']
                        date = f"{operation['date'][8:10]}.{operation['date'][5:7]}.{operation['date'][0:4]}"
                        description = operation['description']
                        if "from" in operation:
                            data_from = operation["from"].split(' ')
                            if len(data_from[-1]) == 16:
                                name_from = " ".join(i for i in data_from[:-1])
                                number_from = f"{''.join(i for i in data_from[-1][0:4])} " \
                                              f"{''.join(i for i in data_from[-1][4:6])}" \
                                              f"** **** {''.join(i for i in data_from[-1][-4:])}"
                            else:
                                name_from = " ".join(i for i in data_from[:-1])
                                number_from = f"**{''.join(i for i in data_from[-1][-4:])}"
                        else:
                            name_from = None
                            number_from = None
                        if name_from:
                            print(f"{date} {description} \n{name_from} {number_from}"
                                  f" -> {name_to}\n{summ_amount} {currency_name}")
                            user_need_operation -= 1
                            last_operations += 1
                        else:
                            print(f"{date} {description}\n"
                                  f"{name_to}\n{summ_amount} {currency_name}")
                            user_need_operation -= 1
                            last_operations += 1


operations_data()
