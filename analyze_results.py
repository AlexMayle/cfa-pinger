import json

if __name__ == '__main__':
    with open('results.log', 'r') as f:
        lines = f.readlines()

    for i in range(0, len(lines), 2):
        line = lines[i]
        ping_result = json.loads(line)
        if ping_result['status'] != 200:
            print(json.dumps(ping_result))
