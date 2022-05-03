import pyautogui, webbrowser

from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+573122389016")

sleep(10)

for i in range(10):
    pyautogui.typewrite('#Advertencia! Posible incendio!#')
    pyautogui.press('enter')