# Data project template

### Requirements to use this template:

- Python 3.5+
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip, pipx or similar.

```bash
$ pip install cookiecutter
```

or

```bash
$ pipx install cookiecutter
```

### To start a new project:

1. Run

```
cookiecutter https://github.com/AleSR13/databricks-data-project-template.git
```

2. Create a GitLab Repo

Go to your GitLab account and create a new repository. Name it after your `{{cookiecutter.project_name}}`.

3.  Activate your GitLab repo

On your computer, enter your newly created project folder, where project folder is the project_name you entered when you ran cookiecutter, then activate your repository:

```
git init .
git add .
git commit -m "Project template"
git remote add origin your-gitlab-repo
git push -u origin master
```
