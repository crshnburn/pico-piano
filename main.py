import machine

C = 262
D = 294
E = 330
F = 349
G = 392
A = 440
B = 494
C1 = 525

C_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
D_button = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)
E_button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
F_button = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
G_button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
A_button = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)
B_button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)
C1_button = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)
Buzzer = machine.PWM(machine.Pin(15))


while True:
    while C_button.value():
        Buzzer.duty_u16(32767)
        Buzzer.freq(C)
    while D_button.value():
        Buzzer.duty_u16(32767)
        Buzzer.freq(D)
    while E_button.value():
        Buzzer.duty_u16(32767)
        Buzzer.freq(E)
    while F_button.value():
        Buzzer.duty_u16(32767)
        Buzzer.freq(F)
    while G_button.value():
        Buzzer.duty_u16(32767)
        Buzzer.freq(G)
    while A_button.value():
        Buzzer.duty_u16(32767)
        Buzzer.freq(A)
    while B_button.value():
        Buzzer.duty_u16(32767)
        Buzzer.freq(B)
    while C1_button.value():
        Buzzer.duty_u16(32767)
        Buzzer.freq(C1)
    Buzzer.duty_u16(0)        
