
import random

num = input ("Select Level (1-5):")
wallB = box(pos=vector(0,-10,0), size=vector(20,0.2,20), color=color.green)

if num=="1":
  ball = sphere(pos=vector(-10,-9.3,10), radius=0.5, color=color.magenta,  make_trail=True)
  
  target = ring(pos=vector(6, -9.8, -6), radius=3, color=color.red, axis=vector(0,1,0), thickness=0.2)
  box1 = box(pos=vector(5,-9.3,1),
              axis=vector(0,0,0), length=5,
              height=6, width=10, up=vector(0, 1, 0))
              
  box2 = box(pos=vector(-2,-11.3,4),
              axis=vector(0,0,0), length=3,
              height=8, width=5, up=vector(0, 1, 0))
else if num=="2":
  ball = sphere(pos=vector(0,-9.3,10), radius=0.5, color=color.magenta,  make_trail=True)
  
  target = ring(pos=vector(6, -9.8, -6), radius=3.2, color=color.red, axis=vector(0,1,0), thickness=0.2)
  box1 = box(pos=vector(5,-6.3,1),
              axis=vector(0,0,0), length=5,
              height=3, width=4, up=vector(0,1, 0))
              
  box2 = box(pos=vector(-2,-11.3,4),
              axis=vector(0,0,0), length=3,
              height=8, width=5, up=vector(0, 1, 0))    
else if num=="3":
  ball = sphere(pos=vector(-10,-9.3,10), radius=0.5, color=color.magenta,  make_trail=True)
  
  target = ring(pos=vector(3, -3.8, -3), radius=5, color=color.red, axis=vector(0,1,0), thickness=0.2)
  box1 = box(pos=vector(5,-5.3,1),
              axis=vector(0,0,0), length=5,
              height=9, width=5, up=vector(0, 1, 0))
              
  box2 = box(pos=vector(-2,-11.3,4),
              axis=vector(0,0,0), length=3,
              height=8, width=5, up=vector(0, 1, 0))            
else if num=="4":
  ball = sphere(pos=vector(-10,-9.3,10), radius=0.5, color=color.magenta,  make_trail=True)
  
  target = ring(pos=vector(3, -2.8, -3), radius=7, color=color.red, axis=vector(0,1,0), thickness=0.2)
  box1 = box(pos=vector(5,-5.3,1),
              axis=vector(0,0,0), length=5,
              height=9, width=5, up=vector(0, 1, 0))
              
  box2 = box(pos=vector(-2,-11.3,4),
              axis=vector(0,0,0), length=3,
              height=8, width=5, up=vector(0, 1, 0))         
else if num=="5":
  ball = sphere(pos=vector(0,-9.3,10), radius=0.5, color=color.magenta,  make_trail=True)
  
  target = ring(pos=vector(5, -9.8, 4.8), radius=3.2, color=color.red, axis=vector(0,1,0), thickness=0.2)
  box1 = box(pos=vector(5,-6.3,1),
              axis=vector(0,0,0), length=5,
              height=3, width=4, up=vector(0,1, 0))
              
  box2 = box(pos=vector(3,-11.3,7),
              axis=vector(0,0,0), length=3,
              height=8, width=5, up=vector(0, 1, 0))                 
else:
  ball = sphere(pos=vector(3,-9.3,10), radius=0.5, color=color.magenta,  make_trail=True)
  
  target = ring(pos=vector(-8.9, -9.5, 4.8), radius=6, color=color.red, axis=vector(0,1,0), thickness=1.2)
  box1 = box(pos=vector(8,-9.3,2),
              axis=vector(0,0,0), length=5,
              height=5, width=5, up=vector(0,1, 0))
              
  box2 = box(pos=vector(3,-11.3,7),
              axis=vector(0,0,0), length=0,
              height=0, width=0, up=vector(1, 5, 1))                               
              
