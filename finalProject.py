Web VPython 3.2

scene = canvas(background=color.white)

temperature = input("Give me your temperature") 

# the average speed is sqrt(3kT/m), given by the equation that we will be using , where T is the temperature in Kelvin, k is the Boltzmann constant, and m is the mass in kg)
# velocities can be approximated using the normal distribution, but not the speed itself
# use np.random.normal 
# loc is the mean

# boltzman constant: 1.380649 × 10-23 m2 kg s-2 K-1

# bruh I can't even import 

#example = np.random.normal(T)
#print(example)

# standard deviation = sqrt(kT/m)

mass = 2.6567e-26
kb = 1.380649e-23
avgSpeed = 3 * kb * temperature / mass

def randSpeed(temperature):
    parity = 0
    if random() > 0.5:
        parity = 1
    else:
        parity = -1
    return 

mass = 2.6567e-26
rad = 6.6e-11
V = (rad*10)**3
n = 5
R = 0.0821

box(vol=V, size=vec(5,5,5), color=color.black, opacity=0.4)

go = True

alderaans = []
for i in range(n-1):
    alderaans.append(sphere(m=mass, pos=vec((1.5*i)-2,1,0), texture=textures.earth, radius=0.2))
    #alderaans.velocity = 

deathStar = sphere(m=mass, pos=vec(2,-2,0), texture="https://i.imgur.com/S9WXwf2.png", radius=0.2)

g = graph()
k = gdots(graph = g)
    
def random_speed_from_temperature(T):
    v_peak = sqrt(T)
    f_max = (v_peak ** 2) * exp(-v_peak**2 / (2 * T))

    while True:
        v = 5 * sqrt(T) * random()
        f_v = (v ** 2) * exp(-v**2 / (2 * T))
        u = f_max * random()
        if u < f_v:
            return v

temperature = 300
for i in range(30):
    v_sample = random_speed_from_temperature(temperature)
    print(f"Random particle speed: {v_sample:.2f}")
