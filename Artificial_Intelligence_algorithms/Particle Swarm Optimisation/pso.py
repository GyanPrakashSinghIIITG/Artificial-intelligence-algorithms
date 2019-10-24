from numpy import *
from random import random
from math import *

iter_max = 10000
pop_size = 100
dimensions = 2
c1 = 2
c2 = 2
err_crit = 0.00001

class Particle:
    pass
        

def f6(param):
    para = param*10
    para = param[0:2]
    num = (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) * \
        (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) - 0.5
    denom = (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1]))) * \
            (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1])))
    f6 =  0.5 - (num/denom)
    errorf6 = 1 - f6
    return f6, errorf6;
 
particles = []   #initialize the particles
for i in range(pop_size):
    p = Particle()
    p.params = array([random() for i in range(dimensions)])
    p.fitness = 0.0
    p.v = 0.0
    particles.append(p)

gbest = particles[0]  #first particle is the global best initially
err = 999999999
while i < iter_max :
    for p in particles:
        fitness,err = f6(p.params)
        if fitness > p.fitness:
            p.fitness = fitness
            p.best = p.params

        if fitness > gbest.fitness:
            gbest = p
        v = p.v + c1 * random() * (p.best - p.params) \
                + c2 * random() * (gbest.params - p.params)
        p.params = p.params + v
          
    i  += 1
    if err < err_crit:
        break
    
print '\nParticle Swarm Optimisation under clustering\n'
print '-------------Parameters----------------\n',
print 'Population size : ', pop_size
print 'c1              : ', c1
print 'c2              : ', c2

print '---------Result-----------\n',
print 'iterations      : ', i+1
print 'gbest params    : ', gbest.params
print 'gbest fitness   : ', gbest.fitness

