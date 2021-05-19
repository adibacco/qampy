echo 7 > /proc/sys/kernel/printk; echo 1 > /sys/bus/pci/rescan
insmod /lib/modules/4.19.90-rt35/extra/yami.ko scratch_buf_size=0x8000000 scratch_buf_phys_addr=0x2380000000

