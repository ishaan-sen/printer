import requests
from sys import argv

def move_gantry(x=None, y=None, f=2000):
    cmd = "G1"
    if x is not None:
        cmd += f" X{x}"
    if y is not None:
        cmd += f" Y{y}"
    cmd += f" F{f}"

    url = "http://raspberrypi/printer/gcode/script"
    headers = {"Content-Type": "application/json"}
    data = {"script": cmd}

    response = requests.post(url, headers=headers, json=data)

    return (response.status_code, response.text)

def set_abs_pos(x=None, y=None, f=2000):
    cmd = "G90"
    url = "http://raspberrypi/printer/gcode/script"
    headers = {"Content-Type": "application/json"}
    data = {"script": cmd}

    response = requests.post(url, headers=headers, json=data)

    return (response.status_code, response.text)

if __name__ == "__main__":
    print(set_abs_pos())
    print(move_gantry(x=int(argv[1]), y=argv[2]))

