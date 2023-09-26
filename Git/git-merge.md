# Github를 이용한 공동 코드 작업 진행

- Github 를 이용하여 **같은 코드**를 작업을 할 경우

     1. 프로젝트 장의 Github에 새 repository를 등록한 후 진행한다.

     2. 프로젝트 참여자에게 권한을 부여한다. 

     3. `remote add origin <저장소>`를 사용하여 같은 저장소를 사용한다.



     - **같은 Branch** 일 경우

        - 동시에 같은 라인의 코드를 수정했을 경우 : 충돌이 발생한다.   
         따라서, Pull 을 했을 때 최종적으로 사용할 코드를 선택한다.

         - 동시에 다른 라인의 코드를 수정했을 경우 : 두 코드가 동시에 입력 될 수 있으므로 서로가 작업한 코드를 비교, 분석하여 한 사람의 코드만 남길지, 아니면 두 코드 모두 사용할 지 선택한다.

     - **다른 Branch** 일 경우

        - 다른 Branch에 각각 코드 수정을 할 수 있으며, main과 합병하기 전까지는 충돌이 일어나지 않는다.

        - Github에서 Pull request 를 통하여 main에 합병할 Branch를 비교하여 선택하여 합병할 수 있다.


## 타인의 소스 코드 사용하기

- 타인의 소스 코드를 사용할 경우
    - 타인의 소스 코드를 Github에서 Fork 하여, 본인의 Github로 불러온다.
