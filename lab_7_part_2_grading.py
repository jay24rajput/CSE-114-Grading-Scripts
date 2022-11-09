

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


def check_question_1(output):
    # output = output.split('\n')
    # if len(output) == 4:
    #     print(output[2])
    # else:
    print(output)


def check_question_2(output):
    # output = output.split('\n')
    # if len(output) == 4:
    #     print(output[1])
    # else:
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
        if java_file == files[0]:
            check_question_1(stdout)

        elif java_file == files[1]:
            check_question_2(stdout)
    except:
        print("Runtime Error")


files = ['Lab7_P2_1.java', 'Lab7_P2_2.java']
params = [
    [
        '3 40',
        '3.5 35.9'
    ],
    [
        '1.0 3 1',
        '1 2.0 1',
        '1 2 3'
    ]
]
expected = [
    "Area:160\nPerimenter:88\n\nArea:125.65\nPerimeter:78.8",
    "The equation has two roots -0.381966 and -2.61803\nThe equation has one root -1.0\nThe equation has no real roots."
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
