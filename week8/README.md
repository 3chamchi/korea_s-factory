파이참 장고 설정, 장고 명령어 등
---
# 파이참 장고 설정
#### 파이참 프로젝트 디렉토리 열기
* 프로젝트 디렉토리 열기, ```manage.py```가 있는 디렉토리

#### 파이참 파이썬 인터프리터(가상환경) 설정
* 파일 -> 설정 -> 프로젝트 -> Python 인터프리터 -> Python 인터프리터 설정
* 프로젝트 디렉토리에 있는 ```venv```안의 ```python``` 선택
* 없는 경우 가상환경 생성 후 선택

# 명령어
## 윈도우 파워쉘, 터미널 명령어
#### 디렉토리(폴더) 이동
* ```cd {디렉토리명}```

#### 현재 경로 확인
* ```pwd```

#### 현재 디렉토리 파일 등 확인
* ```ls```

## 파이썬 명령어
#### 패키지 설치
* ```pip install {패키지이름}```
* ```python -m pip install {패키지이름}```

#### 패키지 업데이트
* ```pip install --upgrade pip```

#### 가상환경 생성 
* ```python -m venv venv```
* ```python -m venv {가상환경명}```

#### 가상환경 접속  
* 가상환경 접속 시 가상환경 폴더가 있는 위치에서 실행
* 가상환경 접속 후 ```(venv)``` 가상환경명을 접속 확인
* (Windows) ```.\venv\Scrips\activate```
* (Mac) ```soruce venv/bin/activate```

## 장고 명령어
#### 프로젝트 생성  
* ```django-admin startproject config .```
* ```django-admin startproject {프로젝트 이름} {선택/경로}```

#### 앱 생성
* ```django-admin startapp {앱이름}```

#### 장고 서버 실행
* ```python manage.py runserver```

#### 장고 Shell 접속
* ```python manage.py shell```

#### 장고 관리자 계정 생성
* ```python manage.py createsuperuser```

#### DB 생성
* ```python manage.py makemigrations```
* ```python manage.py migrate```

# 참고사항
## Windows 가상환경 접속 오류
1. powershell 관리자 권한 실행
2. 명령어 입력 ```Set-ExecutionPolicy Unrestricted```
3. 파이참, 파워쉘 재실행

## 파이참 터미널, 파워쉘 연결
1. 파일 -> 설정 -> 도구 -> 터미널 -> 애플리케이션 설정 -> 쉘 경로 -> powershell.exe 선택
