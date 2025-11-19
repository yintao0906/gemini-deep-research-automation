from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# 1. 指定ChromeDriver路径
chrome_driver_path = "/usr/local/bin/chromedriver"

# 2. 创建Chrome浏览器实例
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# 3. 打开Google登录页面
driver.get("https://accounts.google.com/signin")

# 4. 找到邮箱输入框，输入邮箱
email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys("yintao0906@gmail.com")
email_input.send_keys(Keys.RETURN)

time.sleep(2)  # 等密码页面加载

# 5. 输入密码
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Yt008296!")
password_input.send_keys(Keys.RETURN)

# 6. 登陆后停留 5 秒再自动关闭
time.sleep(5)
driver.close()




_________

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


def main():
    options = Options()
    options.add_argument("--start-maximized")
    # driver = webdriver.Chrome(options=options)

    # 用 Service 指定 chromedriver 的路径
    service = Service("/usr/local/bin/chromedriver")

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    try:
        url = "https://www.w3schools.com/html/html_tables.asp"
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        # 1. 网页标题
        print("页面标题：", driver.title)

        # 2. 抓取所有 a 标签（链接）
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"页面上共有 {len(links)} 个链接（仅打印前 10 个）：")
        for a in links[:10]:
            text = a.text.strip()
            href = a.get_attribute("href")
            print(" - 文本：", text or "<无文本>", " | URL：", href)

        # 3. 抓取表格数据
        # 找到 id 为 customers 的表格
        table = wait.until(
            EC.presence_of_element_located((By.ID, "customers"))
        )

        # 表头（th）
        header_cells = table.find_elements(By.CSS_SELECTOR, "tr th")
        headers = [h.text.strip() for h in header_cells]
        print("\n表头：", headers)

        # 表体（每一行 tr，跳过第 0 行表头）
        rows = table.find_elements(By.CSS_SELECTOR, "tr")[1:]

        data = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [c.text.strip() for c in cells]
            data.append(row_data)

        print("\n表格数据：")
        for row in data:
            print(row)

    finally:
        import time
        time.sleep(5)
        driver.quit()


if __name__ == "__main__":
    main()



________

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        # 1. 打开登录页面
        driver.get("https://the-internet.herokuapp.com/login")

        # 2. 等待用户名输入框出现
        wait = WebDriverWait(driver, 10)
        username_input = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")

        # 3. 输入用户名和密码
        username_input.send_keys("tomsmith")
        password_input.send_keys("SuperSecretPassword!")

        # 4. 点击登录按钮
        login_button.click()

        # 5. 等待登录成功的提示信息
        success_message = wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        print("登录结果提示：", success_message.text.strip())

    finally:
        # 停 5 秒，看一下结果，再退出
        import time
        time.sleep(5)
        driver.quit()


if __name__ == "__main__":
    main()
________
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

jjjj
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
