import os, sys

files = [
        "-proc-net-xt_qtaguid-iface_stat_fmt__wlan0_c5.txt",
        "-proc-net-xt_qtaguid-iface_stat_fmt__wlan0_c1.txt",
        "-proc-net-dev__wlan0:_c2.txt",
        "-proc-net-xt_qtaguid-iface_stat_all__wlan0_c6.txt",
        "-proc-net-netstat__IpExt:_c7.txt",
        "-proc-net-xt_qtaguid-iface_stat_fmt__wlan0_c2.txt",
        "-proc-net-xt_quota-globalAlert__l0_c0.txt",
        "-proc-net-dev__wlan0:_c3.txt",
        "-proc-net-snmp__Tcp:_c10.txt",
        "-proc-net-xt_qtaguid-iface_stat_fmt__wlan0_c11.txt"
        ]

source_train_dir = "29_android_9_websites_train"
source_test_dir = "29_android_9_websites_test"
train_dir = "29_android_9_websites_train2"
test_dir = "29_android_9_websites_test2"

if not os.path.exists(train_dir):
    os.mkdir(train_dir)
if not os.path.exists(test_dir):
    os.mkdir(test_dir)

for filename in files:
    os.system("cp -f {} {}".format(source_train_dir+"/"+filename, train_dir+"/"+filename))
    os.system("cp -f {} {}".format(source_test_dir+"/"+filename, test_dir+"/"+filename))
