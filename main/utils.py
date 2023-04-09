import json


def load_data():
    with open("operations.json", 'r', encoding="utf-8") as file:
        all_operations = json.load(file)
    return all_operations


def sorted_data(all_operations):
    data = []
    for operation in all_operations:
        if "date" in operation:
            if operation["state"] == "EXECUTED":
                data.append(operation)
    data = sorted(data, key=lambda operation: operation["date"], reverse=True)
    return data


def formatted_data(operation):
    date = f"{operation['date'][8:10]}.{operation['date'][5:7]}.{operation['date'][0:4]}"
    if operation.get("from"):
        number_card = mask_card(operation["from"]) + ' -> '
    else:
        number_card = ''
    number_to = mask_card(operation["to"])

    return f'{date} {operation["description"]}\n' \
           f'{number_card}{number_to}\n' \
           f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n'


def mask_card(card):
    card = card.split(' ')
    if len(card[-1]) == 16:
        card = f"{' '.join(i for i in card[:-1])} " \
               f"{''.join(i for i in card[-1][0:4])} " \
               f"{''.join(i for i in card[-1][4:6])}" \
               f"** **** {''.join(i for i in card[-1][-4:])}"
        return card
    else:
        card = f"{''.join(i for i in card[:-1])} **{''.join(i for i in card[-1][-4:])}"
        return card
