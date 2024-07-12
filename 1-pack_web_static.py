#!/usr/bin/python3
"""a fabric script that compressed"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """compress a webstatic folder into a .tgz"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    result = local(f"tar -cvzf versions/web_static{date}.tgz web_static")
    if result.return_code == 0:
        return "versions/web_static{}.tgz".format(date=date)
    else:
        return None
