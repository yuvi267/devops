## Copy the public key of root user under centos-sshd-passwordless folder

cd devops-sep-2020/Day2/centos-sshd-passwordless

## Assuming you have already generated ssh-keygen while building ubuntu-ansible image build

cp /root/.ssh/id_rsa.pub authorized_keys

## You may now build the custom centos ansible node images as shown below

docker build -t tektutor/ansible-centos .

