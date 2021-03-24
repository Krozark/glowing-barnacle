"""
Some vars needed are defined here
"""
import logging.config
import os

logger = logging.getLogger(__name__)

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.abspath(os.path.join(PROJECT_PATH, "data"))
SUB_REPO_PATH = os.path.join(DATA_PATH, "repo")

# Externale dependencies tha need some special attention.
EXTERNAL_GIT_DEPENDENCIES = {
    "basicsr": {  # this one cannot be install using pip, so we need to clone and install it manually
        "url": "https://github.com/xinntao/BasicSR.git",
        "path": os.path.join(SUB_REPO_PATH, "BasicSR"),
        "branch": "master",
        "setup": "glowing_barnacle.dependencies.basicsr_setup",
    },
    "django": {  # Django need a step to setup the database, so we use this mechanise as well (why not ?)
        "setup": "glowing_barnacle.dependencies.django_setup",
    }
}

LOGGING = {

}

