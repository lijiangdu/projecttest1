import threading
import time, sys
if sys.version_info.major == 2:
    import thread
else:
    import _thread as thread
#线程的启动
# def thread_entry(id):
#     cnt=0
#     while cnt<10:
#         print('Thread:(%d) Time:%s' %(id,time.ctime()))
#         time.sleep(1)
#         cnt+=1
# def start_threads():
#     print(6)
#     t1 = thread.start_new_thread(thread_entry, (1,))
#     t2 = thread.start_new_thread(thread_entry, (2,))
#     print(7)
#     time.sleep(15)
#     #因为元素还没有被加载出来，查找的代码就已经被执行了,所以在此处需要使用sleep等待
#     print(8)
# if __name__ == '__main__':
#     start_threads()
#线程的退出
# g_continue = True
# x1=id(g_continue)
# def thread_entry(id):
#     global g_continue
#     # x2 = id(g_continue)
#     while True:
#         if not g_continue:
#             print("Thread:(%d) exit" %id)
#             # print(x2)
#             thread.exit()
#         else:
#             print('Thread:(%d) Time:%s' %(id,time.ctime()))
#             # print(x2)
#             time.sleep(1)
# def start_threads():
#     global g_continue
#     x3 = id(g_continue)
#     print(x1,x3)
#     t1 = thread.start_new_thread(thread_entry, (1,))
#     t2 = thread.start_new_thread(thread_entry, (2,))
#     time.sleep(3)
#     g_continue = False
#     time.sleep(2)
# if __name__ == '__main__':
#     start_threads()
#deamon属性用法
# import sys, time
# import threading
# def thread_entry():
#     left_round = 10
#     print('Child Thread: Strat Running')
#     while left_round>0:
#         print('Child Thread: Runnning, left round = %d' % left_round)
#         time.sleep(0.5)
#         left_round = left_round -1
#     print('Child Thread Quit')
# def start_threads():
#     # thread1 = threading.Thread(target=thread_entry, daemon=True)
#     thread1 = threading.Thread(target=thread_entry, daemon=False)
#     # thread1 = threading.Thread(target=thread_entry(),daemon=True)
#     #target后面如果接着一个函数，那么将会直接运行该函数，不受到线程控制,只有当target后面接函数名，才会将该函数引入该线程中
#     #默认创建的进程不是daemon进程，当所有非daemon线程结束时，进程结束，当创建非daemon线程时，需要等该线程结束之后整个进程才会结束
#     thread1.start()
#     time.sleep(0.8)
#     print('Active Thread Number = %d' %threading.active_count())
#     time.sleep(1.8)
#     print("Main Thread Quit")
# if __name__ == '__main__':
#     start_threads()
#派生自己的线程类
# import sys, time
# import threading
# class CustomThread(threading.Thread):
#     def __init__(self,thread_name):
#         threading.Thread.__init__(self)
#         self.thread_name = thread_name
#     def run(self):
#         left_round = 10
#         print('start running')
#         while left_round>0:
#             print('Child Thread: Running, left round = %d' %left_round)
#             left_round-=1
#             time.sleep(0.5)
#         print('Child Thread Quit')
# def start_threads():
#     thread1 = CustomThread("thread 1 ")
#     thread1.setDaemon(False)
#     thread1.start()
#     time.sleep(0.8)
#     print("Active Thread Number = %d " %threading.active_count())
#     time.sleep(1.8)
#     print("Main Thread Quit")
# if __name__ == '__main__':
#     start_threads()
#停止线程(有部分问题)
# import threading
# import inspect, sys, time
# import ctypes
# def async_raise_exception(thread_id, exctypes):
#     tid = ctypes.c_long(thread_id)
#     if not inspect.isclass(exctypes):
#         exctypes = type(exctypes)
#     res = ctypes.pythonapi.PyThreadState_SetAsynExc(tid,ctypes.py_object(exctypes))
#     if res ==0:
#         raise ValueError("invalid thread id")
#     elif res!=1:
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,None)
#         raise SystemError("PyThreadState_SetAsyncExc failed")
#     raise SystemError("PyThreadState_SetAsyncExc failed")
# def thread_entry():
#     print("Child Thread Start Running")
#     while True:
#         try:
#             time.sleep(0.2)
#         except SystemExit:
#             print("Got an SystemExit Exception, Quit")
#             break
#     print("Child Thread Quit")
# def start_threads():
#     thread1 = threading.Thread(target=thread_entry())
#     thread1.setDaemon(False)
#     thread1.start()
#     time.sleep(2)
#     print("Active Number %d" %threading.active_count())
#     async_raise_exception(thread1.ident,SystemExit)
#     time.sleep(1)
#     print("Active Number %d" %threading.active_count())
#     print("Main Thread Quit")
# if __name__ == "__main__":
#     start_threads()
#等待线程结束
# import threading
# import inspect, sys, time
# def thread_entry():
#     left_round = 10
#     print('Child Thread: Strat Running')
#     while left_round>0:
#         print('Child Thread: Runnning, left round = %d' % left_round)
#         time.sleep(0.5)
#         left_round = left_round -1
#     print('Child Thread Quit')
# def start_threads():
#     thread1 = threading.Thread(target=thread_entry())
#     thread1.setDaemon(False)
#     thread1.start()
#     thread1.join()
#     print("Main Thread Quit")
# if __name__ == "__main__":
#     start_threads()
#线程锁thread.Lock,只能用在Thread设置的线程中
#不能解锁未锁上的线程，因此必须在start函数中先将read锁上
# read_lock = thread.allocate_lock()
# write_lock = thread.allocate_lock()
# x = 0
# def write_thread_entry():
#     global x, read_lock, write_lock
#     for i in range(2,10,1):
#         write_lock.acquire()
#         x = i
#         time.sleep(1)
#         read_lock.release()
# def read_thread_entry():
#     global x, read_lock,write_lock
#     while True:
#         read_lock.acquire()
#         print(x)
#         time.sleep(1)
#         write_lock.release()
# def start_threads():
#     read_lock.acquire()
#     t1 = thread.start_new_thread(write_thread_entry,tuple())
#     t2 = thread.start_new_thread(read_thread_entry,tuple())
#     time.sleep(20)
# if __name__ == '__main__':
#     start_threads()
#线程锁threading.Lock,只能用在threading设置的线程中
# ww = threading.Lock()
# rr = threading.Lock()
# x = 0
# def www():
#     global x,ww,rr
#     for i in range(1,10,1):
#         ww.acquire()
#         x = i
#         rr.release()
# def rrr():
#     global x,ww,rr
#     while x<9:
#         rr.acquire()
#         print(x)
#         ww.release()
# def sss():
#     rr.acquire()
#     t1 = threading.Thread(target=www)
#     t2 = threading.Thread(target=rrr)
#     t1.setDaemon(False)
#     t2.setDaemon(False)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# if __name__ == '__main__':
#     sss()
# 条件变量threading.Condition
# def thread_entry(id,condition_obj):
#     print(id)
#     for round in range(3):
#         with condition_obj:
#             condition_obj.wait()
#             print('%d Work' % id)
#             # time.sleep(0.1)
#             time.sleep(0.1*id)
#     print('%d Quit' %id)
# def start_threads():
#     condition_obj = threading.Condition()
#     t1 = threading.Thread(target=thread_entry,args=(1,condition_obj))
#     t1.start()
#     time.sleep(0.1)
#     t2 = threading.Thread(target=thread_entry,args=(2,condition_obj))
#     t2.start()
#     for round in range(3):
#         time.sleep(2)
#     # condition_obj.acquire()
#         with condition_obj:
#             condition_obj.notifyAll()
#         print(round)
#     # condition_obj.release()
# if __name__ == '__main__':
#     start_threads()
#信号量threading.Semaphore
# def thread_entry(id,Semaphore_obj):
#     print("Worker Thread %d" %id)
#     time.sleep(1.8)
#     for round in range(4):
#         Semaphore_obj.acquire()
#         print("id:%d" %id)
#         time.sleep(0.1*id)
#     print("%d Quit" %id)
# def start_threads():
#     Semaphore_obj = threading.Semaphore(3)
#     t1 = threading.Thread(target=thread_entry,args=(1,Semaphore_obj))
#     t1.start()
#     t2 = threading.Thread(target=thread_entry, args=(2, Semaphore_obj))
#     t2.start()
#     t3 = threading.Thread(target=thread_entry, args=(3, Semaphore_obj))
#     t3.start()
#     t4 = threading.Thread(target=thread_entry, args=(4, Semaphore_obj))
#     t4.start()
#     for round in range(13):
#         time.sleep(2)
#         print("Release")
#         Semaphore_obj.release()
#     print("end")
# if __name__ == '__main__':
#     start_threads()
#事件threading.Event
#set()闭合开关，clear()断开开关，wait()等待开关闭合
#新建Event对象开始都是非set状态，也就是断开的
# def thread_entry(id,evt):
#     print(id)
#     evt.wait()
#     print("%d Quit" %id)
# def start_threads():
#     event_obj = threading.Event()
#     thread1 = threading.Thread(target=thread_entry,args=(1,event_obj))
#     thread1.start()
#     thread2 = threading.Thread(target=thread_entry, args=(2, event_obj))
#     thread2.start()
#     thread3 = threading.Thread(target=thread_entry, args=(3, event_obj))
#     thread3.start()
#     time.sleep(0.8)
#     print("Active %d" %threading.active_count())
#     """active_count()显示的是当前存活的线程，包括主线程在内
#     """
#     time.sleep(1.8)
#     event_obj.set()
#     # a=event_obj.is_set()
#     # print(a)
#     # event_obj.clear()
#     print("Quit")
# if __name__ == "__main__":
#     start_threads()
#线程安全
#在修改同一个对象的时候，最好加上线程锁，保证线程安全
# mutex_lock = thread.allocate_lock()
# g_list = []
# def operate_resource():
#     global g_list
#     ele_num = len(g_list)
#     if ele_num == 0:
#         g_list.append(1)
#     else:
#         last_ele = g_list[ele_num-1]
#         new_last_ele = last_ele + 1
#         g_list.append(new_last_ele)
# def thread_entry(id, round):
#     while round >0:
#         mutex_lock.acquire()
#         operate_resource()
#         mutex_lock.release()
#         round -= 1
#     print("%d Finished" %id)
# def start_threads():
#     global g_list
#     t1 = thread.start_new_thread(thread_entry, (1,10000))
#     t2 = thread.start_new_thread(thread_entry, (2,10000))
#     time.sleep(10)
#     print("check")
#     loc = 0
#     while loc < 20000:
#         if g_list[loc] != (loc+1):
#             print("Wrong %d" %g_list[loc])
#             break
#         loc+=1
#     print("All Passed")
# if __name__ == "__main__":
#     start_threads()
