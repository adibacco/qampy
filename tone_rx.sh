# first arg is file with td waveform, second is antenna port

WAVEFORM=$1
TARGET_ADDR_DDR=0x2380000000
VSPA_BUFFER_ADDR=0x40000000
RX_ANTENNA_PORT=0
DCS=0

if [[ $2 != 0 ]]; then
	DCS=$2
fi

if [[ $3 != 0 ]]; then
	RX_ANTENNA_PORT=$3
fi


echo "DDR target " $TARGET_ADDR_DDR
echo "VSPA Buffer "  $VSPA_BUFFER_ADDR
echo "Antenna port " $RX_ANTENNA_PORT

python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py cfg buff rx 0 0x41040000 16384 262144 $RX_ANTENNA_PORT
python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py cfg patt rx 0 0 0 1 0 0.0 $RX_ANTENNA_PORT

python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py init rx $RX_ANTENNA_PORT 4294967295 0
python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py start rx  $RX_ANTENNA_PORT

python3 /home/root/l1t-lite/vspa-if-ls${DCS}.py stop rx $RX_ANTENNA_PORT
/home/root/l1t-lite//bin2mem -f $1 -a 0x2381040000 -c 4 -r 262144

