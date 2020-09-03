## You need to create ssh-keygen with default options as a root user

ssh-keygen

## Copy the public key of root user under ubuntu-ansible folder

cd devops-sep-2020/Day2/ubuntu-ansible

cp /root/.ssh/id_rsa.pub authorized_keys

## You may now build the custom ubuntu ansible node images as shown below

docker build -t tektutor/ansible-ubuntu .

