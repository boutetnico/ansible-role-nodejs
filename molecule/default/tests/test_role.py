import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("nodejs"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


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
