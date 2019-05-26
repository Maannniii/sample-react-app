# Sample React App IaC
Ansible project to setup, build and deploy docker containers on push to [Maannniii/sample-react-app](https://github.com/Maannniii/sample-react-app.git "Sample React App").

### Prerequisites:
1. [Install ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).
2. Add entry for server2 in /etc/hosts.
3. Add ssh-keys of server1 to server2.
4. Install and setup Jenkins.
5. Add web hook to repo.

### Setup Machines:
1. `cd` to `ansible` directory.
2. Update `hosts` file.
3. Update variables in `group_vars/all` .
4. Run as `ansible-playbook -i hosts setup.yml`.

### Testing
1. `cd` to `ansible` directory.
2. Run as `ansible-playbook -i hosts deploy.yml`.

## Note:
In order to keep it simple and cross compatible **IaaC** is followed. The same has been deployed and tested in both DigitalOcean and AWS on bare metal servers.
