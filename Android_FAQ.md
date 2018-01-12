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