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
    except Exception:
        return (None)


def do_deploy(archive_path):
    """
    Write a Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers, using the function do_deploy
    """

    if isfile(archive_path) is False:
        return False

    try:
        filename = archive_path.split("/")[1]
        filename1 = (archive_path.split("/")[1]).split(".")[0]
        input_path = "/data/web_static/releases/{}/".format(filename1)
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(input_path))
        run("sudo tar -zxvf /tmp/{} -C {}".format(filename, input_path))
        run("sudo rm -rf /tmp/{}".format(filename))
        run("sudo mv -n {}/web_static/* {}".format(input_path, input_path))
        run("sudo rm -rf {}/web_static".format(input_path))
        run("sudo rm /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(input_path))
        return True

    except Exception:
        return False


def deploy():
    """
    Write a Fabric script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers,
    using the function deploy
    """
    return_pack = do_pack()
    if return_pack is None:
        return False
    return do_deploy(return_pack)
