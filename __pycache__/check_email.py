import re

def check_email(email):
    # 소문자 r를 추가한 것은 백슬래시를 두번 겹쳐서 사용하지 않고 한번만 사용하겠다는 의미임. raw string notation 문법
    pattern = r'^[a-zA-Z0-9_+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.search(pattern, email):
        return True
    else:
        return False

# 샘플 이메일 리스트.
emails = [
    "john.doe@example.com",
    "user_name123@domain.com",
    "user+tag@sub.domain.org",
    "invalid-email.com",
    "user@.com",
    "user@domain",
    "@nouser.com",
    "user@domain.c",
    "user@domain..com",
    "user@@domain.com"
]

# 결과 출력.
for email in emails:
    result = check_email(email)
    print(f"{email:30}->{'Valid' if result else 'Invalid'}")