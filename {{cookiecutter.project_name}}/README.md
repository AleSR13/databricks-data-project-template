# Welcome to {{cookiecutter.project_name}}

{{cookiecutter.description}}

### The directory structure

```
├── README.md          <- The top-level README for developers using this project.
├── pyproject.toml     <- To track project dependencies (using poetry)
├── LICENSE            <- License to use this project (if any)
├── CONTRIBUTING.md    <- Rules for contributing to this repo (if any)
├── CHANGELOG.md       <- Log of changes to the repo
├── .gitignore         <- Enlists which files/folders to ignore in git commands
│
├───.github            <- GitHub configuration
│   ├───templates      <- GitHub templates (e.g. to report issues)
│   └───workflows      <- GitHub CI/CD workflows (if any)
├───config             <- Configuration files for the repo
├───docs               <- Holds repo documentation
├───notebooks          <- Databricks notebooks for exploration (not for jobs)
├───src                <- Code for the package. This is the only official code of the repo (unlike the notebooks)
│   ├───jobs           <- Databricks jobs
│   ├───schemas        <- Schemas of the tables to be created
│   └───utils          <- Utils of the repo containing reusable code across multiple jobs
├───terraform          <- Infrastructure as code using terraform
│   └───envs           <- Contains variables and specific configuration per environment (dev, test, prod)
└───tests              <- Code tests (using pytest)
```
