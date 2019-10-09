import pyautogui as pg

def click_on_image():
    button_loc = pg.locateOnScreen('pic.png')
    print(button_loc)

    button_loc_point = pg.center(button_loc)
    print(button_loc_point)

    button_loc_x, button_loc_y = button_loc_point

    print(button_loc_y)

    pg.click(button_loc_x, button_loc_y, duration=5)

if __name__ == '__main__':
    click_on_image()