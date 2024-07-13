#!/usr/bin/python3
"""module"""
from fabric.api import env, put, run, task, local
import datetime
import os

# Define the hosts to deploy to
env.hosts = ['54.83.139.226', 'I35.153.16.228']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """ This function is responsible """
    try:
        local('mkdir -p versions')
        date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        result = local(f"tar -cvzf versions/web_static{date}.tgz web_static")
        return result
    except Exception as e:
        return None

@task
def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory
        put(archive_path, "/tmp/")

        # Get the archive file name and folder name
        archive_name = os.path.basename(archive_path)
        folder_name = archive_name.replace('.tgz', '')

        # Create the release folder
        run(f"mkdir -p /data/web_static/releases/{folder_name}")

        # Uncompress the archive
        run(f"tar -xzf /tmp/{archive_name} -C /data/web_static/releases/{folder_name}")

        # Delete the archive from the web server
        run(f"rm /tmp/{archive_name}")

        # Delete the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run(f"ln -s /data/web_static/releases/{folder_name} /data/web_static/current")

        return True
    except:
        return False
