Web VPython 3.2

scene.background=vec(0.5,0.8,0.1)


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


button(bind = something, text="Start time\n")
slide1 = slider(bind=something)
slide1_caption = wtext(text="Temperature\n")
slide2 = slider(bind=something)
slide2_caption = wtext(text="Num. of particles\n")
slide3 = slider(bind=something)
slide3_caption = wtext(text="Volume\n")

def something(b):
    return

t = 0
dt = 10
while True:
    rate(1/dt)
    
    if go:
        for i in range(len(alderaans)):
            alderaans[i].pos += vec(i, 0, 0)
            deathStar.pos += vec(0.5, 0.5, 0.5)
        t += dt

