# first arg is file with td waveform, second is antenna port

WAVEFORM=$1
TARGET_ADDR_DDR=0x2380000000
VSPA_BUFFER_ADDR=0x40000000
ANTENNA_PORT=0

DCS=0

if [[ $2 != 0 ]]; then
	DCS=$2
fi

if [[ $3 != 0 ]]; then
	ANTENNA_PORT=$3
fi



echo "DDR target " $TARGET_ADDR_DDR
echo "VSPA Buffer "  $VSPA_BUFFER_ADDR
echo "Antenna port " $ANTENNA_PORT
echo "DCS " $DCS


/home/root/l1t-lite/bin2mem -f $WAVEFORM -a $TARGET_ADDR_DDR -c 4
python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py cfg buff tx 0 $VSPA_BUFFER_ADDR 15360 122880 $ANTENNA_PORT
#python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py cfg buff tx 0 $VSPA_BUFFER_ADDR 15360 122880 1


python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py cfg patt tx 0 0 0 1 0 1.0 $ANTENNA_PORT
#python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py cfg patt tx 0 0 0 1 0 1.0 1

python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py init tx $ANTENNA_PORT 4294967295 0
#python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py init tx 1 4294967295 0

python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py start tx $ANTENNA_PORT
python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py start tx $ANTENNA_PORT
#python3 /home/root/l1t-lite/vspa-if-ls0.py start tx 1


