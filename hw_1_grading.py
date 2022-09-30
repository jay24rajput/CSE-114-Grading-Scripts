

import os.path
import subprocess
from subprocess import STDOUT, PIPE
from sys import stdout
from tabnanny import check
import zipfile


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def check_question(output):
    print(output)


def compile_java(java_file):
    try:
        subprocess.check_call(['javac', java_file])
    except:
        print(f"{bcolors.FAIL}Compile error{bcolors.ENDC}")
        return False
    return True


def execute_java(java_file, stdin, files):
    # java_class,ext = os.path.splitext(java_file)
    cmd = ['java', java_file]
    try:
        proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        stdout, stderr = proc.communicate(stdin)
        stdout = stdout.decode('utf-8')
        check_question(stdout)
    except:
        print("Runtime Error")


files = ['hw1q1.java', 'reward_points.java', 'hw1q3.java', 'ForeignMoney.java']
params = [
    [
        'steak\nguacamole\nyes',
        'chicken\nsalsa\nno',
        'veggie\nbeans\nhuh?',
        'steak\ncheese\nyes',
        'chicken\nsalsa\nyes',
        'veggie\nsalsa\nyes'

    ],
    [
        'gas 210 19',
        'dining 75 12',
        'groceries 67 22',
        'travel 400 19',
        'dining 155 13',
        'electronics 1400, 110',
        'gas 22 12',
        'groceries 225 30'
    ],
    [
        '10000 8840 7800 7800',
        '5600 3840 2800 0',
        '6700 4500 0 0',
        '5600 0 0 0'
    ],
    [
        '59457'
    ]
]

expected = [
    "14.15\n10.10\n8.85\n11.65\n12.05\n12.55",
    "34\n19\n25\n23\n33\n129\n13\n46",
    "9420.00\n4406.40\n4032.00\n2016.00",
    "The number of dots is the same as:\n3 bricks\n15 stacks\n9 lines\n3 dots"
]

for index, file in enumerate(files):
    print(f"{bcolors.HEADER}--------------Grading file " +
          file + f"------------------{bcolors.ENDC}")
    success = compile_java(file)
    if success:
        for param in params[index]:
            execute_java(file, param.encode(), files)

    print(f"{bcolors.OKBLUE}Expected:{bcolors.ENDC}")
    print(expected[index])
