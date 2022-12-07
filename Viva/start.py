import os
import shutil

dek_path = os.path.expanduser("~\\Desktop")

def find_viva(d_path):

    if "Vivo" in os.listdir(d_path):
        return d_path + "/Vivo"
    else:
        shutil.copytree("./Vivo", f"{d_path}/Vivo")
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
        load_backup(path)

    else:
        os.mkdir(f"{path}/backup")
        c_2369(path)



while True:
    try:

        try:
            backup_check(find_viva(dek_path))

        except:
            backup_check(find_viva(dek_path))
    except:
        backup_check(find_viva(dek_path))
