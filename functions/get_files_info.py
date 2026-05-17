import os

def list_dir_contents(dir, dir_list):
    if len(dir_list) == 0:
        return ""
    return (
            f"  -{dir_list[0]}: "
            f"file_size={os.path.getsize(os.path.join(dir, dir_list[0]))} bytes, "
            f"is_dir={os.path.isdir(os.path.join(dir, dir_list[0]))}\n" +
            list_dir_contents(dir, dir_list[1:])
    )

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
    except:
        return (
            f"\n"
            f"Error: \"{working_directory}\" is not a directory"
        )

    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = None
    if os.path.isdir(target_dir):
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    else:
        return (
            f"\n"
            f"Results for \"{directory}\" directory:\n"
            f"  Error: \"{directory}\" is not a directory\n"
        )

    if valid_target_dir and directory == ".":
        return (
            f"\n"
            f"Result for current directory:\n"
            f"  Success: \"{directory}\" is within the working directory\n" +
            list_dir_contents(target_dir, os.listdir(target_dir))
        )
    elif valid_target_dir:
        return (
            f"\n"
            f"Result for \"{directory}\" directory:\n"
            f"  Success: \"{directory}\" is within the working directory\n" +
            list_dir_contents(target_dir, os.listdir(target_dir))
        )
    else:
        return (
            f"\n"
            f"Results for \"{directory}\" directory:\n"
            f"  Error: Cannot list \"{directory}\" as it is outside the working directory\n"
        )
