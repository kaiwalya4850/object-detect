camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/master/image.jpg')
camera.stop_preview()