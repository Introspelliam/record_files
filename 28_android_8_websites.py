import os, sys

files = [
        "-proc-net-netstat__IpExt:_c7.txt",
        "-proc-net-netstat__IpExt:_c8.txt",
        "-proc-net-snmp__Ip:_c10.txt",
        "-proc-meminfo__Shmem_c1.txt",
        "-proc-meminfo__Cached_c1.txt",
        "-proc-net-snmp__Ip:_c3.txt",
        "-proc-net-snmp__Ip:_c9.txt",
        "-proc-net-xt_qtaguid-iface_stat_fmt__wlan0_c5.txt",
        "-proc-net-xt_qtaguid-iface_stat_all__wlan0_c8.txt",
        "-proc-meminfo__Inactive\\(anon\\)_c1.txt"
        ]

source_train_dir = "28_android_8_websites_train"
source_test_dir = "28_android_8_websites_test"
train_dir = "28_android_8_websites_train2"
test_dir = "28_android_8_websites_test2"

if not os.path.exists(train_dir):
    os.mkdir(train_dir)
if not os.path.exists(test_dir):
    os.mkdir(test_dir)

for filename in files:
    os.system("cp -f {} {}".format(source_train_dir+"/"+filename, train_dir+"/"+filename))
    os.system("cp -f {} {}".format(source_test_dir+"/"+filename, test_dir+"/"+filename))
