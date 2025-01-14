from selenium import webdriver
import time

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import base64
from solver import PuzleSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
#options.add_extension('extension_1_6_6_0.crx')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"


fnumbers=["3324974902","3358079281","3367956840","3368634399","3368988235","3369522534","3370335881","3370745103","3324974923","3358366138","3367947513","3368634390","3368988202","3369521468","3370335878","3370743891","3324974951","3358718461","3367936495","3368628137","3368988201","3369515080","3370335872","3370741263","3324975036","3359085530","3367935506","3368621483","3368988185","3369512768","3370335870","3370738516","3324975069","3362044735","3367934492","3368619838","3368988168","3369508629","3370335864","3370736987","3324975071","3362504974","3367931638"]
recount=0
count=0
def wait_for_selector(drivers, selector, by=By.XPATH, timeout=30, EC_condtion=None):
    wait = WebDriverWait(drivers, timeout=timeout)
    el = wait.until(lambda d: d.find_element(by, selector))
    if EC_condtion:
        el = wait.until(EC_condtion(by, selector))
    return el


def capcha(driver):
    try:


        canvas = driver.find_element(By.CSS_SELECTOR,'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_slice.geetest_absolute')

        canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

        canvas_png = base64.b64decode(canvas_base64)

        with open(r"shot.png", 'wb') as f:
            f.write(canvas_png)

        canvas1 = driver.find_element(By.CSS_SELECTOR,'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_bg.geetest_absolute')

        canvas_base641 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas1)

        canvas_png1 = base64.b64decode(canvas_base641)

        with open(r"screen.png", 'wb') as f:
            f.write(canvas_png1)
        y="shot.png"

        o="screen.png"




        solver = PuzleSolver(y, o)
        solution = solver.get_position()

        button = driver.find_element(By.CLASS_NAME,'geetest_slider_button')
        ActionChains(driver).click_and_hold(button).perform()
        ActionChains(driver).move_by_offset(xoffset=solution, yoffset=0).perform()
        time.sleep(1.41)
        ActionChains(driver).release().perform()

        try:
            while True:
                try:
                    time.sleep(8)
                    driver.execute_script("document.querySelector('.geetest_refresh_1').click()")
                    time.sleep(8)

                    canvas = driver.find_element(By.XPATH,"33//canvas[2]")

                    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);",
                                                          canvas)

                    canvas_png = base64.b64decode(canvas_base64)

                    with open(r"imgcap/screenshot1.png", 'wb') as f:
                        f.write(canvas_png)

                    canvas1 = driver.find_element(By.XPATH,"33//canvas[1]")

                    canvas_base641 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);",
                                                           canvas1)

                    canvas_png1 = base64.b64decode(canvas_base641)

                    with open(r"imgcap/screenshot2.png", 'wb') as f:
                        f.write(canvas_png1)

                    solver = PuzleSolver("imgcap/screenshot1.png", "imgcap/screenshot2.png")
                    solution = solver.get_position()

                    button = driver.find_element_by(By.CLASS_NAME,'geetest_slider_button')
                    ActionChains(driver).click_and_hold(button).perform()
                    ActionChains(driver).move_by_offset(xoffset=solution, yoffset=0).perform()
                    time.sleep(1.43)
                    ActionChains(driver).release().perform()
                except:
                    break
        except:
            pass
    except:

        pass
while(1):
    driver = webdriver.Chrome(options=options, desired_capabilities=capa)
    time.sleep(20)
    chwd = driver.window_handles

    if (len(chwd) >= 2):
        driver.switch_to.window(chwd[1])

        driver.close()
        driver.switch_to.window(chwd[0])
    driver.get('https://www.pionex.com/en-US/signUp')
    while (1):
        try:

            time.sleep(10)
            chwd = driver.window_handles

            if (len(chwd) >= 2):
                driver.switch_to.window(chwd[1])

                driver.close()
                driver.switch_to.window(chwd[0])
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                               '//input[@type="checkbox"]')))
            phonee.click()
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                              '//button[@class="ant-btn t-button ant-btn-primary"]')))
            phonee.click()
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.ID,
                                                "rc-tabs-1-tab-phone_number")))
            phonee.click()

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#rc-tabs-1-panel-phone_number > div > div.ant-col.pi-form-item-control > div > div > div > div.pi-select-wrap.accountCodeSelect___3lK-t.pi-select-wrap-has-value.pi-select-wrap-lg')))
            phonee.click()
            time.sleep(1)
            while(1):
             try:
               phonee = WebDriverWait(driver, 120).until(
                 EC.presence_of_element_located((By.XPATH,
                                                 '//input[@placeholder="Select area code"]')))
               phonee.send_keys("pakistan")
               break
             except:
              pass
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.NAME,
                                                'Pakistan')))
            phonee.click()
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#accountPhone')))
            phonee.send_keys(fnumbers[recount])
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#')))
            phonee.send_keys("")
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//button[@class="pi-btn pi-btn-primary pi-btn-lg w-full mt-[8px] font-medium"]')))
            phonee.click()
            time.sleep(20)


            capcha(driver)
            time.sleep(5)
            driver.refresh()
            count = count + 1
            if (recount < (len(fnumbers) - 1)):
                recount = recount + 1
            else:
                recount = 0
            print(count)
        except Exception as e:
            try:

              driver.close()
            except Exception  as e:

                pass
            break



