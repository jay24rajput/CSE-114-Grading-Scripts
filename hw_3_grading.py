

import os.path
import subprocess
from subprocess import STDOUT, PIPE
from sys import stdout
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
    # output = output.split('\n')
    # if len(output) == 4:
    #     print(output[2])
    # else:
    print(output)


# def check_question_2(output):
#     # output = output.split('\n')
#     # if len(output) == 4:
#     #     print(output[1])
#     # else:
#     print(output)


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


# files = ['Solution_1.java', 'Solution_2.java', 'Solution_3.java', 'Solution_4.java']
files = ['Digits.java', 'Duplicate.java','Interlace.java','SumQ4.java']

params = [
    [
        '1800Flowers',
        '1800FLOWERS',
        '1-CSE-114-JAVA',
        'Seawolf-SBU-1'

    ],
    [
        '1 2 3 2 1 6 3 4 5 2',
        '1 1 1 1 1 1 1 1 1 1',
        '1 1 2 2 3 4 4 5 5 6'
    ],
    [
        ""
    ],
    [
        '-2 13 -1 3 9 5 -9 4 10'
    ]
]
expected = [
    "18003569377\n18003569377\n12731145282\n73296537281",
    "1 2 3 6 4 5\n1\n1 2 3 4 5 6",
    "2,2,6,2,5,4,1,8,4,4\n10,9,8,1,2,3\n2,10,5,5,1,2,4\nnull\nnull",
    "{(-2,3), (-9,10)}"
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
