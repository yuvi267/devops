# Programming Language
	What and How

	What?
		- I wanted to install latest version of Weblogic
		  on some 50000 servers
		- Among the 50000 servers
			- Some are Windows servers
			- Some are Linux - CentOS, RHEL, Fedora
			- Some are Unix
			- On some of these machines already Weblogic
			  is installed
			  	- Some of them have latest version
			  	- Some of these machines have older version
			  	  of Weblogic
			  	- Some don't have weblogic at all

	How?
		- Logic that needs to followed to achieve the How

	1. Imperative Languauge
		- eg: C++, Java, Python, Shell scripting, Batch 
		- Powerful language

		- You need to write to describe What and How

	2. Declarative Language
		- In a declarative language, you just need to convey What you
		  wanted to do on the servers
		- The How part is taken care by the declarative language



Configuration Management Tools
	- They use declarative language
	- Domain Specific Language (DSL)

	- System Administrators
		- Infra Engineers
		- DBA
		- Support Engineers
		- DevOps Engineers
		- Deployment Team
		- Operations Team

	- Developers
		- Frontend,Middle-ware, Backend
		- Full stack developers
			- Microservices
		- Test Driven Development
			- Test Framework
				- Junit, TestNg, Mockito, PowerMock(Bad)
				- Cucumber, Jasmine, Karma
		- System Administration skills

	- QA
		- Black-box Tester
		- White-box Tester
		- Selenium, Cucumber
			- By writing Java/C++/C#/Python they need to automate test cases
		- System Administrative skills



	- Puppet - DSL (Ruby) - Client/Server Architecture
	- Chef - DSL (Ruby)	- Client/Server Architecture
	- Ansible - DSL (YAML) - Agentless
		1. Ansible Core
			- Open source product
			- Developed in Python
			- Michael Deehan
				- He was former employee of RedHat
				- He founded a company called Ansible Inc
			- RedHat acquired Ansible Inc
			- RedHat was acquired by IBM
			- Command Line Tool
			- DSL
				YAML (Yet Another Markup Language)
					- Superset of JSON (JavaScript Object Notation)
					- human friendly format
					- any one can learn in 10-15 minutes
			
			- Inventory File
				- is a plain text file
					- Windows INI file
				- details on how to connect to remote 
				  ansible nodes
				- login credentials
				- on which port you need to connect
				- connection  method
					- winrm
					- ssh
				- user/password
				- Public/Private key for login authentication
				- Two types

					- Static Inventory
						- plain text file
						- it needs to be managed manually
							- Whenever new server is added as ansible node
							  You need manually add its connectivity details
							  to the inventory file.
							- Whenever ansible nodes goes offline
							  You need manually remove its connectivity details from the inventory file

					- Dynamic Inventory
						- Python script
						- Whenever you run the dynamic inventory python script
								- It finds the ansible nodes that are online
						Docker/AWS/AZure/Google Cloud/Digital Ocean
							- They provide their own dynamic inventory

			- Playbook
				- YAML file
				- can be written with plain text editors
				- uses Ansible Modules to automate certain activities
				  on the Ansible Nodes

			- Adhoc commands
				- unstructed commands like
					- you wanted to find ip, hostname of a ansible node
					
			- Ansible Modules
				- Python scripts
				- There are modules to
					- install, configure, update, upgrade
					  software tools on Unix/Linux/Windows
					- Manage Services
						- Windows Service
						- Linux Service
						- Start/Stop/Restart/Enable/Disable
					- Reboot machine
					- Copy files
					- Manage Fils/Directories
					- Templating Language
						- Python
							- Jinja 2 Templating Language
							- You can use variables and those variables
							  can be substitued at run-time with actual values

			- Ansible Controller Machine (ACM)
				- the machine where Ansible is installed
				  is called ACM
				- it could be laptop/official Desktop
				- Unix/Linux Ansible Nodes
					- SSH connection
					- Python scripts to automate (Built-in)
				- Windows Ansible Nodes
					- WinRM connection
					- Powershell scripts ( Built-in )

			- Ansible Nodes
				- are the servers that needs to be managed by Ansible
				- Pre-requisities
					- Tools that needs to installed
						- SSH Server (Open Source - Pretty much all Unix/Linux comes with SSH Server out of the box)
						- Python is required ( Unix/Linux machines comes out of the box with Python)
						- On Windows servers
							- WinRM (Remote Connection)
							- PowerShell 3.0 +

		2. Ansible Tower (RedHat-IBM)
			- Backed IBM
			- Very good Product Support
			- Based on Ansible Core (open source product)
			- Ansible Core with Web Interface
			- REST API
			- Role Based Access Control
			- Metrics presented in a Graphical fashion
			- Playbook execution logs/history 
		3. AWX
			- Open source variant of Ansible Tower

	- Salt Stack


Ansible Playbook Structure
	- Ansible Playbook is a YAML file
	- Each Playbook contains one ore more Play
	- Each Play targets atleast one ansible node
	- Each Play contains one or more Tasks
	- Each Task invoke at the most one Ansible Module(Python script)

