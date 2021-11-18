## 금융 서비스
> 어느날 문득 결제 관련 기능들을 만들어보고 싶다는 생각을 했다.
>
> 그래서 만들어 보고자 토스를 생각하며 만들어보기로 했다.
> 
> 물론 금융에 대해서 잘 알지 못하지만 시도해서 나쁠건 없다고 생각하며 시작한 프로젝트이다.

toss app의 flow를 살펴보며 만들어 볼 예정이다.

---

### OS

- mac

### version

- python 3.8.5
- django 3.2.9

### 가상환경

- venv

### database

- mysql

### git-flow 전략

- master : 실서버를 바라보고 제품으로 출시될 수 있는 브랜치
- develop : 신규 기능 개발을 테스트하는 브랜치
- feature : 각 기능을 개발할 수 있는 브랜치
- hotfix : 버그 발생시 수정하는 브랜치

#### 작업시 주의 사항

> 혼자 작업할거지만 그래도 계속 숙지하면서 작업하면 이후 협업에 도움이 많이 될듯하다.

- 자신이 만든 feature 브랜치가 pull request가 되었을때 반드시 제거한다.
- 커밋 메세지는 최대한 단순하고 알기 쉽게 작성한다.