import pathlib
import shutil


input_dir = pathlib.Path("{{cookiecutter.project_name}}")

for file in input_dir.glob("**/*"):
    relative_path = file.relative_to(input_dir)
    relative_path.parent.mkdir(parents=True, exist_ok=True)
    if file.is_file():
        print(f"Copying {file} to {relative_path}")
        shutil.copy(file, relative_path)
