###softIRQ
内核提供的一种延迟执行机制,tasklet，高分辨率timer.
###自旋锁
SMP多处理器中并发访问临界区，防止内核抢占造成的竞争。
###工作队列
工作推后执行的形式.工作队列可以把工作推后，交由一个内核线程去执行.运行在进程上下文中执行
~~~ cpp
struct workqueue_struct *create_workqueue(const char *name);
## 内核会在系统中的每个处理器上为该工作队列创建专用的线程
struct workqueue_struct * workqueue_singlethread_workqueue(const char *name);
## 创建一个专用的线程
~~~
###Tasklet

