#!/usr/bin/env python3
"""Auto build my docker images"""

import sys
from datetime import datetime
import subprocess

BASE_IMAGE = "archlinux/archlinux:base-devel"
USER = "u1and0"
IMAGES = {
    # [IMAGE NAME]:DIRECTORY NAME
    "yay": "docker_archlinux_yay",
    "archlinux": "docker_archlinux_env",
    "neovim": "docker_neovim_env",
    "zplug": "docker_zplug",
    "docker": "docker_docker",
    "deno": "docker_deno",
    "vim-go": "docker_vim-go",
    "python-conda": "docker_python-conda",
    # "rust": "docker_rust_env",
}
DAY = datetime.strftime(datetime.today(), '%Y%m%d')


def main():
    """Build docker images"""
    for image, dirname in IMAGES.items():
        cmds = [
            # PULL
            f"sudo docker pull {BASE_IMAGE}",
            # BUILD
            f"sudo docker build --no-cache -t {USER}/{image} ../{dirname}",
            # TAG
            f"sudo docker tag {USER}/{image}:latest {USER}/{image}:{DAY}",
            # PUSH
            f"sudo docker push {USER}/{image}:latest",
            f"sudo docker push {USER}/{image}:{DAY}",
        ]
        for i, cmd in enumerate(cmds):
            try:
                run_command(cmd.split())
                if i == 2:
                    print(f"Successfully tagged {USER}/{image}:{DAY}")
            except subprocess.CalledProcessError as err:
                sys.exit(err)


def run_command(cmd: list) -> subprocess.CompletedProcess:
    """Run docker command"""
    res = subprocess.run(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         check=True)
    sys.stdout.buffer.write(res.stdout)  # Write stdout
    res.check_returncode()  # Unless code 0 => raise CalledProcessError


if __name__ == "__main__":
    main()
