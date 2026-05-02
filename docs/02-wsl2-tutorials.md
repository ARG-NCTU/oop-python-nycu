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



This may install VS Code Server for Linux 64 and take a while to start VS Code.

## 4. VPN

Make sure you add your Windows and WSL to two VPN clients..
Ask VPN manager (ask Nick).

### Install WireGuard

First, update your system and install the WireGuard package:

```bash
sudo apt update
sudo apt install wireguard
```
### 2. Generate Private and Public Keys

Generate a pair of private and public keys for the client. These keys will be stored in the `/etc/wireguard/` directory.

```bash
wg genkey | sudo tee /etc/wireguard/privatekey | wg pubkey | sudo tee /etc/wireguard/publickey
```

To verify, you can check the contents of the keys:

```bash
cat /etc/wireguard/privatekey
cat /etc/wireguard/publickey
```

Try the same procedure as in Ubuntu.
Proivde to VPN manager.
* Your Ubuntu public key (note this should be different from Windows)

VPN manager will give a 10.66.66.XX IP. to finish the setup.

### Configure WireGuard Client Interface

Create the WireGuard configuration file for the client. This file will define how the client connects to the WireGuard server.

```bash
sudo vim /etc/wireguard/wg1.conf
```

Example `wg1.conf` file (client-side):

```ini
[Interface]
PrivateKey = CLIENT_PRIVATE_KEY
ListenPort = 51820
Address = 10.66.66.XXX/24

[Peer]
PublicKey = JVchoWoC1CR9CM3MdNU32Zsr0cTYWTTyWHT3UhgcxSQ=
Endpoint =140.113.148.110:51820
AllowedIPs = 10.66.66.0/24
PersistentKeepalive = 25
```

Ensure the keys and endpoint information are correct, based on the server’s configuration.

### Set File Permissions

For security, set proper file permissions to restrict access to the keys and configuration files.

```bash
sudo chmod 600 /etc/wireguard/privatekey
sudo chmod 600 /etc/wireguard/wg1.conf
```

This ensures that the private key and configuration file are only readable by the root user.

### Start the WireGuard Interface

To bring up the WireGuard interface on the client, use the `wg-quick` command. It doesn't work in ARM architecture:

```bash
sudo wg-quick up wg1
```

To shut down the interface:

```bash
sudo wg-quick down wg1
```

To start at system boot:

```bash
sudo systemctl enable wg-quick@wg1
```

### Verify the Connection

To verify if the client is connected successfully, you can ping the server’s VPN IP address (e.g., `10.66.66.1`):

```bash
ping 10.66.66.1
```

If the ping is successful, the VPN connection is working correctly.

### Wireguard on Windows

Install Wireguard for Windows.

Try the same procedure as in Ubuntu.
Proivde to VPN manager.
* Your Windows public key (note this should be different from Ubuntu)

VPN manager will give a 10.66.66.XX IP. to finish the setup.


## 5. IDE (VS Code) and GitHub Copilot

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

### Try Remote-SSH to a IPC

Ask a partner for a testing remote machine (with 10.66.66.xxx) and username/password.

You need to setup ssh config file. In WSL add the following to ~/.ssh/config
```bash
Host argarm01
    HostName 10.66.66.xxx
    User arg
    IdentityFile ~/.ssh/id_ed25519
```

Copy your public key to argarm01
```bash
ssh-copy-id arg@10.66.66.xxx
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
- Ctrl + Shift + p or click bottom left icon
- Remote-SSH: Connect to Host. 
- You should be able to find argarm01
- Pick Ubuntu, and the VS Code will try to install its server on argarm01

### Enable GitHub Copilot

Login to your GitHub account.
Students can use xxx.edu.tw to apply for free GitHub copilot.
If you do  not have Copilot subscribed, ask Nick.

### VSCode Copilot Commit Configuration

This repository provides custom configuration for GitHub Copilot's commit message generation in VSCode.


For WSL 2 users with Github Copilot extension installed:

1. Navigate to your .vscode-server user settings in WSL2 terminal:
```bash
cd ~/.vscode-server/data/Machine
```

2. Add or modify the `settings.json` file with one of the configurations below.

This configuration enhances Git commit message generation by providing structured templates and guidelines through GitHub Copilot in VSCode.

### [template](https://hackmd.io/@Eudicotz/Syt1jooIJg)
```json
{
    "github.copilot.chat.commitMessageGeneration.instructions": [
        {
            "text": "Write a concise commit message from 'git diff --staged' output in the format `[GITEMOJI] [TYPE](file/topic): [description in {locale}]`. Use GitMoji emojis (e.g., ✨ → feat), present tense, active voice, max 240 characters per line, no code blocks."
        },
        {
            "text": "Present tense, active voice, max 240 characters per line, no code blocks."
        },
        {
            "text": "Provide a detailed body explaining the changes (wrap lines less then 72 characters)."
        }
    ]
}
```

## 6. Try MOOS Tutorial

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
pAntler alpha.moos
```

You should be able to see the pMarineViewer.
Click "Deploy" to start the msssion.

Some hotkeys to remember:
* 'c': centered at alpha
* 'i' or 'o': Zoom in or out
* 'UP', 'DOWN', 'LEFT', 'RIGHT': move around the map
* 'b': Toggle Tiff background
* 'h': Toggle hash lines (default: 50 meters)
* 'f': Toggle full screen
* Ctrl + 'a': Toggle InfoCasting


## 7. Windows Network Settings (ssh, ports, etc)

We will need the Windows to be accessed via VPN network as well.

### Access Windows via SSH

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

## 9. Install Foxglove and WinTAK (Windows)

You should be able to download WinTAK and Foxglove and install them on Windows.

Foxglove
https://foxglove.dev/download

WinTAK
https://argnas.dsmynas.com:5001/sharing/pWCaIyz0K

Version 5.4.0.149

## 10. ROS2 Topics (MVSim on Ubuntu) to Foxglove

Fork and clone https://github.com/MRPT/mvsim




