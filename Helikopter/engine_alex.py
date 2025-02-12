import pygame  
import math
import random
from pygame._sdl2 import Window, Texture, Image, Renderer

import utils_alex

sky_max_x=2000
sky_max_y=1000

global mySky
global myHeli
global myKey_lr
global myKey_ud
myRockets=[]
myCartridge=[]

#--------------------------------------------------------------------------
def img_to_text(rend, file):
                img=pygame.image.load(utils_alex.zip_arch(file))
                tmp=pygame.transform.scale(img, (96*2, 32*2))
                txt=Texture.from_surface(rend,tmp)
                image=Image(txt, (0,0,txt.width, txt.height))
                return image
#--------------------------------------------------------------------------
def img_to_mask(rend, file):
                img=pygame.image.load(utils_alex.zip_arch(file))
                tmp=pygame.transform.scale(img, (96*2, 32*2))
                mask = pygame.mask.from_surface(tmp)
                return mask
#--------------------------------------------------------------------------
class EngineHeli():
        def __init__(self, x,y, renderer):
            self.renderer=renderer
            self.curr_time=0
            self.curr_alpha=255  
            self.image=[]
                       
            #
            self.image.append(img_to_text(renderer,"helicopter_1.png"))
            self.image.append(img_to_text(renderer,"helicopter_2.png"))
            self.image.append(img_to_text(renderer,"helicopter_3.png"))
            self.image.append(img_to_text(renderer,"helicopter_4.png"))
            self.image.append(img_to_text(renderer,"helicopter_5.png"))
            self.image.append(img_to_text(renderer,"helicopter_6.png"))
            self.image.append(img_to_text(renderer,"helicopter_7.png"))
            self.image.append(img_to_text(renderer,"helicopter_8.png"))
            
            self.image[0].blend_mode=1
            self.image[1].blend_mode=1
            self.image[2].blend_mode=1
            self.image[3].blend_mode=1
            self.image[4].blend_mode=1
            self.image[5].blend_mode=1
            self.image[6].blend_mode=1
            self.image[7].blend_mode=1


            self.position_x=x
            self.position_y=y
            self.max_x=0
            self.max_y=0
            self.count=0
            self.up=0
            self.spites=0
            self.angel=0
            self.delay=2
            self.left_right=0
            self.up_down=0
            self.FlipX=0

            
            self.mask1=img_to_mask(renderer,"helicopter_1.png")
            self.mask2=img_to_mask(renderer,"shot.png")

            over=self.mask1.overlap_area(self.mask1, (140,50))
            if over>0:
                    return


            




#----------------------------------------------------------------------------------------------
        def no_change(self):
            if self.delay==2:
                    if self.left_right<0:
                            self.left_right+=1
                    if self.left_right>0:
                            self.left_right-=1
                    if self.up_down<0:
                            self.up_down+=1 
                    if self.up_down>0:
                            self.up_down-=1 

            angle=0
            if self.left_right>0:
                                angle=self.left_right
            if self.left_right<0:
                                angle=360+self.left_right

            self.image[0].angle=angle
            self.image[1].angle=angle
            self.image[2].angle=angle
            self.image[3].angle=angle
            self.image[4].angle=angle
            self.image[5].angle=angle
            self.image[6].angle=angle
            self.image[7].angle=angle

            self.angel=angle


            if self.FlipX==1:
                                self.image[0].flip_x=True
                                self.image[1].flip_x=True
                                self.image[2].flip_x=True
                                self.image[3].flip_x=True
                                self.image[4].flip_x=True
                                self.image[5].flip_x=True
                                self.image[6].flip_x=True
                                self.image[7].flip_x=True
            else:
                                self.image[0].flip_x=False
                                self.image[1].flip_x=False
                                self.image[2].flip_x=False
                                self.image[3].flip_x=False
                                self.image[4].flip_x=False
                                self.image[5].flip_x=False
                                self.image[6].flip_x=False
                                self.image[7].flip_x=False
                
