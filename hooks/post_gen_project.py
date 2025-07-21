import logging
import pathlib
import shutil

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def main():

    project_root = pathlib.Path.cwd()
    project_name_folder = project_root / "{{cookiecutter.project_name}}"

    if project_name_folder.exists() and project_name_folder.is_dir():
        for item in project_name_folder.iterdir():
            target = project_root / item.name
            LOGGER.info("Moving %s to %s", item, target)
            if item.is_dir():
                shutil.move(str(item), str(target))
            else:
                shutil.move(str(item), str(target))

    # input_dir = pathlib.Path("{{cookiecutter.project_name}}")

    # for file in input_dir.glob("**/*"):
    #     if file.is_file():
    #         parent_folder = pathlib.Path(".").joinpath(file.parent)
    #         parent_folder.mkdir(parents=True, exist_ok=True)
    #         output_file = parent_folder.joinpath(file.name)
    #         LOGGER.info("Copying %s to %s", file, output_file)
    #         shutil.copy(file, output_file)
    return True


if __name__ == "__main__":
    main()
