Web VPython 3.2

scene.background = color.white
scene.align = 'left'

ourbox = box(size=vec(5, 5, 5), color=color.black, opacity=0.2)

mass = 2.6567e-26
rad = 0.05
V = 125
n = 30
T = 30
R = 0.0821
particlemax = 500
len = 5
collisions = 0
oldlen = 5

################################################################################

running = True
choosing = True
tchanged = False
nchanged = False
vchanged = False

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
        print_options(delete=True)
    else: 
        b.text = "Run"
        if choosing = True:
            choices.disabled = False
    
button(text = "Pause", pos = scene.title_anchor, bind = Run)

def bindtemp(evt):
    global T, tchanged
    T=evt.value
    tchanged = True
    
def bindpart(evt):
    global n, atomlist, nchanged
    n=evt.value
    for i in range(0, n):
        atomlist[i].visible = True
    for i in range(n, particlemax):
        atomlist[i].visible = False
    nchanged = True

def bindvol(evt):
    global len, V, particlemax, vchanged, atomlist, oldlen
    len = evt.value
    ourbox.size = vec(len, len, len)
    V = (len)**3
    vchanged = True
    for i in range(0, particlemax):
        atomlist[i].pos.x = atomlist[i].pos.x * len / oldlen
        atomlist[i].pos.y = atomlist[i].pos.y * len / oldlen
        atomlist[i].pos.z = atomlist[i].pos.z * len / oldlen
    oldlen = len

tempslider = slider(bind=bindtemp, min=0, max=100, value = T)
tempslider_caption = wtext(text="Temperature\n")
partslider = slider(bind=bindpart, min=1, max=particlemax, value = n, step = 1)
partslider_caption = wtext(text="Num. of particles\n")
volslider = slider(bind=bindvol, min=1, max=10, value = len)
volslider_caption = wtext(text="Volume\n")

tempslider.disabled = True
partslider.disabled = True
volslider.disabled = True

def M(m):
    global tempslider, partslider, volslider, running, tchanged, nchanged, vchanged
    tempslider.disabled = True
    partslider.disabled = True
    volslider.disabled = True
    val = m.selected
    if val == "Temperature": 
        tempslider.disabled = False
        tchanged = True
    elif val == "Number of particles": 
        partslider.disabled = False
        nchanged = True
    elif val == "Volume": 
        volslider.disabled = False
        vchanged = True
    choosing = False
    choices.disabled = True
    print("now you can only change THAT variable")

choices = menu(choices=['Choose a variable', 'Temperature', 'Number of particles', 'Volume'], index=0, bind=M)
choices.disabled = True

wowT = label(pos=vec(0, 0, 0), text="temp: " + T, xoffset=20, yoffset=100, space=30, height=16, border=4, font='sans')
wowN = label(pos=vec(0, 0, 0), text="num: " + n, xoffset=20, yoffset=-50, space=30, height=16, border=4, font='sans')
wowV = label(pos=vec(0, 0, 0), text="vol: " + (V**3), xoffset=-20, yoffset=50, space=30, height=16, border=4, font='sans')

def bordercontrol(i):
    global collisions
    if abs(atomlist[i].pos.x)+rad >= (ourbox.size.x / 2):
        atomlist[i].vel.x = -1 * atomlist[i].vel.x
        collisions += 1
    if abs(atomlist[i].pos.y)+rad >= (ourbox.size.y / 2):
        atomlist[i].vel.y = -1 * atomlist[i].vel.y
        collisions += 1
    if abs(atomlist[i].pos.z)+rad >= (ourbox.size.z / 2):
        atomlist[i].vel.z = -1 * atomlist[i].vel.z
        collisions += 1
        
tvp = graph(title = "Temperature v Pressure", xtitle = "Temperature (K)", ytitle = "Pressure (Pascals)", width = 450, height = 400, align = 'right')
nvp = graph(title = "Number of Particles v Pressure", xtitle = "Number of Moles (mol)", ytitle = "Pressure (Pascals)", width = 450, height = 400, align = 'right')
vvp = graph(title = "Volume v Pressure", xtitle = "Volume (m\u00b3)", ytitle = "Pressure (Pascals)", width = 450, height = 400, align = 'right')

tvpdot = gdots(graph = tvp, color = color.red)
nvpdot = gdots(graph = nvp, color = color.red)
vvpdot = gdots(graph = vvp, color = color.red)
    
tvpdot.plot(0, 0)
nvpdot.plot(0, 0)
vvpdot.plot(0, 0)

################################################################################

atomlist = []
for i in range(0, particlemax):
    atomlist[i] = sphere(pos=vec(0, 0, 0), radius=rad, color=color.cyan)
    atomlist[i].vel = vector.random() * 3
    
for i in range(n, particlemax):
    atomlist[i].visible = False

dt = 0.01
t = 0
oldt = 0
while True:
    rate(1/dt)
    wowT.text = "temp: " + T
    wowN.text = "num: " + n
    wowV.text = "vol: " + V
    if running:
        for i in range(0, n):
            atomlist[i].pos += atomlist[i].vel * dt
            bordercontrol(i)
        if tchanged:
            tvpdot.plot(T, collisions)
            tchanged = False
        elif nchanged:
            nvpdot.plot(n, collisions)
            nchanged = False
        elif vchanged:
            vvpdot.plot(V, collisions)
            vchanged = False
        if t >= oldt + 10 * dt:
            collisions = 0
            oldt = t
        t += dt
    else:
        for i in range(0, n):
            atomlist[i].visible = True
    
            
