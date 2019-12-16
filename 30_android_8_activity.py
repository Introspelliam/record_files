import os, sys

files = [
        "-proc-meminfo__MemFree_c1.txt",
        "-proc-meminfo__Active:_c1.txt",
        "-proc-meminfo__AnonPages_c1.txt",
        "-proc-meminfo__Mapped_c1.txt",
        "-proc-meminfo__HighFree_c1.txt",
        "-proc-meminfo__Active\\(anon\\)_c1.txt",
        "-proc-net-sockstat__sockets_c2.txt",
        "-proc-meminfo__PageTables_c1.txt",
        "-proc-net-protocols__UNIX_c2.txt",
        "-proc-meminfo__LowFree_c1.txt"
        ]

source_train_dir = "30_android_8_activity_train"
source_test_dir = "30_android_8_activity_test"
train_dir = "30_android_8_activity_train2"
test_dir = "30_android_8_activity_test2"

if not os.path.exists(train_dir):
    os.mkdir(train_dir)
if not os.path.exists(test_dir):
    os.mkdir(test_dir)

for filename in files:
    os.system("cp -f {} {}".format(source_train_dir+"/"+filename, train_dir+"/"+filename))
    os.system("cp -f {} {}".format(source_test_dir+"/"+filename, test_dir+"/"+filename))
