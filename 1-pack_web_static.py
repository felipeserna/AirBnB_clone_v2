#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo, using
the function do_pack."""

from datetime import datetime
from fabric.api import *


def do_pack():
    """Creates a .tgz archive from web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive))
        return (archive)
    except:
        return (None)
