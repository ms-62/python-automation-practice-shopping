import pytest
import logging,os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




#접속 설정 관련은 픽스쳐로 관리
@pytest.fixture(scope="class", autouse=True)
def setup_driver(request):
    #브라우저 옵션
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)  # 스크립트가 끝나도 브라우저가 꺼지지 않게하려면 True 로 변경
    chrome_options.add_argument("--start-maximized")  # 브라우저 창 최대화
    chrome_options.add_argument("--incognito") #강제 시크릿 모드 활성화

    #브라우저 설치 및 서비스 설정
    service = Service(ChromeDriverManager().install())
    _driver = webdriver.Chrome(service=service, options=chrome_options)
    _wait = WebDriverWait(_driver, 10)
    
    if request.cls is not None:
        request.cls.driver = _driver
        request.cls.wait = _wait

    yield _driver, _wait
    
    _driver.quit()
#접속 url
@pytest.fixture(scope="session")
def base_url():
    # 나중에 여기서 환경별로 URL을 분기할 수 있습니다.
    return "https://www.saucedemo.com"

#logging
@pytest.fixture(scope="class", autouse=True)
def setup_logging():
    log_dir = os.path.join("reports", "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, "run.log")
    print(">>> run.log path:", log_path)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s:%(funcName)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(),
        ],
        force=True,
    )
#login
@pytest.fixture
def login_page(setup_driver):
    driver, wait = setup_driver
    # LoginPage 객체를 생성해서 반환
    from pages.login_page import LoginPage
    return LoginPage(driver)

@pytest.fixture
def inventory_page(setup_driver):
    driver, wait = setup_driver
    from pages.inventory_page import InventoryPage
    return InventoryPage(driver)

#정상로그인 메서드
@pytest.fixture()
def login_user(login_page,setup_driver, base_url):
    driver, wait = setup_driver
    driver.get(base_url)
    login_page.pass_login("standard_user", "secret_sauce") #login_page login가져와서 쓰는 형태로 변경
    return driver, wait

#테스트 전에 장바구니 정리하는 픽스쳐
@pytest.fixture()
def cart_setup(login_user, base_url):
    driver, wait = login_user
    from pages.inventory_page import InventoryPage
    inventory_page = InventoryPage(driver)
    
    inventory_page.open_side_bar()
    inventory_page.reset_app_state()
    
    yield
    
    inventory_page.open_side_bar()
    inventory_page.reset_app_state()
        