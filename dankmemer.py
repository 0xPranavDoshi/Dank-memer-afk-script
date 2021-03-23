import pyautogui,time
pyautogui.FAILSAFE = True
a=10000
b=0
time.sleep(3)
while(a>b):
   pyautogui.typewrite("pls fish")
   pyautogui.press('enter')
   pyautogui.typewrite("pls beg")
   pyautogui.press('enter')      
   pyautogui.typewrite("pls dep all")
   pyautogui.press('enter')   
   time.sleep(45)
   b=b+1
