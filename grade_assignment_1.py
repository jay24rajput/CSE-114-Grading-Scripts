

import os.path,subprocess
from subprocess import STDOUT,PIPE
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
    answer = output.split(' ')[-1]
    print(answer)

def check_question_2(output):
    answer = output.split(' ')[-1]
    print(answer)

def check_question_3(output):
    for index, char in enumerate(output):
        if char.isnumeric():
            break
    print(output[index:])

def check_question_4(output):
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
        stdout,stderr = proc.communicate(stdin)
        stdout = stdout.decode('utf-8')
        if java_file == files[0]:
            check_question_1(stdout)

        elif java_file == files[1]:
            check_question_2(stdout)

        elif java_file == files[2]:
            check_question_3(stdout)

        elif java_file == files[3]:
            check_question_4(stdout)
    except:
        print("Runtime Error")


# success = compile_java('Lab2Q1.java')
# files = os.listdir()
# for file in files:
#     if file.endswith('.zip'):
#         zipped_file = file
#         break

# with zipfile.ZipFile(zipped_file, 'r') as zip_ref:
#     zip_ref.extractall()

# os.chdir(zipped_file.split('.')[0])


files = ['GetEnergy.java', 'GetAcceleration.java', 'GetFarenheit.java','GetSchedule.java']
params = ['55.5 3.5 10.5', '5.5 50.9 4.5','43.5', '']
for index, file in enumerate(files):
    print(f"{bcolors.HEADER}--------------Grading file "+ file + f"------------------{bcolors.ENDC}")
    success = compile_java(file)
    if success:
        execute_java(file, params[index].encode(), files)