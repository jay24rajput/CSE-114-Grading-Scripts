

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
        'cat\ncatsanddogs\ncats!anddogs',
        'ILoveTreesandeatingicecream\nILovecatsss',
        'VERYCOOLINDEED'
    ],
    [
        '20'
    ]
]
expected = [
    "The password is all lowercase, it must contain the character ! to be secure.\
    \nThe password is too short. Must be at least 10 characters.\
    \nThe password is all lowercase, so it must contain the character ! to be secure.\
    \nYour password cats!anddogs is secure\n\
    The password is long. Must be no more than 20 characters.\
    \nYour password Lovecatsss is secure\
    \nYour password VERYCOOLINDEED is secure",
    "1\t0.5000\
    \n2\t1.1667\
    \n.....\
    \n19\t16.4023\
    \n20\t17.3546"
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