#----------------------------------------------------------------------------------------------
        def change(self, new):
                    if self.FlipX!=1:
                                    if new==1: #rigth
                                        self.left_right+=1         
                                        if self.left_right>80:
                                            self.left_right=80
                                            #self.FlipX=1
                                    if new==-1: #left
                                        self.left_right-=1         
                                        if self.left_right<-80:
                                            self.left_right=-80
                                            #self.FlipX=1
                    else:
                                    if new==1: #rigth
                                        self.left_right+=1         
                                        if self.left_right>80:
                                            self.left_right=80
                                            #self.FlipX=0
                                    if new==-1: #left
                                        self.left_right-=1         
                                        if self.left_right<-80:
                                            self.left_right=-80
                                            #self.FlipX=0

                                    
                    if new==2: #up
                        self.up_down+=1         
                        if self.up_down>80:
                            self.up_down=80                
                    if new==-2: #down
                        self.up_down-=1         
                        if self.up_down<-80:
                            self.up_down=-80  
                    flip=0
                    angle=0
                    #if self.left_right<0:
                    #                    flip=1
                    if self.left_right>0:
                                        angle=self.left_right
                    if self.left_right<0:
                                        angle=360+self.left_right
                    
                    if self.FlipX==1:
                                self.image[0].flip_x=True
                                self.image[1].flip_x=True
                                self.image[2].flip_x=True
                                self.image[3].flip_x=True
                                self.image[4].flip_x=True
                                self.image[5].flip_x=True
                                self.image[6].flip_x=True
                                self.image[7].flip_x=True
                    else:
                                self.image[0].flip_x=False
                                self.image[1].flip_x=False
                                self.image[2].flip_x=False
                                self.image[3].flip_x=False
                                self.image[4].flip_x=False
                                self.image[5].flip_x=False
                                self.image[6].flip_x=False
                                self.image[7].flip_x=False
                                
                    
                    self.image[0].angle=angle
                    self.image[1].angle=angle
                    self.image[2].angle=angle
                    self.image[3].angle=angle
                    self.image[4].angle=angle
                    self.image[5].angle=angle
                    self.image[6].angle=angle
                    self.image[7].angle=angle
                    
                    self.angel=angle

#----------------------------------------------------------------------------------------------
        def show(self):
                    self.delay-=1
                    if self.delay<=0:
                        self.delay=2
                        self.spites+=1
                        if self.spites>7:
                            self.spites=0
                    
                    step=0
#-------------------
                    if self.left_right!=0:
                                        step=self.left_right/10
#-------------------
                    if self.left_right<0 and self.delay==1:
                                if self.position_x>50: 
                                                    self.position_x-=1
                    if step<-1:
                                if self.position_x>50: 
                                                    self.position_x+=step
#-------------------
                    if self.left_right>0 and self.delay==1:
                                if self.position_x<1750: 
                                                    self.position_x+=1
                    if step>1 :
                                if self.position_x<1750: 
                                                    self.position_x+=step
                    step=0
                    if self.up_down!=0:
                                 step=self.up_down/10

                    if self.up_down<0 and self.delay==1:
                                if self.position_y>40: 
                                                    self.position_y-=1
                    if step<-1 :
                                if self.position_y>40: 
                                                    self.position_y+=step

                    if self.up_down>0 and self.delay==1:
                                if self.position_y<700: 
                                                    self.position_y+=1
                    if step>1:
                                if self.position_y<700: 
                                                    self.position_y+=step

                    if self.position_y<200:
                                            engine_sky_up_down(-1)
                    if self.position_y>600:
                                            engine_sky_up_down(1)

                    self.image[self.spites].draw(dstrect=(self.position_x, self.position_y))

                   
#--------------------------------------------------------------------------  
        def check(self):
                    #mask=self.mask[self.spites]                 
                    return 0

class EngineImage():
        def __init__(self, file, renderer):
            self.renderer=renderer
            self.curr_time=0
            self.curr_alpha=255                                  
            self.image = pygame.image.load(utils_alex.zip_arch(file))
            self.texture = Texture.from_surface(self.renderer, self.image)
            self.texture.blend_mode=1
            self.position_x=0
            self.position_y=0
            self.max_x=0
            self.max_y=0
            self.count=0
            self.up=0
#--------------------------------------------------------------------------      



def engine_sky(): #2000 x 1000
        mySky.count+=1
        if mySky.count>8:
                mySky.count=0 
                mySky.position_x-=1
                if mySky.up < 0:
                    if mySky.position_y<0:
                            mySky.position_y+=1
                if mySky.up > 0:
                    if mySky.position_y>-200:
                            mySky.position_y-=1
                            

        mySky.texture.alpha=mySky.curr_alpha
        mySky.texture.draw(dstrect=(mySky.position_x, mySky.position_y))
        delta=sky_max_x-mySky.max_x #520
        if mySky.position_x<=(- (delta)):
            mySky.texture.draw(dstrect=(mySky.position_x+2000, mySky.position_y))
            

        if mySky.position_x<=(-sky_max_x):
            mySky.position_x=0

