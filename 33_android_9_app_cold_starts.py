import os, sys

files = [
        "-proc-net-protocols__UNIX_c2.txt",
        "-proc-meminfo__Mapped_c1.txt",
        "-proc-net-sockstat__sockets_c2.txt",
        "-proc-meminfo__AnonPages_c1.txt",
        "-proc-meminfo__Committed_AS_c1.txt",
        "-proc-meminfo__Active\\(anon\\)_c1.txt",
        "-proc-meminfo__VmallocUsed_c1.txt",
        "-proc-net-sockstat__TCP:_c8.txt",
        "-proc-meminfo__Shmem_c1.txt",
        "-proc-net-protocols__TCPv6_c2.txt"
        ]

source_train_dir = "33_android_9_app_cold_starts_train"
source_test_dir = "33_android_9_app_cold_starts_test"
train_dir = "33_android_9_app_cold_starts_train2"
test_dir = "33_android_9_app_cold_starts_test2"

if not os.path.exists(train_dir):
    os.mkdir(train_dir)
if not os.path.exists(test_dir):
    os.mkdir(test_dir)

for filename in files:
    os.system("cp -f {} {}".format(source_train_dir+"/"+filename, train_dir+"/"+filename))
    os.system("cp -f {} {}".format(source_test_dir+"/"+filename, test_dir+"/"+filename))
