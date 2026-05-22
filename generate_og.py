from playwright.sync_api import sync_playwright

def generate_screenshot():
    with sync_playwright() as p:
        # Запускаємо браузер у фоновому режимі
        browser = p.chromium.launch()
        
        # Задаємо точні розміри вашої інфографіки (1536x864)
        page = browser.new_page(viewport={"width": 1536, "height": 864})
        
        # Відкриваємо сторінку на локальному сервері
        page.goto("http://localhost:8000", wait_until="networkidle")
        
        # Чекаємо 1.5 секунди (1500 мс), щоб відпрацювала анімація прогрес-барів
        page.wait_for_timeout(1500)
        
        # Зберігаємо у форматі JPEG з якістю 70% для WhatsApp/Telegram
        page.screenshot(path="og-image.jpg", type="jpeg", quality=70)
        
        browser.close()
        print("Скриншот og-image.jpg успішно створено!")

if __name__ == "__main__":
    generate_screenshot()
    
