# first arg is file with td waveform, second is antenna port
import sys, os, subprocess

WAVEFORM=sys.argv[1]
TARGET_ADDR_DDR=0x2380000000
VSPA_BUFFER_ADDR=0x40000000

OFFSET_TX_SECTION = 0
OFFSET_CH=0x40000

DCS=sys.argv[2]
ANTENNA_PORT=sys.argv[3]

def run_process(args):
    os.system(args)



print('DDR target ' + hex(TARGET_ADDR_DDR))
print('VSPA Buffer ' + hex(VSPA_BUFFER_ADDR))
print('Antenna port ' + str(ANTENNA_PORT))
print('DCS ' + str(DCS))


b2m = '/home/root/l1t-lite/bin2mem -f ' + WAVEFORM + ' -a ' + hex(TARGET_ADDR_DDR) + ' -c 4'
print(b2m)
run_process(b2m)

toks = sys.argv[1].split('-')


cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py cfg buff tx 0 ' + hex(VSPA_BUFFER_ADDR + ANTENNA_PORT*OFFSET_CH + OFFSET_TX_SECTION) + ' ' + str(toks[1]) + ' ' + str(toks[2]) + ' ' + str(ANTENNA_PORT)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py cfg patt tx 0 0 0 1 0 1.0 ' + str(ANTENNA_PORT)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py init tx ' + str(ANTENNA_PORT) + ' 4294967295 0'
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py start tx ' + str(ANTENNA_PORT)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py start tx ' + str(ANTENNA_PORT)
print(cmd)
run_process(cmd)


