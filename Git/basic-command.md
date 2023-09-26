# basic command
> git 기본 문법 정리

## 초기 설정
```bash
git config --global user.email <email>
git config --global user.name <name>
```

## git 저장소 만들기

- `git init`
    - `git directory`를 생성해주는 명령어
    - 관리하고 싶은 최상위 위치에서 실행

## git 상태 체크

- `status`
    - 현재 git으로 관리되고있는 파일/폴더의 상태를 출력

## 코드 수정하고 저장소에 저장하기

- `add`
    - `git add <파일/폴더이름>`
    - `working directory` 에서 `staging area`로 추가
    - 일반적으로 모든 파일, 포더를 추가하기 위해 아래의 코드를 사용
        - `git add .`

- `commit`
    - `git commit -m "message"`
    - `staging area`에 올라간 파일들의 스냅샷을 찍어서 `.git directory`에 저장
    - 일반적으로 `-m` 옵션을 넣어서 메세지를 추가하여 등록

## 원격저장소에 업로드하기

- `remote add`
    - `git remote add origin <UrL>`
    - 원격저장소 주소를 origin 이라는 이름으로 저장

- `push`
    - `git push <원격저장소이름> <브랜치이름>`
    - 원격저장소에 브랜치를 업로드

## Github Page 생성하기

- `github.io` 
   - https://사용자이름.github.io/저장소이름/ 를 통해 본인의      Github 웹페이지 생성

## 원격저장소에서 불러오기

- `pull`
    - `git pull <원격저장소이름> <브랜치이름>`
    - 원격저장소에 저장된 브랜치를 불러오기

## 원격저장소에 있는 타인 코드를 복사하기

- `clone`
    - `git clone <원격저장소 코드 링크>`
    - 터미널을 이용하여 현재 파일 위치를 찾아 `git clone <원격저장소 링크>` 를 하여 타인의 코드를 복사

## 새로운 Branch를 생성하기

- `branch`
    - `git branch` : 현재의 branch를 확인한다.
    - `git branch <브랜치명>` : 새로운 branch를 생성한다.
        - `git branch -c <브랜치명>` : branch를 생성하며, 그 branch로 이동 
    - `git switch <브랜치명>` : <브랜치명>으로 이동한다.
    - `git branch -d <브랜치명>` : 해당 branch를 삭제한다.
        - **주의** : push 할 때, 새 branch 명을 입력한다.