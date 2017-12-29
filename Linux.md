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


