# diqa-sequencing-template
A standardized template for genomic sequencing data workflows maintained by DIQA.

# Description and overview
This repository is meant to provide a basic template for setting up a project. 
It provides a basic repository structure as well as files to aid in establish github processes 

# Installation
Setting Up a New Repository from this Template

1. Click the "Use this template" button at the top of this repository
2. Name your repository (recommend: sequencing-[name-of-pathogen/group])
3. Clone your new repository to your computer:
```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

# Repository Usage Guide
This section provides guidance on how to use the key directories and files in 
this template repository.

## README
You are currently reading the README specifically written for this template repository. Upon creating a project you should comprise a detailed README more 
suited for your project that (at a minimum) has the following components:

- Project Title & Description
  - Clear, concise name of the project
  - Brief overview of what the project does and its purpose
  
- Installation Instructions
  - Prerequisites/dependencies
  - Step-by-step installation process

- Usage Examples
  - Basic examples showing how to use the project
  - Code snippets demonstrating key functionality
  - Command line examples if applicable

- Configuration
  - Description of configuration options
  - Environment variables
  - Configuration file formats

- Project Structure
  - Overview of important directories and files
  - Purpose of each major component

- Contributing Guidelines
  - How others can contribute to the project
  - Code standards and practices
  - Pull request process

- License Information (if applicable)
  - Clear statement of the project's license
  - Any usage restrictions

- Contact Information/Support
  - How to reach maintainers
  - Where to report issues
  - Community channels

The README does not need to strictly follow this format. However, you should 
aim to provide as much of the information outlined above as possible at a minimum.

## .github/ directory
This directory contains GitHub-specific configuration files that control how your repository behaves on GitHub.

How to use it:

- Workflows (`.github/workflows/`): These YAML files define automated processes (GitHub Actions) that run when specific events happen in your repository.
  - `validate-commits-prs.yml`: This workflow performs validation on code contributions (branch names/commits/pull requests) to ensure that best practice 
  is being followed (see `Release Cycle Process` section). 
  - `runs-tests.yml` This workflow runs all tests in the `tests/` dir. 
  - `prepare-release.yml` This workflow automates the creation of GitHub releases when a pull request from a release branch is merged into the main branch.
- Templates (`.github/templates/`): Contains reusable templates for creating
  consistent components across repositories.
  - Example: By creating an issue or pull request template the u
Customize these templates to match your specific pathogen project's needs.

Best practice: Don't delete this directory. The workflows help ensure code 
quality and save you time by automating repetitive tasks. Modify if needed.


## .gitignore File
This file tells Git which files or directories to ignore when you 
commit changes. This helps to ensure that the remote repostiory is kept clean 
but also to prevent sensitive information does not accidently get pushed.

The template's .gitignore is already set up to exclude common files.
- Large data files (in the data/ directory)
- Environment files (like .env)
- Cache and temporary files
- System files (like .DS_Store on Mac)

How to use it:

If you need to work with additional file types that shouldn't be tracked, add 
them to this file in the following manner:
```bash
# Ignore a specific file
example-file-name.json

# Ignore all files with a specific extension
*.log

# Ignore an entire directory
example-dir-name/

# Ignore files in any directory with a specific name
**/example-file-name.yaml

