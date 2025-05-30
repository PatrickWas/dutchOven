Web VPython 3.2

mass = 2.6567e-26
rad = 6.6e-11
V = (rad*10)**3
n = 5
T = 30
R = 0.0821

box(vol=V, size=vec(5,5,5), color=color.black, opacity=0.4)

go = True

alderaans = []
for i in range(n-1):
    alderaans.append(sphere(m=mass, pos=vec((1.5*i)-2,1,0), texture=textures.earth))

deathStar = sphere(m=mass, pos=vec(2,-2,0), texture="https://i.imgur.com/S9WXwf2.png")

tempslider = slider(bind=bindtemp, min=0, max=100, value = T)
tempslider_caption = wtext(text="Temperature\n")
partslider = slider(bind=bindpart, min=1, max=100, value = n)
partslider_caption = wtext(text="Num. of particles\n")
volslider = slider(bind=bindvol, value = V)
volslider_caption = wtext(text="Volume\n")

def bindtemp(evt):
    global T
    T=evt.value
    
def bindpart(evt):
    global n
    n=evt.value

def bindvol(evt):
    global V
    V=evt.value

t = 0
dt = 0.01
wowT = label(pos=vec(0, 0, 0), text="temp: " + T, xoffset=20, yoffset=100, space=30, height=16, border=4, font='sans')
wowN = label(pos=vec(0, 0, 0), text="num: " + n, xoffset=20, yoffset=-50, space=30, height=16, border=4, font='sans')
wowV = label(pos=vec(0, 0, 0), text="vol: " + V, xoffset=-20, yoffset=50, space=30, height=16, border=4, font='sans')
while True:
    rate(1/dt)
    wowT.text = "temp: " + T
    wowN.text = "num: " + n
    wowV.text = "vol: " + V
    if go:
        for i in range(len(alderaans)):
            alderaans[i].pos += vec(i, 0, 0)
            deathStar.pos += vec(0.5, 0.5, 0.5)
        t += dt
