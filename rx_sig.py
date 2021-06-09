# first arg is file with td waveform, second is antenna port

import sys, os, subprocess

WAVEFORM_RX=sys.argv[1]
TARGET_ADDR_DDR=0x2380000000
VSPA_BUFFER_ADDR=0x40000000
OFFSET_RX_SECTION=0x1000000
OFFSET_RX_CH=0x40000

DCS_RX=sys.argv[2]
ANTENNA_PORT_RX=int(sys.argv[3])

def run_process(args):
    os.system(args)
 
 
toks = sys.argv[1].split('-')
DMA=toks[1]
TRANSFER=toks[2]



print('DDR target ' + hex(TARGET_ADDR_DDR))
print('VSPA Buffer ' + hex(VSPA_BUFFER_ADDR))
print('Antenna port ' + str(ANTENNA_PORT_RX))
print('DCS ' + str(DCS_RX))
print('DMA ' + str(DMA))

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_RX) + '.py cfg buff rx 0 ' + hex(VSPA_BUFFER_ADDR + ANTENNA_PORT_RX*OFFSET_RX_CH + OFFSET_RX_SECTION) + ' ' + str(DMA) + ' ' + str(TRANSFER) + ' ' + str(ANTENNA_PORT_RX)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_RX) + '.py cfg patt rx 0 0 0 1 0 0.0 ' + str(ANTENNA_PORT_RX)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_RX) + '.py init rx ' + str(ANTENNA_PORT_RX) + ' 4294967295 0'
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_RX) + '.py start rx ' + str(ANTENNA_PORT_RX) 
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_RX) + '.py stop rx ' + str(ANTENNA_PORT_RX)
print(cmd)
run_process(cmd)

m2f = '/home/root/l1t-lite//bin2mem -f ' + WAVEFORM_RX + ' -a ' + hex(TARGET_ADDR_DDR + ANTENNA_PORT_RX*OFFSET_RX_CH + OFFSET_RX_SECTION) + ' -c 4 -r ' + str(TRANSFER)
print(m2f)
run_process(m2f)

