## Ansible Vault

Helps in protected sensitive data like 
* login credentials
* webserver credentials
* account details, etc

ansible-vault is a tool that helps you in protecting the sensitive data.

You can do the below with ansible-vault
* create - let's you create a vault protected file with data
* edit - let's you modify vault protected file
* view - let's you view the vault protected data
* decrypt - let's you decrypt vault protected file
* encrypt - let's you encrypt vault protected file
* rekey - modify the password of vault protected file

ansible-vault create credentials.yml

credentials.yml
username: devops
password: devops@123

## You may now check the file is encrypted
cat credentials.yml

## You may try viewing the vault protected file. Need to type password.
ansible-vault view credentials.yml

## You may try editing the vault protected file.
ansible-vault edit credentials.yml

## In case you have created the credentials.yml with a normal text editor and you wish to encrypt, you may try this
ansible-vault encrypt credentials.yml

## If you wish to edit with regualar text editor, you may decrypt the file as below
ansible-vault decrypt credentials.yml

## You can access the vault protected file from playbook
ansible-playbook vault-playbook.yml --ask-vault-pass

## You can store the vault password in some hidden location as shown below
echo "tektutor" > ./.secrets

In your ansible.cfg file, you can configure under [defaults] section

vault_password_file=./.secrets

ansible-playbook vault-playbook.yml
