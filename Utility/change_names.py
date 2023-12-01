import os

def rename_files(folder_path):
    files = os.listdir(folder_path)
    counter = 760
    for file_name in files:
        new_name = str(counter) + os.path.splitext(file_name)[1] 
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        counter += 1

if __name__ == "__main__":
    folder_path = "./dataset/Train/Normal"
    rename_files(folder_path)
