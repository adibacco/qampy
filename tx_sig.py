# first arg is file with td waveform, second is antenna port
import sys, os, subprocess

WAVEFORM_TX=sys.argv[1]
TARGET_ADDR_DDR=0x2380000000
VSPA_BUFFER_ADDR=0x40000000

OFFSET_TX_SECTION = 0
OFFSET_TX_CH=0x40000

DCS_TX=sys.argv[2]
ANTENNA_PORT_TX=int(sys.argv[3])

def run_process(args):
    os.system(args)

WAVE_LEN = os.stat(WAVEFORM_TX).st_size

print('Wave len ' + str(WAVE_LEN))

print('DDR target ' + hex(TARGET_ADDR_DDR))
print('VSPA Buffer ' + hex(VSPA_BUFFER_ADDR))
print('Antenna port ' + str(ANTENNA_PORT_TX))
print('DCS ' + str(DCS_TX))


toks = sys.argv[1].split('-')
DMA_SIZE = toks[1]

if (WAVE_LEN < 1024):
    print('NOT ENOUGH SAMPLES')
    quit()

for dma in range(16384, 1, -1):
    if (WAVE_LEN % dma == 0):
        DMA_SIZE = dma
        break

if (dma < 64): 
    print('DMA SIZE WRONG ' + str(DMA_SIZE))
    quit() 

b2m = '/home/root/l1t-lite/bin2mem -f ' + WAVEFORM_TX + ' -a ' + hex(TARGET_ADDR_DDR + ANTENNA_PORT_TX*OFFSET_TX_CH + OFFSET_TX_SECTION) + ' -c 4'
print(b2m)
run_process(b2m)


cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_TX) + '.py cfg buff tx 0 ' + hex(VSPA_BUFFER_ADDR + ANTENNA_PORT_TX*OFFSET_TX_CH + OFFSET_TX_SECTION) + ' ' + str(DMA_SIZE) + ' ' + str(WAVE_LEN) + ' ' + str(ANTENNA_PORT_TX)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_TX) + '.py cfg patt tx 0 0 0 1 0 1.0 ' + str(ANTENNA_PORT_TX)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_TX) + '.py init tx ' + str(ANTENNA_PORT_TX) + ' 4294967295 0'
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_TX) + '.py start tx ' + str(ANTENNA_PORT_TX)
print(cmd)
run_process(cmd)



