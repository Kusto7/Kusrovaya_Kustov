import json

with open("operations.json", 'r', encoding="utf-8") as file:
    raw_json = file.read()
    all_operations = json.loads(raw_json)


def operations_data():
    pass


last_operations = 5

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
for operation in all_operations:
    if "date" in operation:
        if operation['date'] in sorted_data[:-5-1:-1]:
            if last_operations == 0:
                break
            else:
                print('')
                name_to = f"{''.join(i for i in operation['to'].split(' ')[:-1])} " \
                          f"**{''.join(i for i in operation['to'].split(' ')[-1][-4:])}"
                summ_amount = operation['operationAmount']['amount']
                currency_name = operation['operationAmount']['currency']['name']
                date_ = f"{operation['date'][0:4]}.{operation['date'][5:7]}.{operation['date'][8:10]}"
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
                    number_from = ''

            print(f'''{date_} {description}
{name_from} {number_from} -> {name_to}
{summ_amount} {currency_name}''')
