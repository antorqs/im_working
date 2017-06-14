import random
import time
import glob

upper_limit = 30
jump = 1
logs_folder = "/var/log"
head_size = 15
speed = 2

def head_log():
    file_list = glob.glob(logs_folder + "/*.log")
    file_path = file_list[random.randrange(0, len(file_list))]
    try:
        with open(file_path) as file:
            head = [next(file) for x in range(head_size)]
        for line in head:
            print(line.replace("\n", ""))
    except:
        print("Continue...")
    print("\n\n")


def print_progess():
    for ii in range(0, upper_limit):
            time.sleep(random.random() / speed)
            if ii % jump == 0 or ii == upper_limit - 1:
                progress = int((ii+1)*100/upper_limit)
                print("\r[{}{}]{}%".format("#" * progress, "." * (100 - progress), progress), end="")
    print("\n")

while True:
    head_log()
    print_progess()
    
