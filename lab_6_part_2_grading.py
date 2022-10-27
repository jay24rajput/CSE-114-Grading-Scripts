

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


files = ['Q1_1.java', 'Q2_2.java']
params = [
    [
        '9\n1 10 1 0 3 9 5 9 6',
    ],
    [
        '9\n1 -10 1 0 -3 9 5 9 6'
    ]
]
expected = [
    "The dominators are: 10 9",
    "The new array is: -10 -3 0 1 1 9 5 9 6"
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
