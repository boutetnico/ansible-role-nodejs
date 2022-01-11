[![tests](https://github.com/boutetnico/ansible-role-nodejs/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-nodejs/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.nodejs-blue.svg)](https://galaxy.ansible.com/boutetnico/nodejs)

ansible-role-nodejs
===================

This role installs [NodeJS](https://nodejs.org/en/).

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                     | Required | Default                       | Choices   |                                     |
|------------------------------|----------|-------------------------------|-----------|-------------------------------------|
| nodejs_dependencies          | true     | `[apt-transport-https,gnupg]` | list      |                                     |
| nodejs_version               | true     | `16.x`                        | string    |                                     |
| nodejs_package_state         | true     | `present`                     | string    | Use `latest` to upgrade.            |
| nodejs_global_npm_packages   | true     | `[]`                          | list      | Global NPM packages to install.     |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-nodejs
          nodejs_global_npm_packages:
            - name: npm-check-updates
              version: 10.2.5
            - name: yarn

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
