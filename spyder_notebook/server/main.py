# Copyright (c) Jupyter Development Team, Spyder Project Contributors.
# Distributed under the terms of the Modified BSD License.

"""Entry point for server rendering notebooks for Spyder."""

import os
from notebook.app import JupyterNotebookApp, NotebookBaseHandler
from tornado import web
from traitlets import default

HERE = os.path.dirname(__file__)


class SpyderNotebookHandler(NotebookBaseHandler):
    """A notebook page handler for Spyder."""

    @web.authenticated
    def get(self, path=None):
        """Get the notebook page."""
        tpl = self.render_template(
            'spyder-notebook-template.html', page_config=self.get_page_config())
        return self.write(tpl)


class SpyderNotebookApp(JupyterNotebookApp):
    """The Spyder notebook server extension app."""

    name = 'spyder_notebook'

    @default('static_dir')
    def _default_static_dir(self):
        return os.path.join(HERE, 'static')

    @default('templates_dir')
    def _default_templates_dir(self):
        return HERE

    def initialize_handlers(self):
        """Initialize handlers."""
        self.handlers.append(('/spyder-notebooks(.*)', SpyderNotebookHandler))
        super().initialize_handlers()


if __name__ == '__main__':
    SpyderNotebookApp.launch_instance()
