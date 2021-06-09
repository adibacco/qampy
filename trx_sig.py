import sys, os, subprocess


# <waveform_tx> <dcs_tx> <antenna_port_tx> <waveform_rx> <dcs_rx> <antenna_port_rx>

WAVEFORM_TX=sys.argv[1]
TARGET_ADDR_DDR=0x2380000000
VSPA_BUFFER_ADDR=0x40000000

OFFSET_TX_SECTION = 0
OFFSET_TX_CH=0x40000

DCS_TX=sys.argv[2]
ANTENNA_PORT_TX=int(sys.argv[3])

WAVEFORM_RX=sys.argv[4]

OFFSET_RX_SECTION=0x1000000
OFFSET_RX_CH=0x40000

DCS_RX=sys.argv[5]
ANTENNA_PORT_RX=int(sys.argv[6])


def run_process(args):
    os.system(args)



print('DDR target ' + hex(TARGET_ADDR_DDR))
print('VSPA Buffer ' + hex(VSPA_BUFFER_ADDR))
print('Antenna port TX ' + str(ANTENNA_PORT_TX))
print('DCS TX ' + str(DCS_TX))
print('Antenna port RX ' + str(ANTENNA_PORT_RX))
print('DCS RX ' + str(DCS_RX))

b2m = '/home/root/l1t-lite/bin2mem -f ' + WAVEFORM_TX + ' -a ' + hex(TARGET_ADDR_DDR + ANTENNA_PORT_TX*OFFSET_TX_CH + OFFSET_TX_SECTION) + ' -c 4'
print(b2m)
run_process(b2m)

toks = sys.argv[1].split('-')
dma = toks[1]
transfer = toks[2]

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_TX) + '.py cfg buff tx 0 ' + hex(VSPA_BUFFER_ADDR + ANTENNA_PORT_TX*OFFSET_TX_CH + OFFSET_TX_SECTION) + ' ' + str(dma) + ' ' + str(transfer) + ' ' + str(ANTENNA_PORT_TX)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_TX) + '.py cfg patt tx 0 0 0 1 0 1.0 ' + str(ANTENNA_PORT_TX)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_TX) + '.py init tx ' + str(ANTENNA_PORT_TX) + ' 4294967295 0'
print(cmd)
run_process(cmd)

# RX


cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_RX) + '.py cfg buff rx 0 ' + hex(VSPA_BUFFER_ADDR + ANTENNA_PORT_RX*OFFSET_RX_CH + OFFSET_RX_SECTION) + ' ' + str(dma) + ' ' + str(transfer) + ' ' + str(ANTENNA_PORT_RX)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_RX) + '.py cfg patt rx 0 0 0 1 0 0.0 ' + str(ANTENNA_PORT_RX)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_RX) + '.py init rx ' + str(ANTENNA_PORT_RX) + ' 4294967295 0'
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_TX) + '.py start trx ' + str(ANTENNA_PORT_TX)
print(cmd)
run_process(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS_RX) + '.py stop trx ' + str(ANTENNA_PORT_TX)
print(cmd)
run_process(cmd)

m2f = '/home/root/l1t-lite//bin2mem -f ' + WAVEFORM_RX + ' -a ' + hex(TARGET_ADDR_DDR + ANTENNA_PORT_RX*OFFSET_RX_CH + OFFSET_RX_SECTION) + ' -c 4 -r ' + str(transfer)
print(m2f)
run_process(m2f)