# Ignore everything in a directory except one file
example-file-dir/*
!example-file-dir/example-file-name

# Ignore all subdirectories wherever they appear
**/example-subdir-name/
```

Best practice: Never commit PII, large data files, passwords, or API keys to your repository. Add any files or directories containing files w/ sensitive 
information to .gitignore. PII should never be stored within a repository, 
regardless of whether or not the file or directory is part of the .gitignore.

## docs/ directory
This directory contains all documentation for your repository.

How to use it:

Create and store documentation in this directory. Ensure documentation is kept 
up to do date with the code in product. Good documentation helps new contributors understand your project and reduces the time you spend answering basic questions.

Examples:
- Pipeline/process Documentation (`docs/pipeline`): Explains how your data processing pipeline works.
- Data Dictionary (`docs/data_dictionary`): Defines all metadata fields used in your project.
  
If you plan to create a github pages and serve it from the `docs/` directory 
direcory would serve two purposes: 
- provide information for users of your template repository
- provide public-facing documentation site through GitHub Pages.

Note: all content in this directory will be considered part of your public documentation site.

Best practice: Try to keep documents as markdown(.md) or at least have a markdown version if possible.
- You can add Adding a `docs/internal/` subdirectory for documentation that's 
  meant for repo users but not necessarily meant to be published on the site.

## tests/ directory
This directory contains all the automated tests that verify your code functions correctly. A robust test suite is essential for ensuring your pipeline/process 
is producing the correct results. Additionally, a correctly structured `tests/` 
directory will be beneficial. Below are components to a test suite that can be 
considered "bare minimum".

### How to use it
- Unit Tests (`tests/unit/`): Tests for individual functions or classes in 
  isolation.
  - Mirror your src/ directory structure to make tests easy to find
    - Example: tests/unit/pipelines/validation/test_schema_validator.py tests src/pipelines/validation/schema_validator.py
  - Focus on testing one function or class per test file
- Integration Tests (`tests/integration/`): Tests that verify different components 
work together correctly.
  - Test complete processing workflows from input to output to verify that 
  components interact correctly with each other
    - Example: tests/integration/test_full_pipeline.py might test the entire metadata processing workflow
- Test Data (`tests/data/`): Subdirectory containing test datasets organized by purpose and size.
  - This folder should contain smaller subdirectories based on the type of test 
  the data is used for and the functionality being tested. As this will largely 
  depend on the individual project it has not been included in this template
- Conftest (tests/conftest.py): Shared pytest fixtures and configuration.

```bash
# Running all tests
pytest
```
```bash
# Running individual tests files
pytest tests/unit/example_file_test.py
```
```bash
# Running individual tests within a test file
pytest tests/unit/example_file_test.py::test_example
```

Note: Depending on the project end-to-end (e2e) tests may be beneficial in 
addition to integration tests.

### Naming conventions
- Test files must be named as `test_*.py` or `*_test.py`
- Individual test methods/functions should be named as `test_*`
- Test classes (without an `__init__` method) should be named `Test*` and test methods/functions within the class as `test_*` 

### Best practices
Run tests before committing changes to ensure you haven't broken anything. As part of the run-tests.yaml all tests should automatically run as 
part of a newly created pull request. However, it is still good practice to run 
tests prior to each commit. Add new tests when you add new features. Keep 
datasets appropriately sized for their purpose.

## Release Cycle Process

### Overview
This repository uses an automated release workflow that manages versioning and releases through GitHub Actions. The process follows a structured branching strategy and automated releases through pull requests.

### Branch Strategy
- `main`: Production-ready code
- `release/*`: Release preparation branches (e.g., release/0.1.0)
- `feature/*`: New feature development
- `fix/*`: Bug fixes
- `docs/*`: Documentation changes
- `refactor/*`: Code refactoring
- `chore/*`: Maintenance tasks

### Commit Guidelines

All commits must follow the conventional commits format:
- `feat:` - New features
- `fix:` - Bug fixes
- `chore:` - Maintenance tasks
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `perf:` - Performance improvements
- `test:` - Test updates
- `build:` - Build system changes
- `ci:` - CI configuration changes
- `revert:` - Revert previous changes

Example:
```bash
git commit -m "feat: add data validation"
git commit -m "fix: correct calculation bug"
git commit -m "chore: update dependencies"
```

### Step-by-Step Process

#### Start New Feature Development
```bash
# Create new feature branch from main
git checkout main
git pull
git checkout -b feature/your-feature-name
# Work on your feature
# Commit using conventional commits:
git add .
git commit -m "feat: add new functionality"
git push origin feature/your-feature-name
```

#### Create a release branch 
```bash
# Create release branch from main for the release cycle
git checkout main
git pull
git checkout -b release/0.1.0
git push origin release/0.1.0
```

#### Create Feature Pull Request
1. Go to GitHub repository
2. Click "Pull requests"
3. Click "New pull request"
4. Set branches:
    - base: release/0.1.0
    - compare: feature/your-feature-name
5. Add descriptive title following commit convention (e.g., "feat: implement user authentication")
6. Add description detailing the changes
7. Request reviews
8. Tests will run automatically

#### Merge Features to Release Branch
- Review and approve feature PRs
- Merge approved features into release branch
- Continue until release is ready

#### Create Release Pull Request
1. Once release branch contains all intended features:
2. Create PR from release branch to main
3. Title must follow commit convention (e.g., "release: v0.1.0")
4. Description should include:
    - Summary of changes
    - Notable features
    - Breaking changes (if any)
    - Updated dependencies (if any)
5.  Request reviews

#### Final Release Process
When release PR is approved and merged to main, the workflow automatically:
  - Creates a version tag (e.g., v0.1.0)
  - Generates GitHub Release with release notes
  - Closes the release cycle
    
#### Version Numbering
Follow semantic versioning (MAJOR.MINOR.PATCH):
  - MAJOR (1.0.0) - Breaking changes
  - MINOR (0.1.0) - New features (backwards compatible)
  - PATCH (0.0.1) - Bug fixes

#### Important Notes
- All changes must go through pull requests
- PR titles must follow conventional commit format
- Release PRs require approval before merging to main
- Tests must pass before merges are allowed
- Each release should have proper documentation of changes

# Package Dependency Management
This template is set up with infrastructure needed to use [UV](https://docs.astral.sh/uv/) for package and project management. You will need `UV` installed on your machine before using it.

## Setup
### Installation
You can use a standalone installer using the commands below, or download `UV` directly from PyPi with pip/pipx. Below are commonly used methods for installation. See the [official documentation](https://docs.astral.sh/uv/getting-started/installation/) for a full list of installation methods.
  - Windows:  
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```  
  - Linux/macOS (with curl):
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
  - Linux/macOS (with wget):
    ```bash
    wget -qO- https://astral.sh/uv/install.sh | sh
    ```
  - PyPi:
    ```
    pip install uv
    ```
After installing, you should try to run this command in your terminal to check that it is available.
```bash
uv
```
If you have trouble, you may need to add the installation directory to your PATH.

### Project Environment
After `UV` is installed and available for use from your terminal, the next step is to create a virtual environment. Navigate to your project folder as the current directory and run [this command](https://docs.astral.sh/uv/reference/cli/#uv-venv)
```bash
uv venv
```
This will create a `.venv` directory within your project directory, which includes files necessary to use and manage a virtual environment as well as a `.gitignore` to exclude the environment from git tracking.  

Finally, activate the newly created virtual environment by running either of these commands
- Linux/macOS:
  ```bash
  source .venv/Scripts/activate
  ```
- Windows:
  ```powershell
  .venv\Scripts\activate
  ```

### Syncing
The last step in intial set up is to sync your virtual environment with the existing `uv.lock`. Do this by running the following command
```bash
uv sync
```
A handful of packages should be installed: those used as a standard by DIQA like [polars](https://github.com/pola-rs/polars) and [wadoh_raccoon](https://github.com/NW-PaGe/wadoh_raccoon), as well as their dependencies.

## Management
See documentation on [managing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/) and [locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/) for full details.

### Adding/removing dependencies
- Packages used in a project, and their dependencies, should be added to `pyproject.toml` AND `uv.lock` to maintain a clean and reproducible environment. This is done by using the `add` command.
  ```bash
  uv add wadoh_raccoon
  ```
- You can also specify exact versions or bounds
  ```bash
  uv add "wadoh_racoon>=1.0.0"
  ```
- Sources can be specified for packages outside of public package registries (i.e. PyPi).
  ```bash
  uv add "wadoh_raccoon @ git+https://github.com/NW-PaGe/wadoh_raccoon"
  ```
- Existing requirements files can be imported using the `-r` option
  ```bash
  uv add -r requirements.txt
  ```
- Removing dependencies can be done simply by using `remove` and specifying the dependency name
  ```bash
  uv remove wadoh_raccoon
  ```

### Updating versions
Locking (and syncing) is generally automatically handled by UV. Locking is required, however, when updating packages from previously-recorded versions.  

- To upgrade a single package to the latest version, while retaining the locked versions of all other packages:
  ```bash
  uv lock --upgrade-package wadoh_raccoon
  ```
- To upgrade a single package to a specific version:
  ```
  uv lock --upgrade-package wadoh_raccoon==2.0.0
  ```

# Contact
This repository is maintained by the Data Integration and Quality Assurance (DIQA) - Sequencing Team
- doh.cds.genseqsurvdq@doh.wa.gov

In the subject line, please include "diqa-sequencing-template:" for any questions regarding this repository.
