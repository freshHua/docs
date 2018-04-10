 <center>Android FAQ</center>
 ========================================
 ### Wi-Fi连接速度
~~~java
WifiInfo wInfo = wifiManager.getConnectionInfo();
wInfo.getLinkSpeed();
~~~
Wi-Fi内核driver 802.11n　获取linkspeed
### ifconfig网络节点
~~~ shell
wlan0     Link encap:UNSPEC  
          inet addr:10.4.19.61  Bcast:10.4.19.255  Mask:255.255.255.0 
          inet6 addr: fe80::da7e:4bdf:2a06:98e5/64 Scope: Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:384122 errors:0 dropped:242 overruns:0 frame:0 
          TX packets:268772 errors:4659 dropped:0 overruns:0 carrier:0 
          collisions:0 txqueuelen:1000 
          RX bytes:447314496 TX bytes:18283828
~~~
		  
TX packets dropped　内核主动丢掉
RX packets 

###扫描二维玛
在比较暗处无法扫描二维码，

### cgroup
cpu 参数rt_runtime_us　实时进程一次能占有CPU的最长时间，缺省是1秒
cpuset 
### minikin
~~~ shell
    #00 pc 000000000000a78c  /system/lib64/libminikin.so (_ZNK7android14FontCollection17calcCoverageScoreEjjPNS_10FontFamilyE+112)
    #01 pc 000000000000a638  /system/lib64/libminikin.so (_ZNK7android14FontCollection15calcFamilyScoreEjjijPNS_10FontFamilyE+44)
    #02 pc 000000000000aaf8  /system/lib64/libminikin.so (_ZNK7android14FontCollection16getFamilyForCharEjjji+416)
    #03 pc 000000000000b294  /system/lib64/libminikin.so (_ZNK7android14FontCollection7itemizeEPKtmNS_9FontStyleEPNSt3__16vectorINS0_3RunENS4_9allocatorIS6_EEEE+656)
    #04 pc 00000000000139fc  /system/lib64/libminikin.so (_ZN7android6Layout11doLayoutRunEPKtmmmbPNS_13LayoutContextE+140)
    #05 pc 000000000001392c  /system/lib64/libminikin.so
    #06 pc 0000000000013358  /system/lib64/libminikin.so (_ZN7android6Layout12doLayoutWordEPKtmmmbPNS_13LayoutContextEmPKNS_14FontCollectionEPS0_Pf+452)
    #07 pc 0000000000012e00  /system/lib64/libminikin.so (_ZN7android6Layout17doLayoutRunCachedEPKtmmmbPNS_13LayoutContextEmPKNS_14FontCollectionEPS0_Pf+456)
    #08 pc 0000000000013030  /system/lib64/libminikin.so (_ZN7android6Layout11measureTextEPKtmmmiRKNS_9FontStyleERKNS_12MinikinPaintEPKNS_14FontCollectionEPf+488)
    #09 pc 000000000002f7c0  /system/lib64/libhwui.so (_ZN7android12MinikinUtils11measureTextEPKNS_5PaintEiPNS_8TypefaceEPKtmmmPf+164)
    #10 pc 00000000001174ac  /system/lib64/libandroid_runtime.so
~~~
~~~shell
$:export PATH=${PATH}:prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9/bin
~~~
~~~shell
$:aarch64-linux-android-addr2line -e ${TARGET_OUTPUT}/symbols/system/lib64/libminikin.so -a 000000000000a638
~~~

#libicui18n
~~~shell
    #00 pc 000000000016ddc4  /system/lib64/libicui18n.so (_ZN6icu_5612RegexMatcher12MatchChunkAtEiaR10UErrorCode+872)
    #01 pc 0000000000170f20  /system/lib64/libicui18n.so (_ZN6icu_5612RegexMatcher7matchesER10UErrorCode+364)
    #02 pc 000000000001d850  /system/lib64/libjavacore.so
    #03 pc 000000000080c1ac  /system/framework/arm64/boot.oat (offset 0x54d000) (java.util.regex.Matcher.matchesImpl+184)
    #04 pc 000000000080d8ac  /system/framework/arm64/boot.oat (offset 0x54d000) (java.util.regex.Matcher.matches+88)
    #05 pc 0000000002793400  /system/framework/arm64/boot-framework.oat (offset 0x1812000) (com.android.internal.app.procstats.ProcessStats.updateFragmentation+396)
    #06 pc 000000000278a0dc  /system/framework/arm64/boot-framework.oat (offset 0x1812000) (com.android.internal.app.procstats.ProcessStats.resetCommon+280)
    #07 pc 000000000279277c  /system/framework/arm64/boot-framework.oat (offset 0x1812000) (com.android.internal.app.procstats.ProcessStats.reset+56)
    #08 pc 0000000002789040  /system/framework/arm64/boot-framework.oat (offset 0x1812000) (com.android.internal.app.procstats.ProcessStats.<init>+588)
    #09 pc 0000000002788570  /system/framework/arm64/boot-framework.oat (offset 0x1812000) (com.android.internal.app.procstats.ProcessStats$1.createFromParcel+76)
    #10 pc 00000000027885f4  /system/framework/arm64/boot-framework.oat (offset 0x1812000) (com.android.internal.app.procstats.ProcessStats$1.createFromParcel+48)
    #11 pc 000000000147917c  /data/dalvik-cache/arm64/system@framework@services.jar@classes.dex (offset 0x1019000)
~~~
frameworks/base/core/java/com/android/internal/app/procstats/ProcessStats.java
ProcessStats -＞ reset -> resetCommon -> updateFragmentation
读取文件/proc/pagetypeinfo,每一行正则表达式进行匹配
~~~java
private static final Pattern sPageTypeRegex = Pattern.compile(
            "^Node\\s+(\\d+),.*. type\\s+(\\w+)\\s+([\\s\\d]+?)\\s*$");
~~~
进入java 通用库
~~~java
import java.util.regex.Pattern;
import java.util.regex.Matcher;
~~~
libcore/ojluni/src/main/java/java/util/regex/Matcher.java
matches方法调用jni
libcore/luni/src/main/native/java_util_regex_Matcher.cpp
matchesImpl
matchesImpl调用libicui18n.so
使用工具aarch64-linux-android-addr2line分析
~~~shell
$:export PATH=${PATH}:prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9/bin
$:aarch64-linux-android-addr2line -e ${TARGET_OUTPUT}/symbols/system/lib64/libicui18n.so -a 0000000000170f20
$:/proc/self/cwd/external/icu/icu4c/source/i18n/rematch.cpp:1541
$:aarch64-linux-android-addr2line -e ${TARGET_OUTPUT}/symbols/system/lib64/libicui18n.so -a 000000000016ddc4
$:/proc/self/cwd/external/icu/icu4c/source/i18n/rematch.cpp:4373
~~~
最后定位代码，heap buffer overflow，产生SIGSEGV信号，system_server异常，android系统重启
~~~cpp
op      = (int32_t)pat[fp->fPatIdx];
~~~


###CPU，内存监控
CPU占用情况
~~~
adb shell dumpsys cpuinfo
~~~
内存占用情况
~~~
adb shell dumpsys meminfo
~~~
内核节点
~~~
/proc/cpuinfo
/sys/devices/system/cpu/
/proc/stat
/proc/$pid/smaps
~~~