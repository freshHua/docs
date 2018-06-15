###进程
进程描述符，current为当前进程描述符宏中的thread_info．
~~~cpp
struct task_struct {
	struct thread_info *thread_info;
};
~~~
进程时间片：分配可运行程序的处理器时间段，默认时间片的10ms

* 进程状态
TASK_RUNNING  可执行状态 和 正在执行的状态
TASK_INTERRUPTIBLE 等待状态。等待状态可被信号解除
TASK_UNINTERRUPTIBLE 等待状态,状态不可中断。等待状态不可被信号解除

###内核线程
~~~cpp
struct task_struct*kthread_create(int(threadFn*)(void*data),void*data,const char*namefmt[],...);
kthread_run
创建内核线程，不主动运行，运行需要wake_up_process()唤醒.
~~~
~~~cpp
struct task_struct*kthread_run(int(threadFn*)(void*data),void*data,const char*namefmt[],...);
kthread_run
创建内核线程，运行，通过kthread_create,wake_up_process实现.
~~~

~~~cpp
int kthread_stop(struct task_struct *k);
结束kthread,过程
1.Sets kthread­>kthread_should_stop to true
2.唤醒线程
3.等待线程结束
~~~
~~~cpp
bool kthread_should_stop(void);
~~~

###内核抢占
当进程位于内核空间时，有一个更高优先级的任务出现时，如果当前内核允许抢占，则可以将当前任务挂起，执行优先级更高的进程。
$$
preempt\_count \gt  0  　　\text{　禁止内核抢占　}
$$
~~~cpp
preempt_disable() // preempt_count + 1
get_cpu() //preempt_disable()一样
preempt_enable() // preempt_count - 1
put_cpu() //preempt_enable()一样
preempt_enable_no_resched() // preempt_count -1，不立即抢占式调度 
put_cpu＿no_resched()　//preempt_enable_no_resched一样
~~~

###softIRQ
内核提供的一种延迟执行机制,tasklet，高分辨率timer.
###自旋锁
SMP多处理器中并发访问临界区，防止内核抢占造成的竞争。
用途高效的对互斥资源进行保护，同步临界区时间不能过长，处理过程中CPU不能处于休眠状态．

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

###内核空间内存申请
* kmalloc(),分配的内存大小有限制（128KB）
* kzalloc() kmalloc(__GFP_ZERO)
* vmalloc()

###内核调度
~~~cpp
schedule() 显示调用运行调度
sched_yield() 
yield()主动放弃CPU运行时间
~~~
CFS(完全公平调度算法） SCHED_NOMAL
实时调度算法 SCHED_FIFO和SCHED_RR
通过nice和counter值决定权值，nice越小，counter越大，被调度的概率越大，调度策略、优先级，获取CPU时间片大小
nice 范围　[-20,19]

SCHED_FIFO一旦占用cpu则一直运行。一直运行直到有更高优先级任务到达或自己放弃
SHCED_RR策略的进程的时间片用完，系统将重新分配时间片，并置于就绪队列尾。放在队列尾保证了所有具有相同优先级的RR任务的调度公平。
实时进程为静态优先级 [0,MAX_RT_PRIO]

###SATA
SATA硬盘的write-through ,write-back
###中断
~~~cpp
int request_threaded_irq(unsigned int irq, irq_handler_t handler, irq_handler_t thread_fn,
                         unsigned long irqflags, const char *devname, void *dev_id)
~~~
查看中断注册信息 `/proc/interrupts`
~~~shell
cat /proc/interrupts
~~~
###系统调用