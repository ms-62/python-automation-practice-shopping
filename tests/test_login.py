import pytest
import logging


logger = logging.getLogger()

#로그인 테스트 파라미터 라이즈
@pytest.mark.parametrize("usr_id , usr_pw",[
    ("standard_user","secret_sauce"),
    ("locked_out_user","secret_sauce"),
    ("problem_user","secret_sauce"),
    ("performance_glitch_user","secret_sauce"),
    ("error_user","secret_sauce"),
    ("visual_user","secret_sauce")
    ])
def test_pass_login(login_page,setup_driver, base_url,usr_id,usr_pw):
    driver, wait = setup_driver
    driver.get(base_url)
    login_page.login(usr_id,usr_pw)
    assert login_page.is_success is True, f"TEST FAILED | ID : {usr_id}" #assert가 최종으로 검증하면 try-except에 raise제외해도됨
        
        