# WSL2 Ubuntu 24.04 Installation Guide and New Member Tutorials

This guide provides step-by-step instructions to install and set up Ubuntu 24.04 under Windows Subsystem for Linux 2 (WSL2).

---

## Prerequisites

- Windows 10 version 2004 or higher (Build 19041+), or Windows 11
- Administrator privileges
- Internet connection
- Try to update your NVidia Driver to the latest in Windows. Noted that WSL follows the CUDA version on Windows. Forcompatibility, we wil use Cuda 12.8 or above. This is relatively easier to upgrade in Windows ;P

---

## 1. Enable WSL and Virtual Machine Platform

Open **PowerShell as Administrator** and run:

```bash
wsl --list --online
wsl --install -d Ubuntu-24.04
```

Restart your computer if prompted.

---

## 2. Set WSL2 as Default

In PowerShell:

```bash
wsl --set-default-version 2
```

---

- Create a new UNIX username and password when prompted.

---

## 3. Initial Ubuntu and Docker

- Launch Ubuntu 24.04 from the Start Menu.

- Ubuntu 24.04

```bash
lsb_release -a
```

### Install Docker Desktop

Enter WSL cli,
```bash
sudo apt install docker.io
```
> [!CAUTION] Do not use docker desktop on windows! 有回報說WSL共用Windows docker desktop 會有一些問題更麻煩，建議就改裝在Ubuntu

If you encounter permission issue. Make sure you add the user to docker group in WSL

```bash
sudo usermod -aG docker $USER
```

Try to check Docker Compose Settings

- Docker Compose Version: v2.38+
- Make sure buildx is enabled. 

```bash
docker compose version
docker buildx version
```

If you can run docker-compose but not docker compose (v2), or you can not locate docker-compose-plugin. Try this:
[This Stack Overflow answer](https://stackoverflow.com/questions/76031884/sudo-apt-get-install-docker-compose-plugin-fails-on-jammy){:target="_blank"}

---

## 4. IDE (VS Code) and GitHub Copilot

### Install VS Code on Windows

- Download and install [Visual Studio Code](https://code.visualstudio.com/) from the official website.
- Launch VS Code after installation.

### Install Remote - WSL Extension

- In VS Code, go to the Extensions view.
- Search for **Remote Development** and install it.
- This allows you to open and develop directly in your WSL2 Ubuntu environment from VS Code.

You can clone a repo in Ubuntu and

```bash
code .
```

This may install VS Code Server for Linux 64 and take a while to start VS Code.

### Try Remote-SSH to a IPC

You need to setup ssh config file. In WSL add the following to ~/.ssh/config
```bash
Host argarm01
    HostName 10.66.66.128
    User arg
    IdentityFile ~/.ssh/id_ed25519
```

Copy your public key to argarm01
```bash
ssh-copy-id arg@10.66.66.128
```

Make sure you can
```bash
ssh argarm01
```

Now copy your ssh key (id_ed25519, id_ed25519.pub) and the config to your Windows user
```bash
cp ~/.ssh/id_ed25519* /mnt/c/User/XXXX/.ssh
cp ~/.ssh/config /mnt/c/User/XXXX/.ssh
```
This is perhaps not the best way, but make sure you own both WSL and Windows users.

Now in Windows VS Code
- Ctrl + Shift + p
- Remote-SSH: Connect to Host. 
- You should be able to find argarm01
- Pick Ubuntu, and the VS Code will try to install its server on argarm01

### Enable GitHub Copilot

Login to your GitHub account.
If you do  not have Copilot subscribed, ask Nick.


## 5. Try MOOS Tutorial

Install Essentials
```bash
sudo apt update
sudo apt install -y build-essential libelf-dev tmux vim sudo g++ subversion xterm cmake libfltk1.3-dev freeglut3-dev libpng-dev libjpeg-dev libxft-dev libxinerama-dev libtiff5-dev
```

Build MOOS-IvP

```bash
git clone git@github.com:moos-ivp/moos-ivp.git
cd moos-ivp
./build-moos.sh
./build-ivp.sh
```

Add MOOS bin to ~/.bashrc

```bash
export PATH="$PATH:/home/$USER/moos-ivp/bin"
```

Verify the path

```bash
source ~/.bashrc
which MOOSDB
which pHelmIvP
```

Run alpha mission

```bash
cd ~/moos-ivp/ivp/missions/s1_alpha
pAntler --MOOSTimeWarp=10 alpha.moos
```

You should be able to see the pMarineViewer.
Click "Deploy" to start the msssion.

In official MOOS-IvP repo, the Windows WSL docs may be outdated.
https://github.com/moos-ivp/moos-ivp/blob/main/README-WINDOWS.txt

## 6. VPN

Make sure you add your Windows and WSL to two VPN clients. See the VPN setup folder.

## 7. Windows Network Settings (ssh, ports, etc)

Download OpenSSH-Win64.

https://github.com/PowerShell/Win32-OpenSSH/releases

Run PowerShell as Admin.
```bash
Get-Service sshd

# Start service
Start-Service sshd

# Enable auto start
Set-Service sshd -StartupType Automatic
```

Add Rule for OpenSSH
```bash
New-NetFirewallRule -Name sshd `
  -DisplayName "OpenSSH Server (Port 22)" `
  -Enabled True `
  -Direction Inbound `
  -Protocol TCP `
  -Action Allow `
  -LocalPort 22
```

Add a new Windows Admin user
```bash
net user jsuser JetSeaAI2024 /add
net localgroup administrators jsuser /add
net user
```

Now you should be able to
```bash
ssh jsuser@10.66.66.XXX
```


## 8. File System

Windows and WSL are two-way mounted.

Download something from Windows Browser.

You can access them in WSL:
```bash
cd /mnt/c/Users/WIN_USERNAME/Downloads/
```

---

## 9. Install WinTAK, Foxglove, or other JetSea AI Apps (Windows)

### Public Repo

You should be able to download WinTAK and Foxglove and install them on Windows.

### JetSea AI Apps

Install USV-Control-GUI.

Install Unity Apps.

## 10. ROS2 Topics (MVSim on Ubuntu) to Foxglove

See the detail in JetSea AI Quick Start 
https://github.com/JetSeaAI/mvsim

## 11. MOOS pShare

mvsim 和MOOS uSimMarine對接，可以參考alpha pShare 

https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=Lab.ClassMultivAutonomyPreLab&utm_source=chatgpt.com


