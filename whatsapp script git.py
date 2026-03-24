from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# تشغيل المتصفح
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# فتح واتساب ويب
driver.get("https://web.whatsapp.com")

wait = WebDriverWait(driver, 60)

print("اعمل Login بالـ QR Code...")

# انتظار لحد ما الشاتات تظهر (يعني اللوجين تم)
wait.until(
    EC.presence_of_element_located((By.XPATH, 'All chats'))
)

print("تم تسجيل الدخول")

# فتح أول شات
first_chat = wait.until(
    EC.element_to_be_clickable((By.XPATH, 'Choose chat'))
)
first_chat.click()

# انتظار مربع الكتابة
message_box = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, 'message box')
    )
)

# كتابة وإرسال رسالة
message_box.send_keys("Hi this is a semi automated message from Selenium \n From ur lover AboNana")
message_box.send_keys(Keys.ENTER)
time.sleep(10)

print("تم إرسال الرسالة")
