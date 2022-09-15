# SSH key

You can follow below step to setting your ssh key for Github.

## 1. Generate key 
```
 $ mkdir ~/.ssh
 $ chmod 700 ~/.ssh
 $ ssh-keygen -t ed25519 -C "your_email@example.com"
```
## 2. Push key to Github
```
 $ cat ~/.ssh/key_name.pub 
 ssh-ed25519 ........ your_email@example.com
```
Log in your Github account and select setting\
![](https://i.imgur.com/NddBUYg.png)\
See left column and select SSH and GPG keys → New SSH key\
![](https://i.imgur.com/heWiCrV.png)\
Finally, copy your key in the bloew and set your name of key.\
![](https://i.imgur.com/3VUGFkC.png)

## 3. Make sure ssh key 
```
 $ ssh -T git@github.com
 Hi XXX! You’ve successfully authenticated, but GitHub does not provide shell access.
```

## 4. Transfer http to ssh

This step will modify current repo from http to ssh, if you have already use ssh key, then you can skip this step. 
```
 $ cd [to your repo]
 $ git remote -v
 origin  https://github.com/user_name/project.git (fetch)
 origin  https://github.com/user_name/project.git (push)
 $ git remote set-url origin git@github.com:user_name/project.git
 $ git remote -v
 origin  git@github.com:user_name/project.git (fetch)
 origin  git@github.com:user_name/project.git (push)
```

## 5. Others

This step will handle some warnings, these warnings will not affect the use of ssh key, this step you can decide for yourself whether or not to do it.
```
 $ git clone git@github.com:user_name/project.git
 Cloning into 'project'
 Warning: Permanently added the RSA host key for IP address  '192.30.252.128' to the list of known hosts.
 X11 forwarding request failed on channel 0
 (...)
```

Edit ssh_config
```
 $ sudo vim /etc/ssh/ssh_config
```

In the ssh_config
```
 Host github.com
    ForwardX11 no

 Host *
    ForwardX11 yes
```

Edit hosts
```
 $ sudo vim /etc/hosts
```

In the hosts, add below command.
**This ip is not fixed, you should change it depend on your warning.**
```
192.30.252.128　　github.com
```