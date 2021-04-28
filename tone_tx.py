# first arg is file with td waveform, second is antenna port
import sys, os

TARGET_ADDR_DDR=0x2380000000
VSPA_BUFFER_ADDR=0x40000000

DCS=sys.argv[2]
ANTENNA_PORT=sys.argv[3]




print('DDR target ' + hex(TARGET_ADDR_DDR))
print('VSPA Buffer ' + hex(VSPA_BUFFER_ADDR))
print('Antenna port ' + str(ANTENNA_PORT))
print('DCS ' + str(DCS))


b2m = '/home/root/l1t-lite/bin2mem -f ' + sys.argv[1] + ' -a ' + hex(TARGET_ADDR_DDR) + ' -c 4'
print(b2m)
os.system(b2m)

toks = sys.argv[1].split('@')


cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py cfg buff tx 0 ' + hex(VSPA_BUFFER_ADDR) + ' ' + str(toks[1]) + ' ' + str(toks[2]) + ' ' + str(ANTENNA_PORT)
print(cmd)
os.system(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py cfg patt tx 0 0 0 1 0 1.0 ' + str(ANTENNA_PORT)
print(cmd)
#os.system(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py init tx ' + str(ANTENNA_PORT) + ' 4294967295 0'
print(cmd)
os.system(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py start tx ' + str(ANTENNA_PORT)
print(cmd)
os.system(cmd)

cmd = 'python3 /home/root/l1t-lite/vspa-if-ls'+str(DCS) + '.py start tx ' + str(ANTENNA_PORT)
print(cmd)
os.system(cmd)


