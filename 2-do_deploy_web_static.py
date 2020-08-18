#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy."""

from datetime import datetime
from fabric.api import *
from os.path import isfile


env.hosts = ['35.231.65.220', '34.227.7.13']


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


def do_deploy(archive_path):
    """Deploy web_static in servers"""
    if isfile(archive_path) is False:
        return False

    file_name_tgz = archive_path.split("/")[1]
    file_name = file_name_tgz.split(".")[0]

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}"
            .format(file_name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name_tgz, file_name))
        run("rm /tmp/{}".format(file_name_tgz))
        run("mv /data/web_static/releases/{}/web_static/* \
             /data/web_static/releases/{}/".format(file_name_tgz, file_name))
        run("rm -rf")
        run("rm -rf /data/web_static_current")
        run("ln -s /data/web_static/releases/{}/ \
             /data/web_static/current".format(file_name))

        return True

    except:
        return False