#-----------------------------------------------------------------------------------------------                    
def engine_sky_up_down(up):
        mySky.up=up
#-----------------------------------------------------------------------------------------------
def engine_heli():
        global myHeli 
        global myKey_lr
        global myKey_ud
        if myKey_lr!=0:
            if myKey_lr==pygame.K_LEFT:
                myHeli.change(-1)
            if myKey_lr==pygame.K_RIGHT:
                myHeli.change(1)
        if myKey_ud!=0:                
            if myKey_ud==pygame.K_UP:
                myHeli.change(-2)
            if myKey_ud==pygame.K_DOWN:
                myHeli.change(2)
        if myKey_lr==0 and myKey_ud==0:
            myHeli.no_change()

        myHeli.show()
        myHeli.check()

#-----------------------------------------------------------------------------------------------
def engine_heli_change(a):
        global myHeli
        myHeli.change(a)

#-----------------------------------------------------------------------------------------------
class SpriteCartridge():
        def __init__(self,x,y,angle,direction):
            self.curr_time=0
            self.curr_alpha=255                                  
            self.position_x=x+0.00
            self.position_y=y+0.00
            self.max_x=0
            self.max_y=0
            self.radius=0
            self.angle=angle
            self.direction=direction

def cartridge_add():
    if myHeli.FlipX==0:
        r_x=98
        r_y=32
        angle=360-myHeli.angel
        radian=(angle*3.14159/180)
        x = r_x*math.cos(radian)
        y = r_y*math.sin(radian)
        add=32+24
        myCartridge.add(myHeli.position_x+x+48,myHeli.position_y+add-y,myHeli.angel, myHeli.FlipX )
    else:
        r_x=32 
        r_y=32
        angle1=myHeli.angel-90  
        radian1=(angle1*3.14159/180) 
        angle2=myHeli.angel  
        radian2=(angle2*3.14159/180) 

        x = r_x*math.cos(radian1)

        y = r_y*math.sin(radian2)
        add=32+24
        myCartridge.add(myHeli.position_x+32-x,myHeli.position_y+add-y,myHeli.angel, myHeli.FlipX )

def cartridge_more_add():
        for x in range(40):
            angle=x*9
            myCartridge.add(myHeli.position_x,myHeli.position_y,angle, 0 )
    
    
class EngineCartridge():
        def __init__(self, file, renderer):
            self.renderer=renderer
            image = pygame.image.load(utils_alex.zip_arch(file))
            texture = Texture.from_surface(self.renderer, image)
            texture.blend_mode=1
            self.image=Image(texture, (0,0,texture.width, texture.height))
            self.image.blend_mode=1
            self.cartridges=[]

        def add(self, x,y,angle,direction ):
            sprite=SpriteCartridge(x,y,angle,direction)
            self.cartridges.append(sprite)


        def show(self):
             ccc=len(self.cartridges)
             if ccc>0 and ccc<20:
                        ccc=0
             for r in self.cartridges: 
                    self.image.angle=r.angle

                    if r.direction==1:
                        self.image.flip_x=True
                    else:
                        self.image.flip_x=False
                                  
                    if r.direction==0:
                                r.radius+=10                                
                                angle=0
                                if r.angle<0:
                                        angle=-r.angle
                                else:
                                        angle=360-r.angle

                                radian=(angle*3.14159/180)
                                x = r.radius*math.cos(radian)
                                y = r.radius*math.sin(radian)
                                
                                self.image.draw(dstrect=(r.position_x+x, r.position_y-y))
                                if r.position_x+x>2000:
                                            self.cartridges.remove(r)
                                            continue
                                if r.position_x+x<-100:
                                            self.cartridges.remove(r)
                                            continue
                                if r.position_y-y<-100:
                                            self.cartridges.remove(r)
                                            continue
                                if r.position_y-y>1000:
                                            self.cartridges.remove(r)
                                            continue


                    if r.direction==1:
                                r.radius+=10
                                angle=0
                                if r.angle<0:
                                        angle=-r.angle
                                else:
                                        angle=360-r.angle

                                radian=(angle*3.14159/180)
                                x = r.radius*math.cos(radian)
                                y = r.radius*math.sin(radian)
                                
                                self.image.draw(dstrect=(r.position_x-x, r.position_y+y))
                                if r.position_x-x<-100:
                                            self.cartridges.remove(r)
                                            continue
                                if r.position_y+y<-100:
                                            self.cartridges.remove(r)
                                            continue
                                if r.position_y+y>1000:
                                            self.cartridges.remove(r)
                                            continue


