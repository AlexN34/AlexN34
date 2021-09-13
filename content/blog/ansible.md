Title: Learning Ansible
Date: 2018-4-12 16:23
Tags: ansible, devops
Slug: learning-ansible
Category: ansible
Author: Alex Nguyen
Summary: New DevOps tool: Ansible

## Background
Moving into Digital Platforms (Cloud and DevOps kind of work) is going to require a new toolset - knowing Python, it seems like Ansible would be a good choice to pick up for infrastructure automation.

Toying around with local hosts looks promising so far - links to playbooks [here](https://github.com/alexnguyennn/learn-ansible). Next step is orchestrating real servers - fingers crossed I'll get to explore/use some the extensibility features for work!

### Tidbits
- Ansible runs with central controller node running commands on other nodes (which don't necessarily have Ansible installed)
- SSH is used so as long as that's ok you can orchestrate other servers
- Host node should run Linux, scripts can talk to Windows nodes (using specific modules e.g. `win_shell` instead of `shell`)
- The INI configuration file is called inventory (`-i` flag) - list host address of grouped servers
- In playbook, can set variables with `vars` and refer throughout playbook YML using `{{}}` syntax
- Can configure custom behaviour on repeat runs through `notify` (in conjunction with `changed_when`) and `handlers` syntax

## Commands
- Ansible is installed and run as a python package: `pip install ansible ansible-lint`
- `ansible -i <inventory> <host> -m <ansible-module> -a <module-arguments>` to run commands on host/group of hosts interactively on a shell e.g. `ansible -i webapp local -m command -a "uname -r" `

- Ansible `playbook.yml` is analogous to `docker-compose.yml`: YAML-fied version of the active ad-hoc command
- `ansible-playbook -i <inventory-file> <playbook.yml>` to a run a playbook 
- `ansible-doc` is `man` for modules
