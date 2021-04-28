# first arg is file with td waveform, second is antenna port

import sys, os, subprocess

WAVEFORM=sys.argv[1]
TARGET_ADDR_DDR=0x2380000000
VSPA_BUFFER_ADDR=0x40000000
OFFSET_RX_SECTION=0x1000000
OFFSET_CH=0x40000

DCS=sys.argv[2]
ANTENNA_PORT=int(sys.argv[3])

def run_process(args):
    os.system(args)


DMA=sys.argv[4]
TRANSFER=sys.argv[5]


print('DDR target ' + hex(TARGET_ADDR_DDR))
print('VSPA Buffer ' + hex(VSPA_BUFFER_ADDR))
print('Antenna port ' + str(ANTENNA_PORT))
print('DCS ' + str(DCS))

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py cfg buff rx 0 ' + hex(VSPA_BUFFER_ADDR + ANTENNA_PORT*OFFSET_CH + OFFSET_RX_SECTION) + ' ' + str(DMA) + ' ' + str(TRANSFER) + ' ' + str(ANTENNA_PORT)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py cfg patt rx 0 0 0 1 0 0.0 ' + str(ANTENNA_PORT)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py init rx ' + str(ANTENNA_PORT) + ' 4294967295 0'
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py start rx ' + str(ANTENNA_PORT) 
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py stop rx ' + str(ANTENNA_PORT)
print(cmd)
run_process(cmd)

m2f = '/home/root/l1t-lite//bin2mem -f ' + WAVEFORM + ' -a ' + hex(TARGET_ADDR_DDR + ANTENNA_PORT*OFFSET_RX + DCS*OFFSET_DCS) + ' -c 4 -r ' + str(TRANSFER)
print(m2f)
run_process(m2f)

