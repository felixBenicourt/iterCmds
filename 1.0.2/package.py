name = "iterCmds"
version = "1.0.2"
author = "felix benicourt"

description = ""

build_command = False
requires = ['iter-1.1.0', 'python-3.10']

def commands():
    env.PYTHONPATH.append(this.root)
    env.PYTHONPATH.append("{root}\iterCmds")
    env.PATH.append(this.root)
    env.PATH.append("{root}\iterCmds")
    alias("sceneRunner", "python {root}/iterCmds/scene_runner.py")



