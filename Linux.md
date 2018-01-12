<center> 笔记 </center>
========================================

###桌面快捷方式
\${HOME}local/share/applications为快捷方式配置目录,进入${HOME}local/share/applications目录，创建相关应用desktop文件，如eclipse.desktop．
~~~shell
[Desktop Entry]
Name=Eclipse
Type=Application
Exec=/home/redbird/eclipse/jee-neon2/eclipse/eclipse
Terminal=false
Icon=/home/redbird/eclipse/jee-neon2/eclipse/icon.xpm
Comment=Integrated Development Environment
NoDisplay=false
Categories=Development;IDE;
Name[en]=Eclipse
~~~~

###Eclipse导入maven的项目
Eclipse 菜单FILE -> Import -> Maven -> Existing Maven Projects
###Ping出现DUP!
ping应答出现了重复的包duplicate
###Ubuntu WiFi热点
修改配置文件
~~~
/etc/NetworkManager/system-connections/
mode=ap(mode改为ap)
~~~
###正则表达式
![Python正则表达式](./images/pattern.png)
###EXT4加密属性
强制加密forceencrypt=footer，无法修改或删除文件
encryptable=footer

