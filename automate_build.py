#!/usr/bin/env python
# build docker images

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
    "vim-go": "docker_vim-go",
    "python-conda": "docker_python-conda",
    "rust": "docker_rust_env",
}
DAY = datetime.strftime(datetime.today(), '%Y%m%d')


def main():
    for image, dirname in IMAGES.items():
        try:
            # PULL
            pllcmd = ["sudo", "docker", "pull", f"{BASE_IMAGE}"]
            run_command(pllcmd)

            # BUILD
            bldcmd = [
                "sudo", "docker", "build", "--no-cache", "-t",
                f"{USER}/{image}", f"../{dirname}"
            ]
            run_command(bldcmd)

            # TAG
            tagcmd = [
                "sudo", "docker", "tag", f"{USER}/{image}:latest",
                f"{USER}/{image}:{DAY}"
            ]
            run_command(tagcmd)
            print(f"Successfully tagged {USER}/{image}:{DAY}")

            # PUSH
            pushcmds = [
                ["sudo", "docker", "push", f"{USER}/{image}:latest"],
                ["sudo", "docker", "push", f"{USER}/{image}:{DAY}"],
            ]
            for pushcmd in pushcmds:
                run_command(pushcmd)
        except subprocess.CalledProcessError as err:
            sys.exit(err)


def run_command(cmd: list) -> subprocess.CompletedProcess:
    res = subprocess.run(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         check=True)
    sys.stdout.buffer.write(res.stdout)  # Write stdout
    res.check_returncode()  # Unless code 0 => raise CalledProcessError


if __name__ == "__main__":
    main()
