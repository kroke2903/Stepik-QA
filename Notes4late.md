1. Проект-VCS-venv-folders-files-selenium-pytest--webdriver-manager
   2. base_page.py:
      # Прописывем фикстуру
      # from selenium.webdriver.chrome.service import Service as ChromiumService
      # from webdriver_manager.chrome import ChromeDriverManager
       @pytest.fixture
       def driver(scope='function'): # определяем функцию драйвера, со скопом.
       driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
       # Разворачиваем 
   3. 
       
       
    
    