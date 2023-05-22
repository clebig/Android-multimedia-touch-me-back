# Android-multimedia-touch-me-back (ex Photovid_android-retoucher)
Python script that "re"touch photos and videos pulled from Android devices with ADB

When doing backups of multimedia files using adb pull, adb doesn't restore files' access, modification and creation times.
This prevents some photos/videos management softwares to automaticaly sort them by date.
This script will restore modification and access times using the file names. It seems common that photos and videos 
are named by Android (at least native photos apps for AOSP, CrDroid, Lineage and OpenCamera) using patterns found among all mentioned photo apps that can be catched up using the following regex '.*([\d]{8})_([\d]{6}).*\..+\Z' .
