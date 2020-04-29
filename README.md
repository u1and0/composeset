maintainer: u1and0 <e01.ando60@gmail.com>
version 3.7 for docker version 18.06+
see https://docs.docker.com/compose/compose-file/

# What for
docker in docker dev.env

* master: zsh & zplug env. Parents for all docker image.
* jupyter: python env. It can use ipython & jupyter
* vim-go: golang env.

# Usage

```
$ cd /path/to/composeset
$ docker-compose up
$ docker exec -it composeset_master_1 zsh -l

# Login master container then...
$ tmux

# Login go env
$ docker exec -it composeset_vim-go_1 zsh -l

# Login python env
$ docker exec -it composeset_jupyter_1 bash -c ". .bashrc && zsh"

# Login python env as ipython
$ docker exec -it composeset_jupyter_1 bash -c ". .bashrc && ipython"
```
