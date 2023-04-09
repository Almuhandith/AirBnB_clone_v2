#!/usr/bin/python3
""" Function that deploys to a server """
from datetime import datetime
from fabric.api import *
import shlex
import os


env.hosts = ['18.234.129.117', '100.25.22.89']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        filename = name.replace('.', ' ')
        filename = shlex.split(filename)
        filename = filename[0]

        releases_path = "/data/web_static/releases/{}/".format(filename)
        tmp_path = "/tmp/{}".format(name)
        
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except:
        return False
