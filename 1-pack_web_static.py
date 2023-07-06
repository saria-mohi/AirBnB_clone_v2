#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    '''function:
    generates a .tgz archive from the contents of the web_static folder
    '''

    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    artifact = f'versions/web_static_{now}.tgz'
    if not os.path.exists('versions'):
        local('mkdir -p versions')

    fab_stat = local(f'tar -czvf {artifact} web_static')
    if fab_stat.succeeded:
        local(f'chmod 664 {artifact}')
        size = os.path.getsize(artifact)
        print(f'web_static packed: {artifact} -> {size}Bytes')
        return artifact
    else:
        return None
