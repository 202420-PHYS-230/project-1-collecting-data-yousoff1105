import analogio as aio
import digitalio as dio
import board
import time

ADCMAX = 2**16-1

adc1 = aio.AnalogIn(board.IO13) # analog ports
adc2 = aio.AnalogIn(board.IO15)
adc3 = aio.AnalogIn(board.IO10)
vfactor = adc1.reference_voltage/ADCMAX

dout = dio.DigitalInOut(board.IO17) # digital output
dout.direction = dio.Direction.OUTPUT

f = open('decay.csv','w')
header = "j,v1,v2,v3,time"

data = []

dout.value = 1
print("sleeping.... let C fully charge")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("0 --- go!")

t0 = time.monotonic_ns()
dout.value = 0

for i in range(0,0xff,0x2): # measure quickly!
    time.sleep(0.001)
    data.append((i,adc1.value, adc2.value, adc3.value, time.monotonic_ns()-t0))

f.write(header + "\n")
print(header)

for i in range(len(data)):
    j,v1,v2,v3,t = data[i]
    sval = f"{j},{v1*vfactor},{v2*vfactor},{v3*vfactor},{t/1e9}"
    f.write(f"{sval}\n")
    print(sval)
    
f.close()

