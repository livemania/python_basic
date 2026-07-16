# Chap07_ChatGPT 로 생성한_ 다운로드 받은 파일 자동 분류.py
import os
import os.path
import shutil
import glob

# 기준 설정 완료.
#base_url = r'C:\Users\xlimit\Documents\github_copilot\python_basic'
base_url = os.getcwd()

# 분류할 대상 확장자와 폴더 매핑.
categories = {
    'Images': ['*.jpg', '*.jpeg', '*.JPG', '*.JPEG'],
    'PDFs': ['*.pdf'],
    'Datasets': ['*.csv','*.tsv', '*.xlsx'],
    'Archives': ['*.zip'],
}

# 각 폴더 생성 및 파일 이동.
for folder, patterns in categories.items():
    target_dir = os.path.join(base_url, folder)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for pattern in patterns:
        files = glob.glob(os.path.join(base_url, pattern))

        for file in files:
            try:
                shutil.move(file, target_dir)
                print(f'Moved {os.path.basename(file)}-> {folder}')
            except Exception as e:
                print(f'Error Moving {file}: {e}')