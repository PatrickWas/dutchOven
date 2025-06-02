Web VPython 3.2

running = True

def Run(b):
    global running
    running = not running
    if running: 
        b.text = "Pause"
        choices.disabled = True
        tempslider.disabled = True
        partslider.disabled = True
        volslider.disabled = True
        choices.selected = "Choose a variable"
    else: 
        b.text = "Run"
        choices.disabled = False
    
button(text = "Pause", pos = scene.title_anchor, bind = Run)

mass = 2.6567e-26
rad = 6.6e-11
V = (rad*10)**3
n = 5
T = 30
R = 0.0821

def bindtemp(evt):
    global T
    T=evt.value
    
def bindpart(evt):
    global n
    n=evt.value

def bindvol(evt):
    global V
    V=evt.value

tempslider = slider(bind=bindtemp, min=0, max=100, value = T)
tempslider_caption = wtext(text="Temperature\n")
partslider = slider(bind=bindpart, min=1, max=100, value = n)
partslider_caption = wtext(text="Num. of particles\n")
volslider = slider(bind=bindvol, value = V)
volslider_caption = wtext(text="Volume\n")

tempslider.disabled = True
partslider.disabled = True
volslider.disabled = True

def M(m):
    global tempslider, partslider, volslider, running
    tempslider.disabled = True
    partslider.disabled = True
    volslider.disabled = True
    val = m.selected
    if val == "Temperature": 
        tempslider.disabled = False
    elif val == "Number of particles": 
        partslider.disabled = False
    elif val == "Volume": 
        volslider.disabled = False

choices = menu(choices=['Choose a variable', 'Temperature', 'Number of particles', 'Volume'], index=0, bind=M)
choices.disabled = True

wowT = label(pos=vec(0, 0, 0), text="temp: " + T, xoffset=20, yoffset=100, space=30, height=16, border=4, font='sans')
wowN = label(pos=vec(0, 0, 0), text="num: " + n, xoffset=20, yoffset=-50, space=30, height=16, border=4, font='sans')
wowV = label(pos=vec(0, 0, 0), text="vol: " + V, xoffset=-20, yoffset=50, space=30, height=16, border=4, font='sans')

dt = 0.01
while True:
    rate(1/dt)
    wowT.text = "temp: " + T
    wowN.text = "num: " + n
    wowV.text = "vol: " + V
    if running:
