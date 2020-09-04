# Setting up a Windows Ansible Node
* You may use an existing Windows Server (On Premise) or
* You may create a T2 - Medium ec2 instance with Microsoft Windows Server 2019 Base AMI.

### WinRM ports must be opened up on Windows Server
* WinRM HTTPS Port - 5986
* WinRM HTTP  Port - 5985

In case of AWS ec2 instance, make sure the above port is opened up in Security Group.

### Windows Node Ansible Requirments

* PowerShell 3.0 or latest
* .Net Framework 4.5 or latest

### Finding PowerShell version
$PSVersionTable

### Finding .Net Framework Version
Open regedit and check if you are able to locate the below entries.  When .Net 4.x is installed on the system, you will find the entry.

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full

### Configuring WinRM on Windows machine 
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1" 

$file = "$env:temp\ConfigureRemotingForAnsible.ps1"

(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)

powershell.exe -ExecutionPolicy ByPass -File $file

### Configuring Windows node with Basic authentication 
Set-Item -Path WSMan:\localhost\Service\Auth\Basic -Value $true

### Verify if WinRM Listeners are running ( 2 listeners one for Http and other for Https expected )
winrm enumerate winrm/config/Listener

### On the Ansible Controller machine, make sure pywinrm is installed
pip install "pywinrm>=0.3.0"
