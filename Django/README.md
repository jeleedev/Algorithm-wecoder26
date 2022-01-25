# Django(ORM)
- [select_related, prefetch_related를 특징](#%EF%B8%8F-select_related-prefetch_related의-특징)
- [select_related, prefetch_related를 사용하는 이유](#%EF%B8%8F-select_related-prefetch_related를-사용하는-이유)
- [N+1 문제가 무엇인지](#%EF%B8%8F-n+1-문제가-무엇인지)
- [ORM 최적화란?](#%EF%B8%8F-orm-최적화란?)
- [ORM의 쓰는 이유와 장점](#%EF%B8%8F-orm의-쓰는-이유와-장점)
- [select_related, prefetch_related를 언제 사용하는지](#%EF%B8%8F-select_relate,-prefetch_related를-언제-사용하는지)
- [Offset 기반 Pagination](#%EF%B8%8F-Offset-기반-Pagination)
- [Cursor 기반 Pagination](#%EF%B8%8F-Cursor-기반-Pagination)

<br>

## 💡️ select_related, prefetch_related의 특징
- select_related, prefetch_related, prefetch_related 모두 N+1 문제를 해결하기 위해 사용한다.

-  select_related은 정참조일 때 사용하는데 JOIN을 통해 데이터를 즉시 로딩한다. 또한 이 결과를 캐쉬에 저장시킨다.

- prefetch_related는 역참조 일 때 사용하는데 추가 쿼리 셋을 이용해 데이터를 가져와 애플리케이션 단에서 모두 합쳐 반환한다.

- 특히, prefetch_related는 result_cash에 캐쉬로 데이터가 담기는데, 기존 query를 보내고, 추가로 역참조에 대한 prefetch_related를 보내 이를 최종적으로 합쳐주기 때문에 query가 1개 더 생기는 특징을 갖고 있다.

<br>

## 💡️ select_related, prefetch_related를 사용하는 이유
- ORM에서 N+1 문제를 해결하기 위해 사용하는 기법을 즉시 호출(EagerLoading)라 하는데, 지금 당장 사용하지 않을 데이터도 포함하여 미리 Query문을 가져오는 방식이다.

- 정참조 일 때는 select_related, 역참조일 때는 prefetch_related 사용하여 데이터를 미리 캐슁하는 방식으로 N+1 문제를 해결한다.

<br>

## 💡️ N+1 문제가 무엇인지

- N+1 문제란 Lazy-Loading의 성능 이슈로 외래키를 참조해서 데이터를 참조해서 데이터를 가져올 때, 발생한다.

- Publish와 Book 테이블이 있고, Book 테이블의 user 필드가 Publish 테이블을 정참조하고 있다고 가정해 보자.
```python
# Publish 테이블
class Publish(TimeStampModel):
    name               = models.CharField(max_length=30)
# Book 테이블    
class Board(TimeStampModel):
    name               = models.CharField(max_length=100)
    description        = models.TextField()
    publisher          = models.ForeignKey('Publish', on_delete=models.CASCADE)
```

- Book에 대한 목록을 반환하는 API를 만든다고 가정 할 때, get 매서드는 아래와 같은 로직을 가진다.
```python
class BookListView(View):
    def get(self, request):
        result = []
        queryset = Book.objects.all()
        for book in queryset:
            books.append({
                'id':book.id,
                'name':book.name,
                'publish':book.publisher.name, # 참조하는 테이블에 접근할 때, 이미 캐싱되있지 않아 query 발생(N+1 문제)
            })
        return JsonResponse({"message": result}, status=200)
```

- 하나의 book 객체의 publish 필드를 통해 Publish 테이블로 이동해 name값을 가져오려는 순간 N+1의 문제가 발생된다.

-  여기서 for문이 순회하는 횟수가 N이 되기 때문에 데이터가 많을 수록 엄청난 양의 query가 발생한다.

<br>

## 💡️ ORM 최적화란?

- Django뿐 아니라 다른 ORM에서도 Lazy-loading방식을 사용한다. Lazy Loading은 CS 전반의 개념으로 generator의 개념과 유사하다.

- Lazy-loading이란 ORM에서 명령을 실행할 때마다 DB에 접근하여 데이터를 가져오는 것이 아닌 실제 데이터를 불러와야할 때, 즉 Query문이 평가되어야하는 시점에 Query문을 실행하여 DB에 데이터를 가져오는 방식이다.

- DB에 요청하는 Query문을 매번 실행시켜 DB에 무리를 주는 방식이 아닌, 최종적으로 Query문이 평가되어야할 때 DB에 요청하기 때문에 게으른 방식이라 얘기한다.

- 문제는 다른 테이블을 정참조하거나 역참조하면서 데이터를 불러올 때, 위에서 설명한 N+1 문제가 발생해서 수많은 Query가 일으킨다.

- 이에 미리 Query를 캐싱해둠으로써 DB에 불필요한 질의를 발생시키지 않는 방법인 EagerLoading을 사용한다.

- 이런 방식을 이용해 쿼리 최적화를 하는 이유는 비용 감소와 서비스의 질을 높히기 위해서 데이터를 빠르게 가져와야하기 때문이다.

- 모든 병목은 DB에서 발생하고, 서비스를 많은 이용자가 사용할 수록 데이터를 가져오는 속도에 서비스의 질이 큰 영향을 미치기 때문에 ORM 최적화는 필수이다.

<br>

## 💡 ORM의 쓰는 이유와 장점
> SQL 대신 ORM을 사용하면, 객체지향적인 코드 인해 더 직관적이고 로직에 집중할 수 있도록 도와줍니다. 또한 선언문, 할당, 종료 같은 부수적인 코드가 없거나 줄어들이 때문에 가독성이 높고 생산성이 증가합니다. 특히, ORM을 사용하면, DBMS에 대한 종속성이 줄어들기 때문에 재사용 및 유지보수에 용이합니다.


### 추가적인 내용 기술
- ORM을 사용하면 SQL문이 아닌 클래스의 메서드를 통해 DB를 조작할 수 있어, 객체 모델만 이용해서 프로그래밍을 하는데 집중할 수 있게 합니다. 

- 또한 SQL문은 절차적/순차적 접근이 혼재되어있지만, ORM은 객체지향적 접근만 고려하면 되기 때문에 생산성이 증가합니다. 

- 특히, SQL문에 선언문, 할당, 종료 같은 부수적인 코드로 문법이 장황하고 복잡한데 비해, ORM은 가독성이 높아 편리성, 유지보수에 용이합니다. 

- 뿐만아니라 프레임워크에서 ORM을 사용하면, 해당 DB에 대한 종속성을 낮출 수 있기 때문에 DBMS를 교체하는데 리스크가 적고 RDBMS의 데이터 구조와 객체지향 모델 사이의 간격을 좁힐 수 있습니다.

- 다만, ORM만으로 모든걸 해결할 순 없습니다. 프로젝트가 커지고, Query가 복잡해질 수록 ORM만을 의존하게되면 속도의 저하가 발생하게 됩니다. 일부 사용되는 대형 Qeury는 속도를 위해 별도의 SQL문을 작성해야할 수 있습니다.

<br>

## 💡️ select_related, prefetch_related를 언제 사용하는지
> 정참조일 때는 select_related를 사용하고, 역참조일 때는 prefetch_related 사용합니다.

### 추가적인 내용 기술
- 각각의 쿼리셋은 DB에 접근 할 때 캐시 메모리를 포함하고 있습니다. 처음 쿼리셋이 요청될 때, 캐시가 비었기 때문에 Query가 발생합니다. 그 이후 동일한 쿼리셋을 사용할 경우 추가적인 Query는 발생하지 않고, 캐시에서 꺼내서 사용하게 됩니다.

- select_related 와 prefetch_related는 모두 QuerySet을 DB에 요청할 때, 미리 related objects들까지 지정해서 불러오는 함수입니다. 

- 이렇게 미리 가져온 data들은 모두 cache에 남아있게 되므로 다시 DB에 접근해야 하는 문제를 덜어주고, N+1 문제를 해결합니다.

- select_related와 prefetch_related는 DB에 요청되는 Query 수를 줄여, performance를 향상시켜준다는 측면에서는 공통점이 있지만, 그 방식에는 차이점이 있습니다.

- select_related는 정참조(foreign-key, OneTonOneFeild) 관계인 모델의 objects들까지 미리 Query를 요청하는 방식입니다.

- prefetch_related는 쿼리셋을 반환할 때 foreign-key, OneTonOneFeild 관계뿐만 아니라 ManyToMany, ManyToOne 관계의 모델들을 함께 가져오는 방식입니다.

- 또한 select_related 는 INNER JOIN 으로 쿼리셋을 가져오고, prefetch_related 는 모델 별로 쿼리를 실행해 최종 쿼리셋을 합쳐 가져오기 때문에 1개의 추가 Query가 발생합니다.

- 이에 일반적으로 정참조에서는 select_related, 역참조에서는 prefetch_related를 사용합니다.

<br>

## 💡️ Offset 기반 Pagination
> offset-based-pagination은 건너띌 row의 수를 offset으로한 뒤 제한할 row의 수를 limit으로 하여 데이터를 pagination하는 기법입니다. offset-based-pagination는 구현이 쉽고 직관적이며, 네트워크 자원을 효율적으로 사용하기 위한 방법으로 전통적으로 사용되어왔습니다.

### 추가적인 내용 기술
- offset-base-pagination는 OFFSET 값을 포함한 SQL 쿼리문을 동반하는데, OFFSET은 row를 건너띌 시작점이고, LIMIT은 제한할 row의 수를 의미합니다.
- offset-base-pagination의 단점은 데이터가 잦은 수정이 발생되는 경우, 데이터 중복 또는 누락 issue가 발생한다는 점입니다.
- 또한 offset-base-pagination은 성능 issue가 존재합니다. 정렬기준에 대해 지정된 OFFSET까지 모두 만들어 놓은 후 LIMIT에 지정한 갯수를 자르는 방식이기 때문에 데이터가 많아질 수록 속도가 느려질 수 밖에 없tmqslek.
![](https://images.velog.io/images/jewon119/post/2e9d6600-bc2d-447e-8b4e-c024433721c0/offset-skip-take.png)

<br>

## 💡️ Cursor 기반 Pagination
> cursor-based pagination은 cursor 개념을 사용하여 사용자에게 응답해준 마지막 데이터 기준으로 다음 n개 응답하는 방식입니다. 즉, n개의 row를 skip 한 다음 10개 주세요가 아니라, 이 row 다음꺼부터 10개 주세요를 요청하는 방식입니다. 이에 cursor-based pagination은 실무에서 주로 사용되며 데이터가 잦은 수정이 반복되더라도 누락 및 중복 이슈가 없고, 빠르다는 장점이 있습니다.

### 추가적인 내용 기술
- cursor-based pagination은 offset based pagination의 단점을 보완하기 위해 실무에서 사용하는 pagination 기법입니다.
- cursor-based pagination은 SQL문에 WHERE절이 필요하고, 중복된 데이터가 존재할 가능성이 있다면 OR절을 추가해서 중복되지 않는 row를 계속 기준 잡을 수 있게 해주어야 합니다.
- OR절이 필요한 이유는 create_at 등을 통해 생성된 날짜로 정렬한 뒤, pagination 했을 때, 동시에 생성된 데이터가 존재한다면 그 시간에 생성된 1개의 row를 제외하고 무시될 수 있기 때문입니다.
![](https://images.velog.io/images/jewon119/post/3b9845b8-80ec-46e6-aceb-232bc0aa89da/cursor-3.png)

<br>