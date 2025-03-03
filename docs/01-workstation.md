# Install AnyDesk

1. You need to install [anydesk](https://anydesk.com/zhs) in your laptop first.

2. Let TA konw your AnyDesk ID, and we will setup a whitelist so that only your team member could access it.

## Remote Access 

1. Please input the IP address, assigned to your team, in the blank.

The IP addresses are listed below.

TODO: to be updated

| Workstation | IP                  | assign      | No. of members    |
| ----------- | ------------------- | ----------- | -----------       |
| WS1         | 140.113.148.99      | 第1組        | 3 |
| WS2         | 140.113.148.100     | 第2組        | 2 |
| WS3         | 140.113.148.101     | 第3組        | 3 |
| WS4         | 140.113.148.103     | 第4組        | 3 |
| WS5         | 140.113.148.104     | 第8組        | 2 |
| WS6         | 140.113.148.105     | 第5組        | 3 |
| WS7         | 140.113.148.106     | 第6組        | 3 |
| WS8         | 140.113.148.107     | 第7組        | 3 |


![](https://github.com/Sensing-Intelligent-System/locobot_competition/blob/main/tutorials/picture/ws2.png)

2. Input the password.

![](https://github.com/Sensing-Intelligent-System/locobot_competition/blob/main/tutorials/picture/ws3.png)

3. Here is your work station.

![](https://github.com/Sensing-Intelligent-System/locobot_competition/blob/main/tutorials/picture/ws4.png)

# Setup your user and password (TA will work on this with you)

1. Open the termianl, and input (by TA)
```
sudo adduser <your team's name>
```
You should then following the command line instruciton and setup your password. 

Note that you wiil NOT have sudo permission. If you wish to install additional packages, please contact TA.

2. Setup the permission for docker. (by TA)
```
sudo adduser <your username>  docker
```

3. Reboot Log in your account and check. (by You)

```
 docker ps
```

![](https://github.com/Sensing-Intelligent-System/locobot_competition/blob/main/tutorials/picture/ws5.png)

# Remenber to log out when your finish your work, so that other user (teammate) won't use your GitHub account. 
