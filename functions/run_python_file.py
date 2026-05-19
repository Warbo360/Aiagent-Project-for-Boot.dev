import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
    except:
        return (
            f"\n"
            f"Error: \"{working_directory}\" is not a directory"
        )

    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file = None
    if not os.path.isfile(target_file):
        return (
            f"\nResults for \"{file_path}\" file:\n"
            f"  Error: \"{file_path}\" does not exist or is not a regular file"
        )
    elif not file_path.endswith("py"):
        return (
            f"\nResults for \"{file_path}\" file:\n"
            f"  Error: \"{file_path}\" is not a Python file"
        )
    else:
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return (
            f"\nResults for \"{file_path}\" file:\n"
            f"  Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"
        )
    else:
        try:
            command = ["python", target_file]
            if args:
                command.extend(args)
            completed_code = subprocess.run(command, capture_output=True, text=True, timeout=30)
            completed_code_return = ""

            if completed_code.returncode != 0:
                completed_code_return = completed_code_return + f"Process exited with code {completed_code.returncode}"

            if not completed_code.stdout and not completed_code.stderr:
                completed_code_return = completed_code_return + f"No output produced"
            elif completed_code.stdout and not completed_code.stderr:
                completed_code_return = (
                    completed_code_return +
                    f"STDOUT: {completed_code.stdout}\n"
                )
            elif completed_code.stderr and not completed_code.stdout:
                completed_code_return = (
                    completed_code_return +
                    f"STDERR: {completed_code.stderr}\n"
                )
            else:
                completed_code_return = (
                    completed_code_return +
                    f"STDOUT: {completed_code.stdout}\n" +
                    f"STDERR: {completed_code.stderr}\n"
                )
            return (
                f"\nResult for \"{file_path}\" Python code:\n"
                f"\n{completed_code_return}"
            )
        except Exception as e:
            return (
                f"\nResults for \"{file_path}\" file:\n"
                f"  Error: excuting Python file: {e}"
            )
