sudo add-apt-repository ppa:neovim-ppa/stable  -y
sudo apt update -y
sudo apt install neovim  -y
sudo apt install ctags -y
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
source ~/.bashrc
nvm list-remote
nvm install v18.19.1
git clone https://github.com/github/copilot.vim \
   ~/.config/nvim/pack/github/start/copilot.vim
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs     https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
sudo add-apt-repository ppa:neovim-ppa/unstable  -y
sudo apt-get update  -y
sudo apt-get install neovim  -y
git config --global core.editor nvim
cp ./install_init.vim ~/.config/nvim/init.vim
nvim --headless +PlugInstall +qall
