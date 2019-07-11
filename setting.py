import json
import argparse


def save_data(room: dict) -> None:
    results_path = 'result.json'
    with open(results_path, 'a+') as json_file:
        json_file.write(json.dumps(room, indent=4) + ',\n')


def input_args() -> list:
    parse = argparse.ArgumentParser(description="Input")
    parse.add_argument('--id', type=str, default=0)
    parse.add_argument('--way', type=str, default='noname')
    parse.add_argument('--testing_flag', type=str, default=True)

    args = parse.parse_args()

    if args.testing_flag:
        return [str(i + 8342037) for i in range(100)]
    return [args.id, args.way]


def condition(id, way):
    if id is 0:
        return [way]
    elif way == 'noname':
        return [id]
    else:
        return [way, id]

