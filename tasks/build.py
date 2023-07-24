from pyboot import CompletedProcess, SourceProject, subprocess_run


def main(context: SourceProject) -> CompletedProcess:
    return subprocess_run("docker build -f ./.devcontainer/dockerfile -t sinksky .")
