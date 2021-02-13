wget 
qemu-system-mips -cpu 4Kc -kernel mipsimage.boot -append "console=devices/\\hw\\pci0\\00:0a.0\\com1\\a" -nographic
