# 네이버 카페나 블로그를 검색하는 경우 먼저 로그인 필요함.
# 이런 경우 아래와 같이처리할 수 있음.
# 미리본인이 사용하는 아이디와 암호를입력해서 클립보드에서 복사해서 붙여넣기를 하는 것처럼 처리할 수있음.
# 네이버에서 로그인하는 주소는 실제 브라우저 창에서 주소를 복사해서 사용하면 됨.

# F12 개발자 모드에서 입력 태그를 찾고,
# 아이디를 입력하는 태그의 이름은 id 인것을 찾을 수 있음. 패스워드는 pw임
# 하단의 로그인하는 버튼의 id는 log.login 임.

# driver.get('주소')을 사용해서 해당 주소를 검색하는 원격 브라우저를 실행함.
#로그인을 해야하는 페이지로 이동해서 아이디를 입력하고 clipboard 모듈의 copy()함수를 사용해서 아이디를 복사해서 붙여넣기 하면 됨.
# drive.find_element() 메서드에서 사용하는 By.XPATH 는 XPATH 수식을 사용한다는 의미임.
# '//*[@id="id"]' 라는 수식은 태그 전체에서 id  속성(@id)이 id 로 되어 있는태그를 검색함.
# 미리 검색을 했던 <input type='text' id='id'>로 되어 있는 아이디 입력 태크를 검색하는 코드임.
# 여기에 ctrl + v 로 붙여넣기를 하는 형태로 미리 지정된 아이디 값이 넘어감.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

# selenium 4.6 이상은 웹드라이버 설치 없이 사용.
driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')

# 로그인 창에 아이디/비밀번호 입력.
loginID = "livemania"
clipboard.copy(loginID)
# mac 은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH, '//*[@id="id"]').send_keys(Keys.CONTROL, 'v')

loginPW = "nexb08)*)*"
clipboard.copy(loginPW)

driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys(Keys.CONTROL,'v')

# 로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()

while True: # 검색이 종료되면 창이 닫히기 때문에 무한 루프를 돌리는 구문임.
    pass  # 당장 아무것도 하고 싶지 않을때 사용하는 키워드.