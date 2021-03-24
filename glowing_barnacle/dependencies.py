"""
This file contains all the function needed to setup the dependencies and setup them if needed
"""
from git import Repo
from .settings import (
    PROJECT_PATH,
    EXTERNAL_GIT_DEPENDENCIES
)
import os
import sys
import logging
import importlib
import subprocess

logger = logging.getLogger(__name__)


def add_dependencies_to_path():
    for key, values in EXTERNAL_GIT_DEPENDENCIES.items():
        if values["path"] not in sys.path:
            sys.path.append(values["path"])


def clone_dependencies():
    logging.info("Setup external git dependencies.")
    for key, values in EXTERNAL_GIT_DEPENDENCIES.items():
        logger.info("Checking %s", key)

        path = values.get("path", None)
        url = values.get("url", None)
        setup = values.get("setup", None)

        if path and os.path.exists(values["path"]):
            logger.info("Already exists, Skipped.")
            continue

        if url:
            logger.info("Cloning repository %s.", path)
            os.makedirs(values["path"], exist_ok=True)
            repo = Repo.clone_from(
                values["url"],
                values["path"],
                branch=values.get("branch", None)
            )

        if setup:
            mod_name, func_name = setup.rsplit(".", 1)
            mod = importlib.import_module(mod_name)
            func = getattr(mod, func_name)
            func(values)


def basicsr_setup(values):
    logging.info("Installing BasicSR.")
    path = values["path"]
    # subprocess.run(
    #     [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
    #     cwd=path,
    #     check=True
    # )
    # subprocess.run(
    #     [sys.executable, "setup.py", "develop", "--no_cuda_ext"],
    #     cwd = path,
    #     check = True
    # )
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-e", "."],
        cwd=path,
        check=True
        )
    subprocess.run(
        [sys.executable, "scripts/download_pretrained_models.py", "DFDNet"],
        cwd=path,
        check=True
    )
    subprocess.run(
        [sys.executable, "scripts/download_pretrained_models.py", "dlib"],
        cwd=path,
        check=True
    )


def django_setup(values):
    subprocess.run(
        [sys.executable, "manage.py", "migrate"],
        cwd=PROJECT_PATH,
        check=True
    )


def main():
    logging.basicConfig(level=logging.INFO)
    clone_dependencies()
    #add_dependencies_to_path()


if __name__ == "__main__":
    main()
