## Splitted APK (Kalau kita bisa split dan merge, kita bisa edit base.apk dan jadi apapun yang kita mau, kita bisa masukkin malware, keylogger, inejct JS dll. Kalau ada integrity checking, harusnya pas merge ada warning - The App has been modified, dll)
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


## Detection on Reverse Engineering Framework Toolings
> Harusnya, kalo ada frida or objection jalan, aplikasi harusnya bisa detect dan force exit. 
> Kalo kita masih bisa jalanin script frida kyk yang buat bypass ssl pinning, or munculin alert pake frida, harusnya exit. Kalo gk exit or masih bisa jalan appnya, jadi finding.
> frida -U -f <target_app> -l <frida_script>


## Accessing Shared Preference
> cd /data/data/com.cashlez.android.garuda.allinone.staging/shared_prefs


