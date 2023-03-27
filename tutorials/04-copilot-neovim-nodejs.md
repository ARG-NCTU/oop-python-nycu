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
https://docs.github.com/en/copilot/getting-started-with-github-copilot/getting-started-with-github-copilot-in-neovim?platform=linux

```
git clone https://github.com/github/copilot.vim \
   ~/.config/nvim/pack/github/start/copilot.vim
```

Use neovim
```
nvim
```

You will be asked to add code to enable the device.


You will see this

<img width="559" alt="image" src="https://user-images.githubusercontent.com/16217256/227206765-a5b992bd-223a-4f12-b7f1-906b1846efd4.png">

## Get Started

```
nvim [your python file].py
```
In navigation mode
```
:Copilot enable
```

* Create docstring for a class 
```
class Point:
   """
   Auto-complete for the docstring will appear here; tab to confirm
   """
```

* Create code from comment
```
# Create a point at the origin
origin = Point() # this will appear automatically

# Create a point at 3, 4
point = Point()   # keep press tab and enter
point.x = 3.0     # keep press tab and enter
point.y = 4.0     # keep press tab and enter

```


