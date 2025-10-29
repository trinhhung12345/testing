from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import time

# === Cấu hình ===
# Đường dẫn tới file HTML local (chỉnh lại cho đúng)
HTML_PATH = "file:///" + os.path.abspath("login.html")

# Khởi tạo ChromeDriver
service = Service("chromedriver.exe")  # nếu đã nằm trong PATH có thể bỏ
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(HTML_PATH)

def test_login_success():
    """Test case 1: Đăng nhập đúng thông tin"""
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    assert msg == "Đăng nhập thành công!", f"Lỗi: {msg}"
    print("[PASSED] Test đăng nhập thành công")

def test_login_wrong_password():
    """Test case 2: Sai mật khẩu"""
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    assert msg == "Sai tên đăng nhập hoặc mật khẩu!", f"Lỗi: {msg}"
    print("[PASSED] Test sai mật khẩu")

def test_login_empty_fields():
    """Test case 3: Bỏ trống username và password"""
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    assert msg == "Sai tên đăng nhập hoặc mật khẩu!", f"Lỗi: {msg}"
    print("[PASSED] Test bỏ trống trường")

# === Chạy các test case ===
try:
    test_login_success()
    test_login_wrong_password()
    test_login_empty_fields()
finally:
    driver.quit()
