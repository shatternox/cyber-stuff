Checklist:
- Root Detection
- Emulator Detection
- Frida Detection
- Exposed Window Layout
- Screenshot Protection
- Android Backup
- Strandhogg
- Smali patching
- Shared Preference
- Custom Keyboard
- Hardcoded Secrets



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


## AAB to APK
Bundletool = https://github.com/google/bundletool/releases
> bundletool build-apks --bundle=/MyApp/my_app.aab --output=/MyApp/my_app.apks
> apksnya di ekstract aja (click kanan extract here)
> nanti ada folder splits, tinggal dimerge aja kyk biasa


## Smali patching

1. apktool d com.easeapp-1_merged-aligned-debugSigned.apk

2. smali > nama packagenya, ex: com > easeapp

3. cari activity yg mau diinject, ex: MainActivity.smali

4. cari function yang mau diinject, ex: onCreate

5. masukkin injection code di bawah locals, localsnya + 2 (ato gk + 4 minimal)

6. apktool b com.easeapp-1_merged-aligned-debugSigned (ini folder hasil decompilenya)

7. java -jar ~/tools/uber-apk-signer-1.3.0.jar -a com.easeapp-1_merged-aligned-debugSigned/dist/com.easeapp-1_merged-aligned-debugSigned.apk

8. install lagi dan boom!


>> Injection code
```
const/4 v0, 0x1

const-string v1, "PoC Visit My Evil Site (https[://]evil.com)"

invoke-static {p0, v1, v0}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

move-result-object v0

invoke-virtual {v0}, Landroid/widget/Toast;->show()V
```


## Loki Keyboard Log Location (for keylogging testing)
/data/media/0/Android/data/com.abifog.lokiboard/files/




