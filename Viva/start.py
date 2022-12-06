import os
import shutil


def find_viva():

    dek_path = os.path.expanduser("~\\Desktop")
    print(dek_path)

    if "Vivo" in os.listdir(dek_path):
        return dek_path + "/Vivo"
    else:
        shutil.copytree("./Vivo", f"{dek_path}/Vivo")
        find_viva()





def load_backup(path):

    for root, dirs, files in os.walk(f'{path}/backup'):

        for file in files:
            shutil.copyfile(f"{path}/backup/{file}", f"{path}/{file.split('.')[0]}.py")


def c_2369(path):

    if "extent" not in os.listdir("./"):
        os.mkdir("./extent")

    for dirr in os.listdir("./extent"):

        for file in os.listdir(f"./extent/{dirr}"):
            shutil.copyfile(f"./extent/{dirr}/{file}", f"{path}/{file.split('.')[0]}.py")


def backup_check(path):

    if "backup" in os.listdir(path):
        load_backup(THE_PATH)

    else:
        os.mkdir(f"{path}/backup")
        c_2369(THE_PATH)

THE_PATH = find_viva()
while True:

    try:
        backup_check(THE_PATH)

    except:
        backup_check(THE_PATH)
