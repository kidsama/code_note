1.安装Git
sudo apt-get install git
git --version
git config --list --global
git config --global user.name liushaowei
git config --global user.email liushaowei@kylinos.cn
git config --list --global
git clone http://172.17.66.163/kamg/kcm/web/monitor-flask.git

2.安装docker
首先，更新软件包索引，并且安装必要的依赖软件，来添加一个新的 HTTPS 软件源：
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
sudo apt list |grep docker
sudo apt install docker.io
安装完没权限，需要把我们当前的用户添加到docker组中
第一步：sudo gpasswd -a username docker  #将普通用户username加入到docker组中，username这个字段也可以直接换成$USER。
第二步：newgrp docker  #更新docker组

3.安装mysql
参考 https://segmentfault.com/a/1190000039203507
sudo apt install mysql-server

sudo service mysql status # 查看服务状态
sudo service mysql start # 启动服务
sudo service mysql stop # 停止服务
sudo service mysql restart # 重启服务

方法一：默认账户登录
查看密码使用sudo cat /etc/mysql/debian.cnf这条查看
方法二：直接进入mysql
命令：sudo mysql
重置密码
重置 root 账户密码
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
刷新权限
FLUSH PRIVILEGES;

3.sudo dpkg -i code_1.80.1-1689183569_amd64.deb