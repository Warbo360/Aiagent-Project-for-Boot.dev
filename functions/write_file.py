import os

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
    except:
        return (
            f"\n"
            f"Error: \"{working_directory}\" is not a directory"
        )

    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file = None
    if os.path.isdir(target_file):
        return (
            f"\nResults for \"{file_path}\" file:\n"
            f"  Error: Cannot write to \"{target_file}\" as it is a directory\n"
        )
    else:
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return (
            f"\nResults for \"{file_path}\" file:\n"
            f"  Error: Cannot write to \"{target_file}\" as it is outside the permitted working directory\n"
        )
    else:
        os.makedirs(working_dir_abs, exist_ok=True)
        with open(target_file, "w") as file:
            file.write(content)
        with open(target_file, "r") as file:
            file_content = file.read()
            if content in file_content:
                return (
                    f"\nResults for \"{file_path}\" file:\n"
                    f"  Succesfully wrote to \"{file_path}\" ({len(content)} characters written)\n"
                )
            else:
                return (
                    f"\nResults for \"{file_path}\" file:\n"
                    f"  Error: Writing to \"{file_path}\" failed\n"
                )
