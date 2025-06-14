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



scene.background = color.white
scene.align = 'left'


mass = 2.6567e-26
rad = 6.6e-11
V = (rad*100)**3
A = (rad*100)**2
n = 50
T = 30
R = 8.314 # for cubic meters and pascals, not the 0.0821 used for liters and atmospheres
particlemax = 250

times = 0

visualRad = 0.05
adjust = (visualRad + visualRad/sqrt(2)) / 2

fullSide = visualRad*100
side = fullSide/2
box(size=vec(fullSide+2*adjust,fullSide+2*adjust,fullSide+2*adjust), color=color.black, opacity=0.2)


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
        choices.selected = "Choose a variable"
        print_options(delete=True)
    else: 
        b.text = "Run"
        if choosing = True:
            choices.disabled = False
    
button(text = "Pause", pos = scene.title_anchor, bind = Run)

def bindtemp(evt):
    global T, alderaans, P, t, times
    times += 1
    tvpdot.plot(T, (proportion**2)*P/A/t/(rad*100))
    pressuredot.plot(times, (proportion**2)*P/A/t/(rad*100) / (n/6.02e23*R*(T+273)/V))
    P = 0
    t = 0
    T=evt.value
    tchanged = True
    for i in range(0, particlemax):
        alderaans[i].vel = vec(vel_from_temp(T+273), vel_from_temp(T+273), vel_from_temp(T+273))
    
def bindpart(evt):
    global n, alderaans, P, t, times
    times += 1
    nvpdot.plot(n, (proportion**2)*P/A/t/(rad*100))
    pressuredot.plot(times, (proportion**2)*P/A/t/(rad*100) / (n/6.02e23*R*(T+273)/V))
    P = 0
    t = 0
    n=evt.value
    for i in range(0, n):
        alderaans[i].visible = True
    for i in range(n, particlemax):
        alderaans[i].visible = False

tempslider = slider(bind=bindtemp, min=-150, max=150, value = T)
tempslider_caption = wtext(text="Temperature\n")
partslider = slider(bind=bindpart, min=1, max=particlemax, value = n, step = 1)
partslider_caption = wtext(text="Num. of particles\n")

tempslider.disabled = True
partslider.disabled = True

def M(m):
    global tempslider, partslider, running
    tempslider.disabled = True
    partslider.disabled = True
    val = m.selected
    if val == "Temperature": 
        tempslider.disabled = False
    elif val == "Number of particles": 
        partslider.disabled = False
    choosing = False
    choices.disabled = True
    
choices = menu(choices=['Choose a variable', 'Temperature', 'Number of particles'], index=0, bind=M)
choices.disabled = True

wowT = label(pos=vec(0, 0, 0), text="temp: " + T, xoffset=20, yoffset=100, space=30, height=16, border=4, font='sans')
wowN = label(pos=vec(0, 0, 0), text="num: " + n, xoffset=20, yoffset=-50, space=30, height=16, border=4, font='sans')

###################################################

P = 0
count = 0

''' vel_from_temp gives proportionally accurate answers, but they're approximately that amount too small:
         The correct speed at 30 *C is 500 m/s, which componently is sqrt(290^2+290^2+290^2).
         The function's component speed at 30 *C is ~28 m/s.
'''
proportion = 290/28

###################################################

tvp = graph(title = "Temperature v Pressure", xtitle = "Temperature (C)", ytitle = "Pressure (Pascals)", width = 450, height = 400, align = 'right')
nvp = graph(title = "Number of Particles v Pressure", xtitle = "Number of Moles (mol)", ytitle = "Pressure (Pascals)", width = 450, height = 400, align = 'right')
pressure = graph(title = "nRT/V v Measured Pressure", xtitle = "Number of Changes Made", ytitle = "Measured Pressure divided by nRT/V (hopefully 1)", width = 450, height = 400, align = 'right')

tvpdot = gdots(graph = tvp, color = color.red)
nvpdot = gdots(graph = nvp, color = color.red)
pressuredot = gdots(graph = pressure, color = color.blue)


# RANDOM STUFF USING THE BOLTZMANN DISTRIBUTION
##############################
def vel_from_temp(T):
    v_peak = sqrt(T)
    f_max = (v_peak ** 2) * exp(-v_peak**2 / (2 * T))
    while True:
        v = 5 * sqrt(T) * random()
        f_v = (v ** 2) * exp(-v**2 / (2 * T))
        u = f_max * random()
        if u < f_v:
            if random() < 0.5:
                return v
            return -v
##############################


def randPos():
    return random()*side*2-side

alderaans = []
for i in range(0, particlemax):
    alderaans.append(sphere(vel=vec(vel_from_temp(T+273), vel_from_temp(T+273), vel_from_temp(T+273)), radius=visualRad, pos=vec(randPos(), randPos(), randPos()), color=color.cyan))
    
for i in range(n, particlemax):
    alderaans[i].visible = False



t = 0
dt = 0.0005
while True:
    rate(1/dt/8)
    wowT.text = "temp: " + T
    wowN.text = "num: " + n
    
    if running:
        for i in range(0, n):
            
        
            newPos = alderaans[i].pos + alderaans[i].vel*dt
            if abs(newPos.x) > side or abs(newPos.y) > side or abs(newPos.z) > side:
                count += 1
                frac = 1
                
                
                tempSide = side
                if abs(newPos.x) > side:
                    if newPos.x < 0:
                        tempSide *= -1
                    frac = abs((tempSide - alderaans[i].pos.x) / (newPos.x - alderaans[i].pos.x))
                    alderaans[i].pos += (alderaans[i].vel*dt*frac)
                    acc = 2*abs(alderaans[i].vel.x)
                    alderaans[i].vel.x *= -1
                    
                elif abs(newPos.y) > side:
                    if newPos.y < 0:
                        tempSide *= -1
                    frac = abs((tempSide - alderaans[i].pos.y) / (newPos.y - alderaans[i].pos.y))
                    alderaans[i].pos += (alderaans[i].vel*dt*frac)
                    acc = 2*abs(alderaans[i].vel.y)
                    alderaans[i].vel.y *= -1
                
                else:
                    if newPos.z < 0:
                        tempSide *= -1
                    frac = abs((tempSide - alderaans[i].pos.z) / (newPos.z - alderaans[i].pos.z))
                    alderaans[i].pos += (alderaans[i].vel*dt*frac)
                    acc = 2*abs(alderaans[i].vel.z)
                    alderaans[i].vel.z *= -1
            
                P += (mass*acc)
                alderaans[i].pos += (alderaans[i].vel*dt*(1-frac))
        
            else:
                alderaans[i].pos += (alderaans[i].vel*dt)
        
        t += dt
