import dearpygui.dearpygui as dpg
import random
import time
from PIL import Image
import pytesseract

notfile = '.png'
der = ''
derfol = ''
chop = 'qwertyuiopasdfghjklzxcvbnm2345678901QWERTYUIOPASDFGHJKLZXCVBNM'
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

dpg.create_context()
dpg.create_viewport(title='png to text',width=1000, height=500)
dpg.setup_dearpygui()
def callback(sender, app_data, user_data):
    print("sender : ", sender)
    if app_data['file_name'] not in notfile:
        global der
        der = app_data['file_path_name']
        der = der.replace("\\\\", "\\")
        dpg.set_value("filej", "Путь файла : " + der)
        print(der)

def callbackx(sender, app_data):
    global derfol
    global dername 
    name = ""
    for i in range(0,9):
        name += random.choice(chop)
    derfol = app_data['file_path_name']
    dername = app_data['file_path_name'] + "\\" + name + ".txt"
    dpg.set_value("filet", "Путь папки для сохранения : " + dername)


def cancel_callback():
    pass

def text_reco():
    global derfol
    global der
    if der == "":
        pass
    else : 
        if derfol == "":
            pass
        else :            
            img = Image.open(der)
            text = pytesseract.image_to_string(img, lang='eng')
            print(text)
            with open(dername, "w") as file:
                file.write(text)
            dpg.set_value("fin", "Импортирование завершенно")
            time.sleep(1)
            dpg.set_value("fin", "...")
            pass


with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, [0, 153, 76], category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, [32, 32, 32])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 153, 76])
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, [0, 153, 76])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 100, 76])
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, [32, 32, 32])
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, [32, 32, 32])
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, [0, 153, 76])
        dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, [0, 153, 76])

with dpg.font_registry():
    with dpg.font(f'Finlandica-Bold.ttf', 13, default_font=True, id="Default font"):
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
dpg.bind_font("Default font")

with dpg.file_dialog(directory_selector=False, show=False, callback=callback, id='file_dialog_id', width=700,height=400, cancel_callback=cancel_callback):
    dpg.add_file_extension(".jpg", custom_text="jpg")
with dpg.file_dialog(directory_selector=True, show=False, callback=callbackx, id='file_dialog_id1', width=700,height=400, cancel_callback=cancel_callback):
    pass



dpg.bind_theme(global_theme)

with dpg.window(width=315, height=440):
    dpg.add_text(label="kek",default_value="Нету файла jpg", wrap=350, tag="filej")
    dpg.add_button(label="Открыть файл с фото", callback=lambda: dpg.show_item("file_dialog_id"),width=300,height=100)
    dpg.add_text(label="kek2",default_value="Нету файла txt", wrap=350, tag="filet")
    dpg.add_button(label="Сохранить в текстовом файле", callback=lambda: dpg.show_item("file_dialog_id1"),width=300,height=100,)
    dpg.add_text(label="kek23",default_value="...", wrap=350, tag="fin")
    dpg.add_button(label="Импортировать",callback=text_reco,width=300,height=100)



dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
