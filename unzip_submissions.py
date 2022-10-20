from zipfile import ZipFile
import re
from io import BytesIO
from os import path, getcwd, walk

ZIP_NAME = 'submissions.zip'
FB_TEMPLATE_NAME = 'example_feedback_template.txt'


class ZipFileNameFound(Exception):
    def __init__(self, error):
        self.__error = error

    def __str__(self):
        return self.__error

def open_zip_file(zip_file_name):
    try:
        return ZipFile(zip_file_name, "r")
    except FileNotFoundError:
        raise ZipFileNameFound(f"No zip file '{zip_file_name}' was found in {getcwd()}")

def get_student_name(name):
    return name.split("_")[0]

def get_student_dir_path(base_path, extension_path):
    return path.join(base_path, extension_path)

def is_zip_file(file_name):
    return re.search(r'\.zip$', file_name) is not None

def is_pdf_file(file_name):
    return re.search(r'\.pdf$', file_name) is not None


def extract_zip_file(file_name, dir_path, parent_zip_file):
    zip_file_data = BytesIO(parent_zip_file.read(file_name))
    with ZipFile(zip_file_data) as child_zip_file:
        child_zip_file.extractall(dir_path)

def add_template_file(student_name, dir_path, template_str):
    template_feedback_name = f"FEEDBACK_{student_name}"
    with open(f"{path.join(dir_path, template_feedback_name)}.txt", 'w+', encoding='UTF-8') as f:
        f.write(template_str)

def extract_all_zip_files(zip_file, submission_path, template_str=None):
    for file_name in zip_file.namelist():
        student_name = get_student_name(file_name)
        student_dir_path = get_student_dir_path(submission_path, student_name)
        if is_zip_file(file_name):
            extract_zip_file(file_name, student_dir_path, zip_file)
        elif is_pdf_file(file_name):
            zip_file.extract(member=file_name, path=student_dir_path)

        if template_str:
            add_template_file(student_name, student_dir_path, template_str)

def get_sub_folder_path(sub_folder_name):
    return path.join(getcwd(), sub_folder_name,"submissions")

def get_template_text(template_path):
    template_f = open(template_path, 'r+', encoding='UTF-8')
    template_str = "".join(template_f.readlines())
    template_f.close()
    return template_str



def subfolder_exists(cur_dir, sub_folder_name):
    for _, folders, _ in walk(cur_dir):
        if sub_folder_name in folders:
            return True
    return False
        
def get_sub_folder_name():
    while True:
        sub_folder_name = input("Enter the name of the lab/project folder you want to extract: ")
        found = subfolder_exists(getcwd(), sub_folder_name)
        if found:
            return sub_folder_name
        print(f"{sub_folder_name} not found!")

def get_gen_template_input():
    gen_template = input("Do you want to generate from a temaplate feedback file? (y/n): ").lower()
    if gen_template == 'y':
        return True
    return False

if __name__ == "__main__":
    sub_folder_name = get_sub_folder_name()
    should_gen_template = get_gen_template_input()
    zip_path = path.join(getcwd(),sub_folder_name, ZIP_NAME)
    template_path = path.join(getcwd(), sub_folder_name, FB_TEMPLATE_NAME)
    print(zip_path, template_path)
    submission_path = get_sub_folder_path(sub_folder_name)
    print(submission_path)
    template_str = get_template_text(template_path) if should_gen_template else None
    zip_file = open_zip_file(zip_path)
    extract_all_zip_files(zip_file, submission_path, template_str)
    zip_file.close()
    