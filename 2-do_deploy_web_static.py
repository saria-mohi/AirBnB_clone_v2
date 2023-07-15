#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static
and move it to the servers
"""

from fabric.api import put, env, sudo
from os.path import exists

env.hosts = ['100.26.233.228', '34.229.67.124']
# env.hosts = ['54.160.90.38', '100.25.36.19']
env.user = 'ubuntu'


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