'''  
ball = sphere(pos=vector(-10,-9.3,10), radius=0.5, color=color.magenta,  make_trail=True)

target = ring(pos=vector(random.uniform(-10, 10), random.uniform(-9.3, -5.3), random.uniform(-10, 10)), radius=random.uniform(1, 4.8), color=color.red, axis=vector(0,1,0), thickness=0.2)
box1 = box(pos=vector(random.uniform(0, 9),-9.3,random.uniform(-9, 0)),
            axis=vector(0,0,0), length=random.uniform(1, 5),
            height=random.uniform(1, 6), width=random.uniform(1, 7), up=vector(random.randint(-3, 3),random.randint(-3, 3),random.randint(-3, 3)))
            
box2 = box(pos=vector(random.uniform(0, 9),-9.3,random.uniform(-9, 0)),
            axis=vector(0,0,0), length=random.uniform(1, 9),
            height=random.uniform(1, 9), width=random.uniform(1, 9), up=vector(random.randint(-3, 3),random.randint(-3, 3),random.randint(-3, 3)))
                        
'''
v = vector(0,0,0)

#mass
ballMass=1
initialVelocity=10

#downwards force of gravity
g=vector(0,-9.81,0)
Fnet=ballMass*g

waiting = True

varr = arrow(shaftwidth=0.85,pos=ball.pos, axis=v, color=color.cyan)

while waiting:
    rate(10)
    k = keysdown() # a list of keys that are down
    if 'left' in k: v.x-=0.1
    if 'right' in k: v.x+=0.1
    if 'down' in k: v.z+=0.1
    if 'up' in k: v.z-=0.1
    if 'w' in k: v.y+=0.1
    if 's' in k: v.y-=0.1
    if 'm' in k: waiting=False
    
    ballMomentum=ballMass*v*2.6
    varr.axis=v

#momentum of the ball

t=0
fps = 60
timePerFrame=(1/fps)

firstTime = True

