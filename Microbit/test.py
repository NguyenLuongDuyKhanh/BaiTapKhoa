def LED_ON():
   brightness=9
   for z in range(4,-1,-1):
       for x in range(5):
            brightness=9
            for y in range(x,-1,-1):
                if z % 2 == 0:
                    display.set_pixel(y,z,brightness)
                elif z % 2 != 0:
                    display.set_pixel(4-y,z,brightness)
                brightness -=2
            sleep(500)
            display.clear()
LED_ON()