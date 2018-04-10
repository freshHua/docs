<center> Nordic开发 </center>
========================================
###开发环境
Nordic一款蓝牙MCU,开发环境Ubunt 14.04
###编译工具GCC
使用ARM Cortex-M toolchain 下载gcc-arm-none-eabi-4_9-2015q3

地址https://launchpad.net/gcc-arm-embedded/4.9/4.9-2015-q3-update

~~~shell
$ bzip2 -d gcc-arm-none-eabi-4_9-2015q3-20150921-linux.tar.bz2
$ tar -xvf gcc-arm-none-eabi-4_9-2015q3-20150921-linux.tar
$ cp gcc-arm-none-eabi-4_9-2015q3 /usr/local
$ export PATH=/usr/local/gcc-arm-none-eabi-4_9-2015q3/bin:${PATH}
~~~

~~~shell
$ arm-none-eabi-gcc --version
＃运行出错error while loading shared libraries: libX11.so.6
$　sudo apt-get install libx11-6:i386
~~~
###烧录调试工具
####JLink
下载https://www.segger.com/downloads/jlink
解压到/opt/SEGGER目录
###开发
####日志
~~~cpp
#include "sdk_config.h"

~~~


