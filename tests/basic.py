"""
"""

import pytest
import os, sys  # explicitly modify path to avoid having to constantly run setup.py to test code
import numpy as np
import logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import PyCUST
import PyCUST.settings

# Logging tests


def test_logging():
    """
    """
    assert PyCUST.settings.debug_mode is True
    log_message = "Py & CUSTrd!"
    PyCUST.logger.info(log_message)
    with open(PyCUST.settings.logging_file_name) as file:
        assert f"PyCUST_log INFO: {log_message}\n" in file.readlines()
