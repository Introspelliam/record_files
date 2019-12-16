import os, glob

classes = {
    "air.com.hypah.io.slither":0,
    "at.DiTronic.androidgroup.randomgallery":0,
    "com.android.chrome":0,
    "com.antutu.ABenchMark":0,
    "com.booking":0,
    "com.cnn.mobile.android.phone":0,
    "com.csst.ecdict":0,
    "com.facebook.katana":0,
    "com.google.android.apps.photos":0,
    "com.google.android.deskclock":0,
    "com.instagram.android":0,
    "com.isis_papyrus.raiffeisen_pay_eyewdg":0, 
    "com.lenovo.anyshare.gps":0,
    "com.paypal.android.p2pmobile":0,
    "com.skype.raider":0,
    "com.sololearn.cplusplus":0,
    "com.sometimeswefly.littlealchemy":0, 
    "com.ted.android":0,
    "com.tripadvisor.tripadvisor":0,
    "com.whatsapp":0
}


def main():
    for train_size in range(10, 80, 10):
        if not os.path.exists(str(train_size)):
            os.mkdir(str(train_size))
        train_dir = str(train_size)+"/train"
        test_dir = str(train_size)+"/test"
        test_size = int(train_size*3/7)
        if not os.path.exists(train_dir):
            os.mkdir(train_dir)
        os.system("rm -rf {}/*".format(train_dir))
        if not os.path.exists(test_dir):
            os.mkdir(test_dir)
        os.system("rm -rf {}/*".format(test_dir))

        # train
        for file in glob.glob(os.path.join("train/", "*.txt")):
            for app in classes:
                classes[app] = train_size
            file_name = file.split("/")[1]
            with open(file) as f:
                for line in f:
                    line_token = line.split(',')
                    number_of_data_points = len(line_token) - 2 
                    current_label = line_token[number_of_data_points].strip()
                    if classes[current_label] != 0:
                        open(train_dir+"/"+file_name, "a").write(line)
                        classes[current_label] -= 1

        # test
        for file in glob.glob(os.path.join("test/", "*.txt")):
            for app in classes:
                classes[app] = test_size
            file_name = file.split("/")[1]
            with open(file) as f:
                for line in f:
                    line_token = line.split(',')
                    number_of_data_points = len(line_token) - 2 
                    current_label = line_token[number_of_data_points].strip()
                    if classes[current_label] != 0:
                        open(test_dir+"/"+file_name, "a").write(line)
                        classes[current_label] -= 1
        

if __name__ == "__main__":
    main()