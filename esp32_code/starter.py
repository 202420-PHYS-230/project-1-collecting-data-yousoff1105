import board # information about the physical microcontroller
import analogio as aio # analog input and output library
import time # standard python time library

ADCMAX = 2**16-1 # maximum input/out from ADC or to DAC

adc1 = aio.AnalogIn(board.IO15)  # to read voltage from pin 15
adc2 = aio.AnalogIn(board.IO10)  # to read voltage from pin 10
vfactor = adc1.reference_voltage/ADCMAX # get conversion factor voltage to pin

vdac = aio.AnalogOut(board.IO17) # to control voltage on pin 17

f = open('starter.csv','w')
header = "j,vdac,v1,v2,time"


vdac.value = 0 # set output voltage to zero
print("sleeping.... let C fully discharge")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("0 --- go!")

f.write(header + "\n")
print(header)

t0 = time.monotonic_ns()

for i in range(0,255,5): # steps of 5 to save time
    time.sleep(0.4) # let the cap charge....
    t = time.monotonic_ns()-t0
    vout = int((i/255)*ADCMAX)
    vdac.value = vout
    sval = f"{i},{vout*vfactor},{adc1.value*vfactor},{adc2.value*vfactor},{t/1e9}"
    f.write(f"{sval}\n")
    print(sval)

vdac.value = 0 # let the LED rest...
f.close()

