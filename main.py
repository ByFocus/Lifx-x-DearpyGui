import dearpygui.dearpygui as dpg
import requests
import json
import token
headers = {"Authorization": "Bearer %s" % token,}
changeColor = ""
selector = "all"

def selector_changer(sender):
    global selector
    if sender == 48:
        selector = "all"
        print("You've chosen all lights") 
    if sender == 50:
        selector = "Here goes your id light"
        print("You've chosen light numer 1") 
    if sender == 51:
        selector = "Here goes your id light"
        print("You've chosen light numer 2") 
    if sender == 52:
        selector = "Here goes your id light"
        print("You've chosen light numer 3") 
    if sender == 53:
        selector = "Here goes your id light"
        print("You've chosen light numer 4") 

def color_changer(sender):
    global changeColor
    if sender == 35:
        changeColor = 'blue'
        print('Changing to blue...')
    if sender == 36:
        changeColor = 'purple'
        print('Changing yo purple...')
    if sender == 38:
        changeColor = 'red'
        print('Changing to red...')
    if sender == 39:
        changeColor = 'cyan'
        print('Changing to cyan...')
    if sender == 41:
        changeColor = 'white'
        print('Changing to default...')
    if sender == 105:
        print(f'Changing to {changeColor}')
    payload = {
        "states": [
            {
        "selector": selector,
        "power": "on",
        "color": changeColor
            },
        ]
    }
    response = requests.put('https://api.lifx.com/v1/lights/states', data=json.dumps(payload), headers=headers)


def get_color_value(): 
    global changeColor
    getColorValue = dpg.get_value(colorPicker)
    firstColorRounded = int(getColorValue[0])
    secondColorRounded = int(getColorValue[1])
    thirdColorRounded = int(getColorValue[2])
    roundedColors = (f'{firstColorRounded},{secondColorRounded},{thirdColorRounded}')
    print(roundedColors)
    changeColor = (f'rgb:{roundedColors}')
    color_changer(sender=105)
    

def lights_controll(sender):
    if sender == 26:
        petition = 'off'
    else:
      petition = 'on'
      
    payload = {
        "states": [
            {
            "selector": selector,
            "power": petition,
            },
        ],
    }
    response = requests.put('https://api.lifx.com/v1/lights/states', data=json.dumps(payload), headers=headers)

def button_callback(sender):
    print(f"sender is: {sender}")

petition = ''

    
def sender_value_brightness():
  brightness_value = dpg.get_value(sliderBrightness)
  payload = {
    "states": [
      {
          "selector" : selector,
          "brightness": brightness_value
    },
        ]
  }
  response = requests.put('https://api.lifx.com/v1/lights/states', data=json.dumps(payload), headers=headers)


with dpg.theme(default_theme=True):
    dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 140, 23), category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

# 1 Window
with dpg.window(label="Power") as window:

    on = dpg.add_button(label="On", callback=lights_controll)
    off = dpg.add_button(label="Off", callback=lights_controll)

# 2 Window



with dpg.window(label="Brightness", pos=(100,0), width=300, height=100) as window1:
    #sendBrightness = dpg.add_button(label="Send info")
    sliderBrightness = dpg.add_slider_float(label="Brightness", max_value=1, min_value=0, default_value=1) 
    send_info = dpg.add_button(label="Send Info!", callback=sender_value_brightness)
    



# 3 Window

with dpg.window(label="Color", pos=(0, 100), height=600, width=400) as window2:
    with dpg.table(header_row=False):    
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()
        blueBtn = dpg.add_button(label="Blue", callback= color_changer) #sender = 35
        purpleBtn = dpg.add_button(label="Purple", callback= color_changer) # sender = 36
        dpg.add_table_next_column()
        redBtn = dpg.add_button(label="Red", callback= color_changer)# sender = 38
        cyanBtn = dpg.add_button(label="Cyan", callback= color_changer)# sender = 39
        dpg.add_table_next_column()
        whiteBtn = dpg.add_button(label="White", callback= color_changer)# sender = 41
    colorPicker = dpg.add_color_picker(label="Choose a color")
    confirmColor = dpg.add_button(label="Confirm", callback=get_color_value)

    # 4 Window
with dpg.window(label='Light Selector', pos=(400, 0), width=200):
    with dpg.table(header_row=False):
        dpg.add_table_column()
        dpg.add_table_column()
        selectorAll = dpg.add_button(label="All", callback=selector_changer) #sender = 48
        dpg.add_table_next_column()
        selectNumberOne = dpg.add_button(label="1", width=30, callback=selector_changer) #sender = 50
        selectNumberTwo = dpg.add_button(label="2", width=30, callback=selector_changer) #sender = 51
        selectNumberThree = dpg.add_button(label="3", width=30, callback=selector_changer) #sender = 52
        selectNumberFour = dpg.add_button(label="4", width=30, callback=selector_changer) #sender = 53

    




dpg.setup_viewport()
dpg.set_viewport_title(title='Lifx Controller Lights')
dpg.set_viewport_width(617)
dpg.set_viewport_height(740)

dpg.start_dearpygui()