while ball.pos.x<=12 and ball.pos.x>= -12 and ball.pos.z<=12 and ball.pos.z>=-12:
  rate(fps)
  if firstTime and ball.pos.y >= target.pos.y and ball.pos.y <= target.pos.y+target.thickness+(0.5*ball.radius) and ball.pos.x <= target.pos.x+target.radius and ball.pos.x >= target.pos.x-target.radius and ball.pos.z <= target.pos.z+target.radius and ball.pos.z >= target.pos.z-target.radius:
    print("You won")
    firstTime = False
    #ball.pos.y=-9.3 #remove duplicate outputs in range
  #https://vpython.org/contents/bounce_example.html  
  if ball.pos.y < wallB.pos.y+(0.5*wallB.size.y):
    ballMomentum.y = abs(ballMomentum.y)
    
  if ball.pos.x <= target.pos.x+target.radius and ball.pos.x >= target.pos.x+target.radius-target.thickness:
    print("1")
    if ball.pos.z <= target.pos.z+target.radius and ball.pos.z >= target.pos.z-target.radius-target.thickness:
      print("2")
      if ball.pos.y <= target.pos.y+(0.5*target.thickness) and ball.pos.y >= target.pos.y-(0.5*target.thickness):
        print("3")
        if ball.pos.x <= target.pos.x+target.radius and ball.pos.x >= target.pos.x+target.radius-target.thickness:
          ballMomentum.x = -1*(ballMomentum.x)
        if ball.pos.x <= target.pos.x+target.radius and ball.pos.x >= target.pos.x+target.radius-target.thickness:
          ballMomentum.z = -1*(ballMomentum.z)
        
  if ball.pos.x <= box1.pos.x+(box1.length/2) and ball.pos.x >= box1.pos.x-(box1.length/2):
    print("1")
    if ball.pos.z <= box1.pos.z+(box1.width/2) and ball.pos.z >= box1.pos.z-(box1.width/2):
      print("2")
      if ball.pos.y <= box1.pos.y+(box1.height/2) and ball.pos.y >= box1.pos.y-(box1.height/2):
        print("3")
        if ball.pos.x <= box1.pos.x+(box1.length/2)-0.1 and ball.pos.x >= box1.pos.x-(box1.length/2)+0.1:
          #ballMomentum.x = abs(ballMomentum.x)
          ballMomentum.z = -1*(ballMomentum.z)  
          ballMomentum.y = -1*(ballMomentum.y) 
          print("x")
        
        if ball.pos.z <= box1.pos.z+(box1.width/2)-0.1 and ball.pos.z >= box1.pos.z-(box1.width/2)+0.1:
          ballMomentum.x = -1*(ballMomentum.x)
          #ballMomentum.z = -1*(ballMomentum.z)  
          ballMomentum.y = -1*(ballMomentum.y) 
          print("z")
          
        if ball.pos.y <= box1.pos.y+(box1.height/2)+0.1 and ball.pos.y >= box1.pos.y-(box1.height/2)-0.1:
          #ballMomentum.x = -1*(ballMomentum.x)
          #ballMomentum.z = -1*(ballMomentum.z)  
          ballMomentum.y = -1*(ballMomentum.y) 
          print("y")
        
  if ball.pos.x <= box2.pos.x+(box2.length/2) and ball.pos.x >= box2.pos.x-(box2.length/2):
      print("1")
      if ball.pos.z <= box2.pos.z+(box2.width/2) and ball.pos.z >= box2.pos.z-(box2.width/2):
        print("2")
        if ball.pos.y <= box2.pos.y+(box2.height/2) and ball.pos.y >= box2.pos.y-(box2.height/2):
          print("3")
          if ball.pos.x <= box2.pos.x+(box2.length/2)-0.1 and ball.pos.x >= box2.pos.x-(box2.length/2)+0.1:
            #ballMomentum.x = abs(ballMomentum.x)
            ballMomentum.z = -1*(ballMomentum.z)  
            ballMomentum.y = -1*(ballMomentum.y) 
            print("x")
          
          if ball.pos.z <= box2.pos.z+(box2.width/2)-0.1 and ball.pos.z >= box2.pos.z-(box2.width/2)+0.1:
            ballMomentum.x = -1*(ballMomentum.x)
            #ballMomentum.z = -1*(ballMomentum.z)  
            ballMomentum.y = -1*(ballMomentum.y) 
            print("z")
            
          if ball.pos.y <= box2.pos.y+(box2.height/2)+0.1 and ball.pos.y >= box2.pos.y-(box2.height/2)-0.1:
            #ballMomentum.x = -1*(ballMomentum.x)
            #ballMomentum.z = -1*(ballMomentum.z)  
            ballMomentum.y = -1*(ballMomentum.y) 
            print("y")        
        
  #if ball.pos.x>=box1.pos.x*mag(box1.axis)-mag(box1.up)*0.5*box1.length:
  #    print("test")
  #if ball.pos.y >= box1.pos.y and ball.pos.y <= box1.pos.y+box1.height and ball.pos.x <= box1.pos.x+box1.length and ball.pos.x >= box1.pos.x-target.length and ball.pos.z <= box1.pos.z+box1.width and ball.pos.z >= box1.pos.z-box1.radius:
  #  print("You hit an obstacle")
  #if ball.pos.y >= box2.pos.y and ball.pos.y <= box2.pos.y+box2.height and ball.pos.x <= box2.pos.x+box2.length and ball.pos.x >= box2.pos.x-target.length and ball.pos.z <= box2.pos.z+box2.width and ball.pos.z >= box2.pos.z-box2.radius:
  #  print("You hit an obstacle")    
    
  #https://www.youtube.com/watch?v=F564RU3k528&ab_channel=PhysicsExplained  
  ballMomentum = ballMomentum + Fnet * timePerFrame
  ball.pos += (ballMomentum*timePerFrame)/ballMass

  t=t+timePerFrame
