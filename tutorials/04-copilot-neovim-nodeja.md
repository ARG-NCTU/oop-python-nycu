# Install Copilot for Neovim


## Install Neovim

```
sudo add-apt-repository ppa:neovim-ppa/stable
sudo apt update -y
sudo apt install neovim
```
See https://unixcop.com/how-to-install-neovim-on-ubuntu-20-04-22-04-lts/

## Install Node.js

We need 16
```
cd ~
curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh
sudo bash /tmp/nodesource_setup.sh
sudo apt install nodejs
```

See https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04

## Copilot

Now we are ready to install Copilot

```
git clone https://github.com/github/copilot.vim \
   ~/.config/nvim/pack/github/start/copilot.vim
```

You will be asked to add code to enable the device.

https://docs.github.com/en/copilot/getting-started-with-github-copilot/getting-started-with-github-copilot-in-neovim?platform=linux

