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
        """Create a tar gzipped archive of the directory web_static."""
        dt = datetime.utcnow()
        file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                            dt.month,
                                                            dt.day,
                                                            dt.hour,
                                                            dt.minute,
                                                            dt.second)
        if os.path.isdir("versions") is False:
            if local("mkdir -p versions").failed is True:
                return None
        if local("tar -cvzf {} web_static".format(file)).failed is True:
            return None
        return file
    except:
        # Return None if there was an error creating the archive
        return None
