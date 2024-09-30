

# EFI system partition

The EFI system partition (also called ESP) is an OS independent partition that acts as the storage place for the UEFI boot loaders, applications and drivers to be launched by the UEFI firmware. It is mandatory for UEFI boot.

当Windows系统安装的时候，会在磁盘的第0扇区划分一个EFI partition，一般的boot loader会在这个partition中存放引导系统启动的程序。
因此，在安装Linux的时候，不用特殊在划分一个EFI partition，一般Linux使用grub作为boot loader。
安装Ubuntu时，需要划分一个boot分区，因为EFI partition会挂载到/boot/efi,Linux的内核和启动程序会安装在/boot,而Arch Linux 同样将内核和启动程序安装在/boot, 可以将Windows划分的EFI partition 挂载到/boot/efi,也可以挂载到/efi,这里更建议挂载到/efi。安装完成之后，grub程序会在EFI partition中保留启动程序。
在文件系统中可以看到：
