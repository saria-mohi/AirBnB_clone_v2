#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env, put, run

env.hosts = ["100.26.233.288", "34.229.67.124"]
env.user = "ubuntu"

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    

    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        archive_path = "/data/web_static/releases/{}/".format(name)
        link = "/data/web_static/current"

        put(archive_path, "/tmp/{}".format(file))
        run("mkdir -p {}/".format(archive_path))
        run("tar -xzf /tmp/{} -C {}/".format(file, archive_path))
        run("rm /tmp/{}".format(file))
        run("rm -rf {}".format(link))
        run("ln -s {} {}".format( archive_path,link))
        return True
    except Exception:
        return False