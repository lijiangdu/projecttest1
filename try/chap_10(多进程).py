import time, os, sys, random
import multiprocessing
#multiprocess模块
#创建进程
# def process_entry():
#     print(u"子进程在运行")
#     print("子进程的id = %d" %os.getpid())
# if __name__ == "__main__":
#     print("父进程的id = %id" %os.getpid())
#     p = multiprocessing.Process(target=process_entry)
#     time.sleep(1)
#     print("启动子进程")
#     p.start()
#     time.sleep(2)
#     print("父进程结束")
#带参数创建进程
# def process_entry(arg1):
#     print("子进程%d正在运行" %arg1)
#     print("子进程%dID为%d" %(arg1,os.getpid()))
# if __name__ == "__main__":
#     print("父进程id为%d" %os.getpid())
#     p1 = multiprocessing.Process(target=process_entry,args=(1,))
#     p2 = multiprocessing.Process(target=process_entry,args=(2,))
#     time.sleep(1)
#     print("启动子进程")
#     p1.start()
#     p2.start()
#     time.sleep(2)
#     print("父进程结束")
#从Process派生一个自己的类创建进程，启动时运行run()函数
# class NewProcess(multiprocessing.Process):
#     def __init__(self,arg):
#         super(NewProcess,self).__init__()
#         self.arg = arg
#     def run(self):
#         print("子进程%d正在运行" %self.arg)
#         print("子进程%d的id=%d"%(self.arg,os.getpid()))
#         while True:
#             time.sleep(10)
#             print(self.arg)
# if __name__ == "__main__":
#     print("父进程的id=%d" %os.getpid())
#     p1 = NewProcess(1)
#     p2 = NewProcess(2)
#     time.sleep(2)
#     print("启动子进程")
#     p1.start()
#     p2.start()
#     time.sleep(2)
#     print("父进程结束")
#进程的属性
#子进程的id在创建之后就确定了，但是ident必须在子进程运行后才有，两者是一样的对象
# def child_process_entry():
#     pid = os.getpid()
#     ppid = os.getppid()
#     print("子进程PID：%dPPID：%d" %(pid,ppid))
#     while True:
#         time.sleep(1)
# if __name__ == "__main__":
#     multiprocessing.freeze_support()
#     main_pid = os.getpid()
#     main_ppid = os.getppid()
#     print("主进程的PID=%d,PPID=%d" %(main_pid,main_ppid))
#     child_process = multiprocessing.Process(target=child_process_entry)
#     child_process.start()
#     print(child_process.ident)
#可以修改进程的Daemon属性，当进程为Daemon进程时，当主进程结束时，子进程也结束，如果进程不是Daemon进程，那么主进程结束后子进程不一定结束
# def child_entry():
#     pid = os.getpid()
#     ppid = os.getppid()
#     print("子进程pid:%d,ppid:%d"%(pid,ppid))
#     print("子进程正在运行")
#     for i in range(5):
#         print("子进程pid:%d,ppid:%d" % (pid, ppid))
#         print("子进程正在运行,%d"%i)
#         time.sleep(1)
# if __name__ == '__main__':
#     print("父进程id %d"%os.getpid())
#     p1 = multiprocessing.Process(target=child_entry)
#     p1.start()
#     time.sleep(2)
#     print("父进程结束")
#进程返回码
# def process_entry(arg1):
#     sys.exit(arg1)
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=process_entry,args=(5,),daemon=True)
#     p1.start()
#     time.sleep(1)
#     print(p1.exitcode)
#强制退出Kill()
# def process_entry():
#     while True:
#         print("子程序正在运行中")
#         time.sleep(1)
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=process_entry,daemon=False)
#     p1.start()
#     if p1.is_alive():
#         print("子程序正在运行中")
#     else:
#         print("子程序已经结束运行")
#     time.sleep(1)
#     print("强制退出子程序")
#     p1.kill()
#     time.sleep(0.1)
#     if p1.is_alive():
#         print("子程序正在运行中")
#     else:
#         print("子程序已经结束运行")
#进程池
#用于从进程池中取出一个进程来进行任务，复用部分已有进程资源，达到提升效率的作用
# def child1_entry(arg1):
#     print("进程%d正在child1运行" %arg1)
#     time.sleep(arg1)
#     print("进程%d停止child1运行" %arg1)
# def child2_entry(arg1):
#     print("进程%d正在child2运行" %arg1)
#     time.sleep(arg1)
#     print("进程%d停止child2运行" %arg1)
# if __name__ == "__main__":
#     pool_obj = multiprocessing.Pool(processes=5)
#     for i in range(1,11,2):
#         pool_obj.apply_async(child1_entry,args=(i,))
#         pool_obj.apply_async(child2_entry, args=(i+1,))
#     pool_obj.close()
#     pool_obj.join()
#进程通信
#管道
# def process_A(s):
#     print("进程A发送hello给B")
#     s.send('hello')
#     print("进程A等待B的数据")
#     data = s.recv()
#     print("进程A结束")
# def process_B(s):
#     print("进程B等待进程A的数据")
#     data = s.recv()
#     print("进程B收到进程A的数据%s" %data)
#     print("进程B发送数据给进程A")
#     s.send('hi')
#     print("进程B结束")
# if __name__ == "__main__":
#     multiprocessing.freeze_support()
#     s = multiprocessing.Pipe()
#     p1 = multiprocessing.Process(target=process_A, args=(s[0],))
#     p2 = multiprocessing.Process(target=process_B, args=(s[1],))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#队列
# def process_read(queue):
#     print("读出程序正在运行")
#     data = queue.get()
#     while (data!='Quit'):
#         print("读出的数据为%s" %data)
#         data = queue.get()
#     print("读出进程退出")
# def process_write(queue):
#     print("写入程序正在运行")
#     data = ['morning','afternoon','evening','none']
#     for w in data:
#         print("写入进程写入数据%s" %w)
#         data = queue.put(w)
#         time.sleep(1)
#     data = queue.put('Quit')
#     print("写入程序退出")
# if __name__ == "__main__":
#     multiprocessing.freeze_support()
#     queue_obj = multiprocessing.Queue(2)
#     p1 = multiprocessing.Process(target=process_read,args=(queue_obj,))
#     p2 = multiprocessing.Process(target=process_write, args=(queue_obj,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#锁Lock
#该实例不能运行是因为python版本的问题，3.7及以下的可以运行
# def process_entry(lock,fd,id):
#     for x in range(30):
#         # lock.acquire()
#         # line = "%d: line 1, round: %d\n" %(id,x)
#         # fd.write(line)
#         # fd.flush()
#         # time.sleep(0.1)
#         # line = "%d: line 2, round: %d\n" % (id, x)
#         # fd.write(line)
#         # fd.flush()
#         # time.sleep(0.1)
#         # line = "%d: line 3, round: %d\n" % (id, x)
#         # fd.write(line)
#         # fd.flush()
#         # lock.release()
#         # time.sleep(0.1)
#         with lock:
#             line = "%d: line 1, round: %d\n" % (id, x)
#             fd.write(line)
#             fd.flush()
#             time.sleep(0.1)
#             line = "%d: line 2, round: %d\n" % (id, x)
#             fd.write(line)
#             fd.flush()
#             time.sleep(0.1)
#             line = "%d: line 3, round: %d\n" % (id, x)
#             fd.write(line)
#             fd.flush()
#             time.sleep(0.1)
# if __name__ =="__main__":
#     file_name ="111.txt"
#     fd = open(file_name,"a+")
#     lock = multiprocessing.Lock()
#     p1 = multiprocessing.Process(target=process_entry, args=(lock, fd, 1))
#     p2 = multiprocessing.Process(target=process_entry, args=(lock, fd, 2))
#     p3 = multiprocessing.Process(target=process_entry, args=(lock, fd, 3))
#     p1.start()
#     p2.start()
#     p3.start()
#     # p1.run()
#     # p2.run()
#     # p3.run()
#     # p1.join()
#     # p2.join()
#     # p3.join()
#     fd.close()
#     print("开始检查结果")
#     fd2 = open(file_name,"r",encoding="utf-8")
#     lines = fd2.readlines()
#     fd2.close()
#     line_num = len(lines)
#     print("总行数%d" %line_num)
#     for x in range(int(line_num/3)):
#         if lines[x*3][:2] != lines[x*3+1][:2]:
#             #列表中A[:2]表示从第最开始到第1个，A[2:]表示从第2个到结尾A[2,:]表示所有行的第三列
#             print("error")
#             sys.exit(1)
#         if lines[x * 3][:2] != lines[x * 3 + 2][:2]:
#             print("error")
#             sys.exit(1)
#     print("成功通过检查")