#--------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------


class SpriteSmoke():
        def __init__(self,x,y,angle,direction):
            self.curr_time=0
            self.curr_alpha=255                                  
            self.position_x=x+0.00
            self.position_y=y+0.00
            self.angle=angle
            self.direction=random.randrange(-1, 2)
            self.sprites=0
            self.delay=0
            

class SpriteRocket():
        def __init__(self,x,y,angle,direction):
            self.curr_time=0
            self.curr_alpha=255                                  
            self.position_x=x+0.00
            self.position_y=y+0.00
            self.max_x=0
            self.max_y=0
            self.radius=0
            self.angle=angle
            self.direction=direction
            self.engine_smokes=[]
            self.smoke_int=0
            

def rocket_add():
    if myHeli.FlipX==0:
        r_x=98
        r_y=32
        angle=360-myHeli.angel
        radian=(angle*3.14159/180)
        x = r_x*math.cos(radian)
        #x=98
        y = r_y*math.sin(radian)
        add=32+24
        myRockets.add(myHeli.position_x+x,myHeli.position_y+add,myHeli.angel, myHeli.FlipX )
    else:
        r_x=32 
        r_y=32
        angle1=myHeli.angel-90  
        radian1=(angle1*3.14159/180) 
        angle2=myHeli.angel  
        radian2=(angle2*3.14159/180) 

        x = r_x*math.cos(radian1)
        #x=98
        y = r_y*math.sin(radian2)
        add=32+24
        myRockets.add(myHeli.position_x+32-x,myHeli.position_y+add-y,myHeli.angel, myHeli.FlipX )

def load_smoke(render, file):
            image = pygame.image.load(utils_alex.zip_arch(file))            
            texture = Texture.from_surface(render, image)
            img=Image(texture, (0,0,texture.width, texture.height))
            img.blend_mode=1
            return img

    
class EngineRocket():
        def __init__(self, file, file1, file2,file3, file4, file5, file6, file7,renderer):
            self.renderer=renderer
            image = pygame.image.load(utils_alex.zip_arch(file))
            texture = Texture.from_surface(self.renderer, image)
            texture.blend_mode=1
            self.image=Image(texture, (0,0,texture.width, texture.height))
            self.image.blend_mode=1
            self.rockets=[]
            self.smoke=[]            
            self.smoke.append(load_smoke(renderer,file1))
            self.smoke.append(load_smoke(renderer,file2))
            self.smoke.append(load_smoke(renderer,file3))
            self.smoke.append(load_smoke(renderer,file4))
            self.smoke.append(load_smoke(renderer,file5))
            self.smoke.append(load_smoke(renderer,file6))
            self.smoke.append(load_smoke(renderer,file7))
            


        def add(self, x,y,angle,direction ):
            spriteRocket=SpriteRocket(x,y,angle,direction)
            self.rockets.append(spriteRocket)


        def show(self):
             for r in self.rockets: 
                    self.image.angle=r.angle

                    if r.direction==1:
                        self.image.flip_x=True
                    else:
                        self.image.flip_x=False
                                  
                    if r.direction==0:
                                r.radius+=6 
                                angle=0
                                if r.angle<0:
                                        angle=-r.angle
                                else:
                                        angle=360-r.angle

                                radian=(angle*3.14159/180)
                                x = r.radius*math.cos(radian)
                                y = r.radius*math.sin(radian)
                                r.smoke_int+=1
                                if r.smoke_int>5:
                                    r.smoke_int=0
                                    y_c=32*math.sin(radian)
                                    smoke=SpriteSmoke(r.position_x+x-20, r.position_y-y-9+y_c,r.angle,r.direction)                                    
                                    r.engine_smokes.append(smoke)
                                for s in r.engine_smokes:
                                    s.position_y+=(s.direction/10)
                                    self.smoke[s.sprites].draw(dstrect=(s.position_x, s.position_y))
                                    s.delay+=1
                                    if  s.delay>15:
                                        s.delay=0
                                        s.sprites+=1
                                        if s.sprites>6:
                                            r.engine_smokes.remove(s)
                                            continue
                                
                                self.image.draw(dstrect=(r.position_x+x, r.position_y-y))
                                if r.position_x+x>2000:
                                            self.rockets.remove(r)
                                            continue
                                if r.position_y-y<-100:
                                            self.rockets.remove(r)
                                            continue
                                if r.position_y-y>1000:
                                            self.rockets.remove(r)
                                            continue


                    if r.direction==1:
                                r.radius+=6
                                angle=0
                                if r.angle<0:
                                        angle=-r.angle
                                else:
                                        angle=360-r.angle

                                radian=(angle*3.14159/180)
                                x = r.radius*math.cos(radian)
                                y = r.radius*math.sin(radian)

                                r.smoke_int+=1
                                if r.smoke_int>5:
                                    r.smoke_int=0
                                    y_c=32*math.sin(radian)
                                    smoke=SpriteSmoke(r.position_x-x+20, r.position_y+y-9-y_c,r.angle,r.direction)                                    
                                    r.engine_smokes.append(smoke)
                                for s in r.engine_smokes:
                                    s.position_y+=(s.direction/10)
                                    self.smoke[s.sprites].draw(dstrect=(s.position_x, s.position_y))
                                    s.delay+=1
                                    if  s.delay>15:
                                        s.delay=0
                                        s.sprites+=1
                                        if s.sprites>6:
                                            r.engine_smokes.remove(s)
                                            continue
                                
                                self.image.draw(dstrect=(r.position_x-x, r.position_y+y))
                                if r.position_x-x<-100:
                                            self.rockets.remove(r)
                                            continue
                                if r.position_y+y<-100:
                                            self.rockets.remove(r)
                                            continue
                                if r.position_y+y>1000:
                                            self.rockets.remove(r)
                                            continue


