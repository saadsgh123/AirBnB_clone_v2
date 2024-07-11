#!/usr/bin/python3
# generates a .tgz archive from the contents of the web_static
# folder of your AirBnB Clone repo
from fabric import task
from datetime import datetime

@task
def do_pack(c):
    """Return a list of files"""
    datet = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"web_static_{datet}.tgz"
    
    c.local("mkdir -p versions")
    create = c.local(f"tar -czf versions/{filename} ./web_static")
    if create.failed:
        return None
    else:
        return f"versions/{filename}"
