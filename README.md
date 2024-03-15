# otoge-bot
> 리듬게임 정보를 디스코드 하나로.

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"/><img src="https://img.shields.io/badge/3.9.6-515151?style=for-the-badge&"/>
<img src="https://img.shields.io/badge/Discord.py-5865F2?style=for-the-badge&logo=discord&logoColor=white"/>

## 봇 명령어

TODO ~~빨리맹글어라~~

## 개발 환경 설정

1. GitHub repository 를 clone 합니다.
```sh
git clone https://github.com/quntnim/otoge-bot.git
```
2. 파이썬 설치 후 가상 환경을 설정 합니다. ([Python 3.9.6](https://www.python.org/downloads/release/python-396/))
```sh
python -m venv [가상환경명]
```
3. 파이썬 가상 환경을 실행하고 패키지를 설치 합니다.
```sh
[가상환경명]\Scripts\activate
pip install -r requirements.txt
```
4. parameter.json 파일을 프로젝트 최상단에 생성 후 아래와 같이 입력 합니다.
```json 
{
  "bot-token": "(테스트할 봇 토큰 입력)"
}
```
5. 봇을 실행 합니다.
```sh
python main.py 
```

## 업데이트 내역

* 0.0.1
    * 작업 진행 중