from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main():
    # 1. Connect to the already-opened and logged-in Chrome browser (debug port 9222).

    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(options=options)

    try:
        # 2. Open the Google Gemini page.
        driver.get("https://gemini.google.com/app")

        # Wait for the input box to appear.
        wait = WebDriverWait(driver, 30)
        input_box = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[contenteditable='true']")
            )
        )

        # 3. Send the prompt
        prompt = "Write a 3-sentence summary about machine learning."
        input_box.send_keys(prompt)
        input_box.send_keys(Keys.ENTER)
        print("Prompt sent. Waiting for response...")

        # 4. Wait for Gemini to produce the response.
        time.sleep(15)

        # 5. First try to fetch the latest response using message-content.
        response_text = ""

        contents = driver.find_elements(By.CSS_SELECTOR, "message-content")
        if contents:
            latest = contents[-1]
            response_text = driver.execute_script(
                "return arguments[0].innerText;", latest
            ).strip()
        else:
            # If there is no message-content, use the fallback method: capture all p[data-path-to-node] elements.
            print("No <message-content> found, fallback to <p[data-path-to-node]>.")
            paras = driver.find_elements(By.CSS_SELECTOR, "p[data-path-to-node]")
            parts = []
            for p in paras:
                txt = p.text.strip()
                if txt:
                    parts.append(txt)
            response_text = "\n".join(parts)

        # 6. Save to a text file.
        with open("gemini_output.txt", "w", encoding="utf-8") as f:
            f.write("PROMPT:\n")
            f.write(prompt + "\n\n")
            f.write("RESPONSE:\n")
            f.write(response_text)

        print("Output saved to gemini_output.txt")

    finally:
        # If you want to close the browser automatically, change it to driver.quit().
        # driver.quit()
        pass


if __name__ == "__main__":
    main()
