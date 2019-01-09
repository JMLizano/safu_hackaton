# -*- coding: utf-8 -*-
"""Create an application instance."""
import shutil

shutil.copy("safu/safu.db", "/tmp/safu.db")

from safu.app import create_app

app = create_app()