# import random
# import time


# def download_task(filename):
#     print('start download %s ...' % filename)
#     time_to_download = random.randint(5, 10)
#     time.sleep(time_to_download)
#     print('%s download end ! time  is %d s ' % (filename, time_to_download))


# def main():
#     start = time.time()
#     download_task('python.pdf')
#     download_task('pk.avi')
#     end = time.time()
#     print('Time all is %.2f' % (end - start))


# if __name__ == '__main__':
#     main()


import multiprocessing
import os
import random
import time


def download_task(filename):
    print('启动下载，进程号为[%d].' % os.getpid())
    print('开始下载%s...' % filename)
    time_to_download = random.randint(5, 10)
    time.sleep(time_to_download)
    print('%s下载完成，总共耗时%d秒' % (filename, time_to_download))


def main():
    start = time.time()
    p1 = multiprocessing.Process(target=download_task, args=('python.pdf', ))
    p1.start()
    p2 = multiprocessing.Process(target=download_task, args=('pk.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print('总共耗时%.2f秒' % (end - start))


if __name__ == '__main__':
    main()
