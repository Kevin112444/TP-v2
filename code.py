from cmu_112_graphics import *

class MyApp(App):
    
    def appStarted(self):
        self.timerDelay = 1
        self.background = self.loadImage('Assets/Backgrounds/background1.jpg')
        self.xd= 0
        self.age = 0
        self.alive = []
        self.sprites = []
        self.spriteCounters = []

    class Units(object):
        def __init__(self,health,attack,atkspd,range,cost):
            self.health = health
            self.attack = attack
            self.atkspd = atkspd
            self.range = range
            self.cost = cost
            self.state = 'walk'
            self.spriteCounter = 0
        
        def __eq__(self, other):
            return (isinstance(other, A) and (self.x == other.x))

        
    class Bat(Units):
        spritesheet = 'Assets/Sprites/Age1/Bat.png'
        def __init__(self):
            super().__init__(10,1,1,0,10)
            
        def action(self):
            if self.state == 'walk':
                return (0,4)
            elif self.state == 'fight':
                return (30,42)

    class Owl(Units):
        spritesheet = 'Assets/Sprites/Age1/Owl.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,9)
            elif self.state == 'fight':
                return (9,18)
            
                
    class Peacock(Units):
        spritesheet = 'Assets/Sprites/Age1/Peacock.png'
        def __init__(self):
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (9,18)
                
    class Rat(Units):
        spritesheet = 'Assets/Sprites/Age1/Rat.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)

    def keyPressed(self,event):
        if event.key == "1":
            newBat = 'bat' + str(len(self.sprites))
            newBat = self.Bat()
            self.alive.append(newBat)
            self.spriteCounters.append(0)
            self.Animate()
        elif event.key == "2":
            newOwl = 'owl' + str(len(self.sprites))
            newOwl = self.Owl()
            self.alive.append(newOwl)
            self.spriteCounters.append(0)
            self.Animate()
        elif event.key == "3":
            newPeacock = 'peacock' + str(len(self.sprites))
            newPeacock = self.Peacock()
            self.alive.append(newPeacock)
            self.spriteCounters.append(0)
            self.Animate()
            
            
    def Animate(self):
        for count in range(len(self.alive)):
            unit = self.alive[count]
            pic = self.loadImage(unit.spritesheet)
            (start,end) = unit.action()
            unitSprite = []
            for i in range(start,end):
                sprite = pic.crop((0 + 512 * (i % 9) , 0 + 512 * (i // 9)\
                , 512 + 512 * (i % 9), 512 + 512 * (i //9 ) ))
                sprite = self.scaleImage(sprite, 1/2)
                sprite = sprite.transpose(Image.FLIP_LEFT_RIGHT)
                unitSprite.append(sprite)
            if count >= len(self.sprites):
                self.sprites.append(unitSprite)
            else:
                self.sprites[count] = unitSprite

    
    def backgrounds(self):
        self.background = self.background.resize((self.width,self.height))

    def timerFired(self):
        self.backgrounds()
        for counter in range(len(self.spriteCounters)):
            self.spriteCounters[counter] = (1 + self.spriteCounters[counter]) % len(self.sprites[counter])
        self.xd += 10
         
    def redrawAll(self,canvas):
        canvas.create_image(self.width/2, self.height/2, \
            image=ImageTk.PhotoImage(self.background))
        for sprite in range(len(self.sprites)):
            unit = self.sprites[sprite]
            canvas.create_image(self.xd, self.height-150, \
                image=ImageTk.PhotoImage(unit[self.spriteCounters[sprite]]))
        
            
MyApp(width=1400, height=700)