import pyautogui,time
pyautogui.FAILSAFE = True
a=10000
b=0
time.sleep(3)
while(a>b):
   pyautogui.write("pls fish")
   pyautogui.press('enter')   
   time.sleep(40)
   b=b+1
