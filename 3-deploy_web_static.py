#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from os.path import exists
from datetime import datetime
from fabric.api import env
from fabric.api import put
from fabric.api import sudo
from fabric.api import local, run

env.hosts = ["100.26.233.228", "34.229.67.124"]
env.user = "ubuntu"


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    # if os.path.isdir("versions") is False:
    local("mkdir -p versions")
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Deploys the web static to the server"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        folder_name = archive_name.split(".")[0]
        releaseVersion = "/data/web_static/releases/{}/".format(folder_name)
        symLink = "/data/web_static/current"

        print("Deploying new version from {}...".format(folder_name))
        put(archive_path, "/tmp/{}".format(archive_name))
        sudo("mkdir -p {}".format(releaseVersion))
        sudo("tar -xzf /tmp/{} -C {} --strip-components=1".format(
            archive_name, releaseVersion))
        sudo("rm /tmp/{}".format(archive_name))
        sudo("rm -f {}".format(symLink))
        sudo("ln -s {} {}".format(releaseVersion, symLink))
        print("New version deployed -> {}".format(releaseVersion))
        return True
    except Exception:
        print("Failed to deploy new version")
        return False


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
