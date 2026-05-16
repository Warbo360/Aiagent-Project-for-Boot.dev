import os

def get_files_info(working_directory, directory="."):

    try:
        working_dir_abs = os.path.abspath(working_directory)
    except:
        return f"Error: \"{working_directory}\" is not a directory"

    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = None
    if os.path.isdir(target_dir):
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    else:
        return f"Error: \"{directory}\" is not a directory"

    if valid_target_dir:
        return f"Success: \"{directory}\" is within the working directory"
    else:
        return f"Error: Cannot list \"{directory}\" as it is outside the working directory"
