import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("gnupg"),
    ],
)
def test_dependencies_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "name",
    [
        ("nodejs"),
    ],
)
def test_nodejs_package_is_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_node_command_works(host):
    cmd = host.run("node --version")
    assert cmd.rc == 0
    assert cmd.stdout.startswith("v")


def test_npm_command_works(host):
    cmd = host.run("npm --version")
    assert cmd.rc == 0


@pytest.mark.parametrize(
    "path,user,group",
    [
        ("/usr/bin/node", "root", "root"),
        ("/usr/bin/ncu", "root", "root"),
        ("/usr/bin/yarn", "root", "root"),
    ],
)
def test_binaries_are_installed(host, path, user, group):
    binary = host.file(path)
    assert binary.exists
    assert binary.is_file
    assert binary.user == user
    assert binary.group == group
