# IOS Pentest Cheatsheet

## Jailbreak

### Terminology
#### Tethered
- Requires a computer to boot the device into a jailbroken state
- The jailbreak is lost when the device is rebooted

#### Untethered
- Does not require a computer to boot the device into a jailbroken state
- The jailbreak persists after the device is rebooted

#### Semi-untethered
- The jailbreak persists after the device is rebooted
- Does not requires a computer to re-enable the jailbreak

#### Semi-tethered
- The jailbreak is lost when the device is rebooted
- Require a computer to re-enable the jailbreak

### Rootful vs Rootless
#### Rootful
- The device is jailbroken and the user has root access to the filesystem (RootFS)
- The user can access and modify any file on the filesystem
- File location is in /root
- Dodge SSV (Signed System Volume) and remounting the filesystem as read-write

#### Rootless
- The device is jailbroken but the user does not have root access to the filesystem (RootFS)
- The user can access and modify only a subset of files on the filesystem
- File location is in /var/jb

### Jailbreak Tools
For more info you can check https://ios.cfw.guide/ 

### Installing Tweaks
#### Sileo
Sileo is a package manager for jailbroken devices. It is a modern alternative to Cydia. Install tweaks using Sileo by adding a repository and searching for the tweak you want to install.

#### Zebra
Same with Sileo, Zebra is a package manager for jailbroken devices.

### Common Tweaks
#### Filza
Filza is a file manager for jailbroken devices. It allows you to browse the filesystem, view and edit files, and install .deb packages.

#### App Manager
App Manager is a tweak that allows you to view and manage installed apps on your device. You can view app data, delete apps, and backup data.

#### Frida
Frida is a dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers. It allows you to inject JavaScript into running processes to hook functions, intercept data, and modify behavior.

#### Shadow
Shadow is a tweak that allows you to run apps in a sandboxed environment. Usually used for jailbreak detection bypass.

#### SSL Kill Switch
SSL Kill Switch is a tweak that disables SSL certificate validation in apps. It allows you to intercept and modify HTTPS traffic using a proxy like Burp Suite.

#### TrollStore
TrollStore is a tweak that allows you to install unsigned apps on your device. It is useful for installing apps that are not available on the App Store.

### Sign IPA
#### CodeSign
CodeSign is a tool that allows you to sign IPA files with your Apple ID. It is useful for installing apps on your device without a computer.

#### AltStore
AltStore is a sideloading tool for iOS that allows you to install unsigned apps on your device. It requires a computer to install and refresh apps every 7 days.

#### TrollStore
TrollStore is a tweak that allows you to install unsigned apps on your device. It is useful for installing apps that are not available on the App Store.

### Extracting IPA
- Filza (Apps)
- Frida IOS Dump (Script)
- TrollDecrypt (Apps)

### More Tools
- QuickTime Player (Screen Recording)
- IAmLazy (Backup Tweaks)
- nano (Text Editor)
- XCode (Development or Patch)
- Hopper (Disassembler)
- IDA Pro (Disassembler)


### Common Findings
- Jailbreak Detection
- SSL Pinning Bypass
- Insecure Data Storage
- Clipboard on Sensitive Data
- Sensitive key in Info.plist
- None or Weak Dynamic Instrumentation Protection
- Un-blurred Screen from Multitasking
- Missing Package Integrity Check