#--------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
def engine_rocket():
        myRockets.show()

def engine_cartridge():
        myCartridge.show()
#-----------------------------------------------------------------------------------------------

def engine_init(renderer, max_x, max_y):
        global mySky
        global myHeli
        global myKey_lr
        global myKey_ud
        global myRockets
        global myCartridge

        myHeli=EngineHeli(100,max_y-200,renderer)
        mySky=EngineImage("sky.png" ,renderer)
        myRockets=EngineRocket("rocket.png", "smoke1.png","smoke2.png","smoke3.png","smoke4.png","smoke5.png","smoke6.png","smoke7.png",renderer)
        myCartridge=EngineCartridge("shot.png" ,renderer)
        mySky.curr_alpha=200
        mySky.max_x=max_x # 2000- 1480=520   
        mySky.max_y=max_y #800
        mySky.position_x=0 #2000
        mySky.position_y=-200 #1000-800
        myKey_lr=0
        myKey_ud=0
    
#-----------------------------------------------------------------------------------------------
def engine():
         engine_sky()
         engine_heli()

         engine_rocket()
         engine_cartridge()

         



#-----------------------------------------------------------------------------------------------
#K_DOWN K_UP K_RIGHT K_LEFT 
#
def set_key(key):
    global myKey_lr
    global myKey_ud
    if key==pygame.K_LEFT or key==pygame.K_RIGHT:    
                myKey_lr=key
    if key==pygame.K_UP or key==pygame.K_DOWN:    
                myKey_ud=key
    if key==pygame.KSCAN_F or key==pygame.K_f :
            if myHeli.FlipX==0:
                    myHeli.FlipX=1
                    #myHeli.left_right=-myHeli.left_right
            else: 
                    myHeli.FlipX=0
                    #myHeli.left_right=-myHeli.left_right
    if key==pygame.KSCAN_R or key==pygame.K_r:
                    rocket_add()

    if key==pygame.KSCAN_H or key==pygame.K_h:
                    cartridge_more_add()

    if key==pygame.K_SPACE:
                    cartridge_add()

    myHeli.no_change()
#-----------------------------------------------------------------------------------------------
#K_DOWN K_UP K_RIGHT K_LEFT 
#
def clear_key(key): 
    global myKey_lr
    global myKey_ud
    if key==pygame.K_LEFT or key==pygame.K_RIGHT:    
                myKey_lr=0
    if key==pygame.K_UP or key==pygame.K_DOWN:    
                myKey_ud=0



def colliderect(self, *other):
        rect = self.__class__(*other)
        return (
            self.x < rect.x + rect.w and
            self.y < rect.y + rect.h and
            self.x + self.w > rect.x and
            self.y + self.h > rect.y
        )
