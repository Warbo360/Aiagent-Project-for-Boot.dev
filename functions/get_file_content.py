import os
from config import *

def read_file_contents(file_path):
    with open(file_path, "r") as file:
        file_content_string = file.read(MAX_CHARS)
        if file.read(MAX_CHARS + 1):
            file_content_string += f"[...File \"file_path\" truncated at {MAX_CHARS} characters]"
    return (
            f"\n"
            f"---- Start of File Contents ----"
            f"\n" +
            file_content_string +
            f"\n"
            f"---- End of File Contents ----"
    )

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
    except:
        return (
            f"\n"
            f"Error: \"{working_directory}\" is not a directory"
        )

    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file = None
    if os.path.isfile(target_file):
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    else:
        return (
            f"\n"
            f"Results for \"{file_path}\" file:\n"
            f"  Error: File not found or is not a regular file: \"{file_path}\"\n"
        )

    if valid_target_file:
        return (
            f"\n"
            f"Result for \"{file_path}\" file:\n"
            f"  Success: \"{file_path}\" is within the working directory\n" +
            read_file_contents(target_file)
        )

    else:
        return (
            f"\n"
            f"Results for \"{file_path}\" file:\n"
            f"  Error: Cannot read \"{file_path}\" as it is outside the permitted working directory\n"
        )
