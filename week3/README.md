3주차 파이썬(1) 
---


# 목표
* 파이썬의 이해
* 변수, 기본 자료형
* 리스트와 딕셔너리

참고자료

- 파이썬 자습서 : [https://docs.python.org/ko/3/tutorial/index.html](https://docs.python.org/ko/3/tutorial/index.html)
- 파이썬 레퍼런스 : [https://docs.python.org/ko/3/reference/index.html](https://docs.python.org/ko/3/reference/index.html#reference-index)
- 파이썬 표준 라이브러리 : [https://docs.python.org/ko/3/library/index.html](https://docs.python.org/ko/3/library/index.html)

# 파이썬 기초

## 파이썬으로 어떤 것들을 할 수 있는가?

- GUI 프로그래밍
- 웹 프로그래밍
- 업무 자동화
- 데이터 크롤링
- 데이터 분석
- ...

## 파이썬이란?

- 귀도 반 로섬
- ![img.png](img.png)    

파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python's Flying Circus〉에서 따온 것이다.  
Python 2.0의 최종 버전은 2000년 10월 16일에 릴리스되었습니다.  
Python 2.7.0은 2010년 7월 3일에 릴리스되었습니다.  
Python 3.0 최종 버전은 2008년 12월 3일에 릴리스되었습니다.  
파이썬은 시스템 유틸리티, GUI 프로그래밍, 웹 프로그래밍, 데이터 분석 등에서 많이 사용되고 있다.  

### 파이썬 특징

- 고급언어
- 가독성이 높음
- 인터프리터식(=스크립트) 언어
- 객체지향적
- 동적 타이핑
- 무료 오픈소스
- 플랫폼 독립적 언어

### 파이썬 철학

- "아름다운 게 추한 것보다 낫다." (Beautiful is better than ugly)
- "명시적인 것이 암시적인 것 보다 낫다." (Explicit is better than implicit)
- "단순함이 복잡함보다 낫다." (Simple is better than complex)
- "복잡함이 난해한 것보다 낫다." (Complex is better than complicated)
- "가독성은 중요하다." (Readability counts)

[https://www.python.org/dev/peps/pep-0020/](https://www.python.org/dev/peps/pep-0020/)

### 파이썬 장단점

장점

- 배우기 쉬움
- 생산성이 뛰어남
- 활발한 생태계
- 배터리 포함(Battery Included)
    - [https://www.python.org/dev/peps/pep-0206/#id3](https://www.python.org/dev/peps/pep-0206/#id3)

단점

- 느리다

### 파이썬 설치

다운로드 링크 : [https://www.python.org/downloads/](https://www.python.org/downloads/)


## 용어 알고가기

등호(`=`), 소괄호(`()`), 중괄호(`{}`), 대괄호(`[]`)

변수

들여쓰기

주석

키워드

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

연산자

```
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
```

구분자

```
(       )       [       ]       {       }
,       :       .       ;       @       =       ->
+=      -=      *=      /=      //=     %=      @=
&=      |=      ^=      >>=     <<=     **=
```

## 자료형, 연산자

자료형 요약

### 정수(int)

- 성질, 이뮤터블
- 생성 방법
- 연산

### 실수(float)

- 성질, 이뮤터블
- 생성 방법
- 연산

### 문자열(str)

- 이뮤터블
- 생성 방법
- 연산
- 슬라이싱
- 관련 기능(함수)
- [https://docs.python.org/ko/3/reference/lexical_analysis.html#f-strings](https://docs.python.org/ko/3/reference/lexical_analysis.html#f-strings)

### 리스트(list)

- 뮤터블
- 생성 방법
- 연산
- 슬라이싱
- 관련 기능(함수)

### 튜플(tuple)

- 뮤터블
- 생성 방법
- 연산
- 슬라이싱
- 관련 기능(함수)

### 딕셔너리(dict)

- 이뮤터블
- 생성 방법
- 연산
- 슬라이싱
- 관련 기능(함수)

### 집합(set)

- 이뮤터블
- 생성 방법
- 연산
- 슬라이싱
- 관련 기능(함수)

### 불린(bool)

- 이뮤터블
- 생성 방법
- 연산
- 관련 기능(함수)