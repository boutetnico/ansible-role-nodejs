[![tests](https://github.com/boutetnico/ansible-role-nodejs/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-nodejs/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.nodejs-blue.svg)](https://galaxy.ansible.com/boutetnico/nodejs)

ansible-role-nodejs
===================

This role installs [NodeJS](https://nodejs.org/en/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                     | Required | Default                       | Choices   |                                     |
|------------------------------|----------|-------------------------------|-----------|-------------------------------------|
| nodejs_dependencies          | true     | `[apt-transport-https,gnupg]` | list      |                                     |
| nodejs_version               | true     | `22.x`                        | string    |                                     |
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
