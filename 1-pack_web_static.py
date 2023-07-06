#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")

        # Create the archive with the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))

        # Return the archive path if the archive was created successfully
        return archive_path
    except:
        # Return None if there was an error creating the archive
        return None
