# XebiaLabs Deploy Setup

## For learning purpose, you may create XebiaLabs XL-Deploy(XLD) tool as a docker container

    docker run -e "ADMIN_PASSWORD=admin" -e "ACCEPT_EULA=Y" -p 4516:4516 --name xld xebialabs/xl-deploy:9.7

## From your web browser, you may now access the XLD page

    http://localhost:4516

## You may download the sample Java web application war file from the below URL

    wget https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/sample.war 

## You may download Tomcat 9.0 as shown below

<strong>For example, in my case I would navigate to /home/jegan/Downloads folder</strong>

    cd /home/jegan/Downloads

    wget http://apachemirror.wuchna.com/tomcat/tomcat-9/v9.0.37/bin/apache-tomcat-9.0.37.tar.gz

<strong> Extract the tar ball</strong>

    tar xvf apache-tomcat-9.0.37.tar.gz

<strong>Navigate to tomcat configuration folder</strong>

    cd apache-tomcat-9.0.37/conf

You need to add the below in the tomcat-users.xml file

    <role rolename="manager-script"/>
    <role rolename="manager-gui"/>
    <user username="tomcat" password="tomcat" roles="manager-script,manager-gui"/>

Configure tomcat to use port 8085 as Jenkins would already use the port 8080 by edit server.xml file
and replace port 8080 with 8085 as shown below

    <Connector port="8085" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443" />

You may now start tomcat server

    cd /home/jegan/Downloads/apache-tomcat-9.0.37/bin

    ./startup.sh

You may now test if you can access the tomcat web page from your browser

    http://localhost:8085

Once the tomcat page gets loaded, click on the manage button and type 'tomcat' as the user and 'tomcat' as the
password without single quotes. If all goes well, you should be able to access the manage page.
