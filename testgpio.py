from gpiozero import LED
from time import sleep
#02 SDA P3
#03 SCL p5
#04 IO4 p7
#14 TXD p8
#15 RXD p10
#17 IO17 p11
#18 IO18 p12
#27 IO27 p13
#22 IO22 p15
#23 IO23 p16
#24 IO24 p18
#10 MOSI p19
#09 MSIO p21
#25 IO25 p22
#11 SCLK p23
#08 CE0/IO8 p24
#07 CE1/IO7 p26
#01 IDSC p28
#05 IO5 p29
#06 IO6 p31
#12 IO12 p32
#13 IO13 p33 xxx
#19 IO19 p35
#16 IO16 p36
#26 IO26 p37
#20 IO20 p38
#21 IO21 p40

led01 = LED(7)
led02 = LED(8)
led03 = LED(11)
led04 = LED(9)
led05 = LED(10)
led06 = LED(18)
led07 = LED(17)
led08 = LED(16)
led09 = LED(6)
led10 = LED(5)
led11 = LED(25)
led12 = LED(24)
led13 = LED(15)
led14 = LED(14)
led15 = LED(19)
led16 = LED(20)
led17 = LED(12)
led18 = LED(1)
led19 = LED(22)
led20 = LED(23)
led21 = LED(26)
led22 = LED(13)
led23 = LED(21)
led24 = LED(27)
led25 = LED(4)
led26 = LED(3)
led27 = LED(2)

interval = 0.02

while True:
    led01.toggle()
    sleep(interval)
    led02.toggle()
    sleep(interval)
    led03.toggle()
    sleep(interval)
    led04.toggle()
    sleep(interval)
    led05.toggle()
    sleep(interval)
    led06.toggle()
    sleep(interval)
    led07.toggle()
    sleep(interval)
    led08.toggle()
    sleep(interval)
    led09.toggle()
    sleep(interval)
    led10.toggle()
    sleep(interval)
    led11.toggle()
    sleep(interval)
    led12.toggle()
    sleep(interval)
    led13.toggle()
    sleep(interval)
    led14.toggle()
    sleep(interval)
    led15.toggle()
    sleep(interval)
    led16.toggle()
    sleep(interval)
    led17.toggle()
    sleep(interval)
    led18.toggle()
    sleep(interval)
    led19.toggle()
    sleep(interval)
    led20.toggle()
    sleep(interval)
    led21.toggle()
    sleep(interval)
    led22.toggle()
    sleep(interval)
    led23.toggle()
    sleep(interval)
    led24.toggle()
    sleep(interval)
    led25.toggle()
    sleep(interval)
    led26.toggle()
    sleep(interval)
    led27.toggle()
    sleep(interval)
    