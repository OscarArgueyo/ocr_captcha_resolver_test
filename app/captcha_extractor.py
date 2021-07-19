#!/usr/bin/python
from captcha_solver import resolve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def extract(url='http://localhost:8000/',
            captcha_id='captcha',
            captcha_input_xpath='//*[@id="textBox"]',
            captcha_submit_xpath='//*[@id="submitButton"]',
            captcha_output_xpath='//*[@id="output"]',
            output_file='results.txt'):

    options = Options()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--disable-logging')
    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    output_path = 'screenshot.png'
    element = driver.find_element_by_id(captcha_id)
    captcha = element.screenshot(output_path)

    if captcha:
        captcha_solution = resolve(path=output_path)
        driver.find_element_by_xpath(captcha_input_xpath).send_keys(captcha_solution)
        driver.find_element_by_xpath(captcha_submit_xpath).click()
        driver.save_screenshot("results.png")
        text_result_captcha_resolved = driver.find_element_by_xpath(captcha_output_xpath).text
        output_file_fp = open(output_file, "a")
        result_line = f"{captcha_solution} - {text_result_captcha_resolved}\n"

        output_file_fp.write(result_line)
        output_file_fp.close()

    driver.close()
    driver.quit()


if __name__ == '__main__':
    extract()