## Splitted APK
> Buat reduce size (Kasih APK yang compatible aja)
> extractnya (adb shell pm path id.pinhome.consumer)
pm (package manager)
am (activity manager)
> adb pull /data/app/id.pinhome.consumer-1/

## Merge APK
> java -jar "C:\Users\ardia\OneDrive - Bina Nusantara\Tools\APKEditor-1.1.7-UPDATE-5.jar" m -i "C:\Users\ardia\OneDrive - Bina Nusantara\INSIGNIA VENTURES\Work (Bug Hunter and Penetration Tester)\PinHome\id.pinhome.consumer-1"

## CheckSign
> Agar bisa diinstall di android, harus di checksign dulu
> android butuh certificate dulu, di folder meta.inf
> java -jar "C:\Users\ardia\OneDrive - Bina Nusantara\Tools\uber-apk-signer-1.3.0.jar" -a id.pinhome.consumer-1_merged.apk
