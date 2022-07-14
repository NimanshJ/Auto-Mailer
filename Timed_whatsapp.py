import pywhatkit
import time
import pyautogui
import keyboard as k

phone = input("The phone no. to which u want to send the msg: ")
msg = input("The msg you want to send: ")
hour, min = map(int, input("Enter the time (h m): ").split())


pywhatkit.sendwhatmsg(f'+91{phone}', msg, hour, min)
pyautogui.click(1320, 690)
time.sleep(5)
k.press_and_release('enter')