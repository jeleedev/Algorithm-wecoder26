# Django(ORM)
- [select_related, prefetch_related를 특징](#%EF%B8%8F-select_related-prefetch_related의-특징)
- [select_related, prefetch_related를 사용하는 이유](#%EF%B8%8F-select_related-prefetch_related를-사용하는-이유)
- [N+1 문제가 무엇인지](#%EF%B8%8F-n+1-문제가-무엇인지)
- [ORM 최적화란?](#%EF%B8%8F-orm-최적화란?)


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