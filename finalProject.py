Web VPython 3.2

#############################
# README

# Welcome to the ideal gas law project! 
# This project models the relationship between number of particles and the average temperature of the particles with 
# pressure. 

# (INITIAL RUN) Upon running the program, the simulation will automatically start. One might notice 
# that all the sliders and buttons are grayed out. This is because the user is restricted
# from changing any of the variables of temperature or number of particles while the 
# simulation is running. 

# (SLIDER/BUTTON) By pressing the button labeled "Pause," the option to select a variable is unlocked. 
# Clearly, only one variable can be changed at a time. One that variable is selected, all the others 
# will remain grayed out while the chosen variable slider can be interacted with. 

# (PARTICLE SPEEDS) Particles are given velocities corresponding to their average temperature using the 
# Boltzmann distribution. This means that some particles move at a lower velocity than others, but 
# their mean velocity is where you'd expect it to be. 

# (GRAPHS) Once a variable is selected, only that graph will be drawn on. It will show the relationship between pressure 
# and whatever variable is chosen. 
#############################

scene.background=vec(1,1,1)

ourbox = box(size=vec(5, 5, 5), color=color.black, opacity=0.2)

mass = 2.6567e-26
rad = 0.05
V = (5)**3
n = 80
T = 300
R = 0.0821
particlemax = 500
len = 5

#############################

running = True
choosing = True

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
    global T
    T=evt.value
    
def bindpart(evt):
    global n, atomlist
    n=evt.value
    for i in range(0, n):
        atomlist[i].visible = True
    for i in range(n, particlemax):
        atomlist[i].visible = False

def bindvol(evt):
    global len, V, particlemax
    len = evt.value
    ourbox.size = vec(len, len, len)
    V = (len)**3

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
    choosing = False
    choices.disabled = True
    print("now you can only change THAT variable")

choices = menu(choices=['Choose a variable', 'Temperature', 'Number of particles', 'Volume'], index=0, bind=M)
choices.disabled = True

wowT = label(pos=vec(0, 0, 0), text="temp: " + T, xoffset=20, yoffset=100, space=30, height=16, border=4, font='sans')
wowN = label(pos=vec(0, 0, 0), text="num: " + n, xoffset=20, yoffset=-50, space=30, height=16, border=4, font='sans')
wowV = label(pos=vec(0, 0, 0), text="vol: " + V, xoffset=-20, yoffset=50, space=30, height=16, border=4, font='sans')

def bordercontrol(i):
    if abs(atomlist[i].pos.x)+rad >= (ourbox.size.x / 2):
        atomlist[i].vel.x = -1 * atomlist[i].vel.x
    if abs(atomlist[i].pos.y)+rad >= (ourbox.size.y / 2):
        atomlist[i].vel.y = -1 * atomlist[i].vel.y
    if abs(atomlist[i].pos.z)+rad >= (ourbox.size.z / 2):
        atomlist[i].vel.z = -1 * atomlist[i].vel.z
    
# RANDOM STUFF USING THE BOLTZMANN DISTRIBUTION
# this is called rejection samping, make sure to talk about that in the README
##############################
def random_speed_from_temperature(T):
    v_peak = sqrt(T) * 30
    f_max = (v_peak ** 2) * exp(-v_peak**2 / (2 * T))
    while True:
        v = 5 * sqrt(T) * random()
        f_v = (v ** 2) * exp(-v**2 / (2 * T))
        u = f_max * random()
        if u < f_v:
            return v
##############################

atomlist = []
x_average = 0
y_average = 0
z_average = 0
for i in range(0, particlemax):
    atomlist[i] = sphere(pos=vec(0, 0, 0), radius=rad, color=color.cyan)
    x_vel = random_speed_from_temperature(T)
    x_average += x_vel
    print("x_vel is: " + x_vel)
    y_vel = random_speed_from_temperature(T)
    y_average += y_vel
    print("y vel is: " + y_vel)
    z_vel = random_speed_from_temperature(T)
    z_average += z_vel
    print("z vel is: " + z_vel)
    atomlist[i].vel = vec(x_vel,y_vel,z_vel)

x_average /= 500
y_average /= 500
z_average /= 500

print(x_average)
print(y_average)
print(z_average)

    
for i in range(n, particlemax):
    atomlist[i].visible = False

dt = 0.001
while True:
    rate(100)
    wowT.text = "temp: " + T
    wowN.text = "num: " + n
    wowV.text = "vol: " + V
    if running:
        for i in range(0, particlemax):
            atomlist[i].pos += atomlist[i].vel * dt
            bordercontrol(i)
    else:
        for i in range(0, n):
            atomlist[i].visible = True
        for i in range(0, particlemax):
            atomlist[i].pos.x = 0
            atomlist[i].pos.y = 0
            atomlist[i].pos.z = 0
            
