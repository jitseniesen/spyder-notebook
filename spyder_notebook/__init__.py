# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Spyder Project Contributors
#
# Licensed under the terms of the MIT License
# -----------------------------------------------------------------------------

"""Spyder Notebook plugin, also serving as Jupyter Server extension."""

# Local imports
from spyder_notebook._version import __version__

# Integration with Jupyter

def _jupyter_server_extension_paths():
    return [{"module": "spyder_notebook"}]


def _jupyter_server_extension_points():
    from .app import JupyterNotebookApp

    return [{"module": "spyder_notebook", "app": JupyterNotebookApp}]


def _jupyter_labextension_paths():
    return [{"src": "labextension", "dest": "@spyder-notebook/lab-extension"}]
