import tinytuya
import time

#dresserlamp
d = tinytuya.BulbDevice('ebf378c4d0e31c2d91ex42', '192.168.0.11', '8262aa6bb1eb82f8')
d.set_version(3.3)  # IMPORTANT to set this regardless of version
data = d.status()
d.set_mode(mode='colour') # white, colour, scene, music
d.set_colour(162, 0, 255) 
time.sleep(3)
d.set_mode(mode='scene') # white, colour, scene, music

#rightlamp
r = tinytuya.BulbDevice('ebc74c1258aca41c1d3pvu', '192.168.0.238', '84c56702884442c1')
r.set_version(3.3)  # IMPORTANT to set this regardless of version
rdata = r.status()
r.set_mode(mode='colour') # white, colour, scene, music
r.set_colour(255, 94, 0)


#leftlamp
l = tinytuya.BulbDevice('eb71194515a20f5c11qxac', '192.168.0.29', 'e94a74a5ab6cd3f7')
l.set_version(3.3)  # IMPORTANT to set this regardless of version
ldata = l.status()
l.set_mode(mode='white') # white, colour, scene, music
l.set_brightness_percentage(brightness=35)


 #BulbDevice
  #      set_colour(r, g, b):
  #      set_white(brightness, colourtemp):
  #      set_white_percentage(brightness=100, colourtemp=0):
  #      set_brightness(brightness):     # Brightness: Type A devices range = 25-255 and Type B = 10-1000
  #      set_brightness_percentage(brightness=100):
  #      set_colourtemp(colourtemp):
  #      set_colourtemp_percentage(colourtemp=100):
  #      set_scene(scene):             # 1=nature, 3=rave, 4=rainbow
  #      set_mode(mode='white'):       # white, colour, scene, music
  #      result = brightness():
  #      result = colourtemp():
  #      (r, g, b) = colour_rgb():
  #      (h,s,v) = colour_hsv()
  #      result = state():


  #rl = tinytuya.BulbDevice('device id', '192.168.0.11', 'local key')
