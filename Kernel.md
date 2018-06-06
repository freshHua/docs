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

###页高速缓存
页高速缓存是内核实现的缓存技术，把数据缓存到物理内存，减少对存储的IO操作。理论上，如有足够大的内存，分配的页高速缓存足够大，读速度可以接近内存的速度．
缓冲区相关配置
/proc/sys/vm/dirty_ratio　缓冲区的大小，表示系统内存的百分比,Android默认值5%．
/proc/sys/vm/drop_caches　控制清理缓存
/proc/pagetypeinfo
/proc/buddyinfo
buddy算法解决物理内存的外碎片问题，其把所有空闲的内存，以2的幂次方的形式，分成11个块链表，分别对应为1、2、4、8、16、32、64、128、256、512、1024个页块。
/proc/meminfo
/proc/slabinfo
slab机制减少这种内部碎片，申请几十个字节
/proc/vmallocinfo


非重要文件的读写后，及时清除，避免产生缓存垃圾．
###优化方向
* 选择R/W速度块的存储器
* 内存足够大，cache足够大，文件缓存大，减少存储的写操作
* 避免小文件的读写和创建，少用文件同步操作
* 系统内置应用独立创建分区，使用内存文件系统
* 数据库，xml文件的进行算法优化

###内核空间内存申请
* kmalloc(),分配的内存大小有限制（128KB）
* kzalloc() kmalloc(__GFP_ZERO)
* vmalloc()

###Linux内核分析
CFS(完全公平调度算法） SCHED_NOMAL
实时调度算法 SCHED_FIFO和SCHED_RR
通过nice和counter值决定权值，nice越小，counter越大，被调度的概率越大，调度策略、优先级，获取CPU时间片大小
SCHED_FIFO一旦占用cpu则一直运行。一直运行直到有更高优先级任务到达或自己放弃
SHCED_RR策略的进程的时间片用完，系统将重新分配时间片，并置于就绪队列尾。放在队列尾保证了所有具有相同优先级的RR任务的调度公平。
###SATA
SATA硬盘的write-through ,write-back
###中断
~~~cpp
int request_threaded_irq(unsigned int irq, irq_handler_t handler, irq_handler_t thread_fn,
                         unsigned long irqflags, const char *devname, void *dev_id)
~~~
/proc/interrupts