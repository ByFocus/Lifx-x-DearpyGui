import dearpygui.dearpygui as dpg
import requests
import json
import token
selector = "all"
headers = {"Authorization": "Bearer %s" % token,}

def selector_changer(sender):
    global selector
    if sender == 40:
        selector = "all"
    if sender == 42:
        selector = "Here goes your id light"
    if sender == 43:
        selector = "Here goes your id light"
    if sender == 44:
        selector = "Here goes your id light"
    if sender == 45:
        selector = "Here goes your id light"
    print(selector)

def color_changer(sender):
    if sender == 31:
        changeColor = 'blue'
        print('Changing to blue...')
    if sender == 32:
        changeColor = 'purple'
        print('Changing to purple...')
    if sender == 33:
        changeColor = 'red'
        print('Changing to red...')
    if sender == 34:
        changeColor = 'cyan'
        print('Changing to cyan...')
    if sender == 35:
        changeColor = 'white'
        print('Changing to default...')
    payload = {
        "states": [{
        "selector": selector,
        "power": "on",
        "color": changeColor
            }
        ]
    }
    response = requests.put('https://api.lifx.com/v1/lights/states', data=json.dumps(payload), headers=headers)
    print(selector)

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
            }
        ],
    }
    print(selector)

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
  }]}
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

with dpg.window(label="Color", pos=(400, 0)) as window2:
    blueBtn = dpg.add_button(label="Blue", callback= color_changer) #sender = 31
    purpleBtn = dpg.add_button(label="Purple", callback= color_changer) # sender = 32
    redBtn = dpg.add_button(label="Red", callback= color_changer)# sender = 33
    cyanBtn = dpg.add_button(label="Cyan", callback= color_changer)# sender = 34
    whiteBtn = dpg.add_button(label="White", callback= color_changer)# sender = 35

    # 4 Window
with dpg.window(label='Light Selector', pos=(500, 0), width=200):
    with dpg.table(header_row=False):
        dpg.add_table_column()
        dpg.add_table_column()
        selectorAll = dpg.add_button(label="All", callback=selector_changer) #sender = 40
        dpg.add_table_next_column()
        selectNumberOne = dpg.add_button(label="1", width=30, callback=selector_changer) #sender = 42
        selectNumberTwo = dpg.add_button(label="2", width=30, callback=selector_changer) #sender = 43
        selectNumberThree = dpg.add_button(label="3", width=30, callback=selector_changer) #sender = 44
        selectNumberFour = dpg.add_button(label="4", width=30, callback=selector_changer) #sender = 45

    




dpg.setup_viewport()
dpg.set_viewport_title(title='Lifx Controller Lights')
dpg.set_viewport_width(750)
dpg.set_viewport_height(200)

dpg.start_dearpygui()
