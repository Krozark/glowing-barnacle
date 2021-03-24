"""
This file contains some helpers to process images
"""

import logging
import os
import shutil
import subprocess
import sys
import tempfile

from .settings import (
    EXTERNAL_GIT_DEPENDENCIES
)


def improve_image_filepath(filepath):
    logging.info("Improve file %s", filepath)
    img_name = os.path.basename(filepath)
    basicsr_path = EXTERNAL_GIT_DEPENDENCIES["basicsr"]["path"]

    with tempfile.TemporaryDirectory() as tmpdirname:
        logging.debug("Creating tempory directory %s", tmpdirname)
        # copy file into temp directory to have only one (because of following script)
        shutil.copyfile(filepath, os.path.join(tmpdirname, img_name))
        subprocess.run(
            [
                sys.executable,
                os.path.join("inference", "inference_dfdnet.py"),
                "--official_adaption", "True",
                "--upscale_factor", "2",
                "--test_path", tmpdirname
            ],
            cwd=basicsr_path,
            check=True
        )
        output_filepath = os.path.join(
            basicsr_path,
            'results',
            'DFDNet',
            os.path.basename(tmpdirname),
            'final_results',
            img_name
        )
        logging.debug("Output file: %s", output_filepath)
    return output_filepath
