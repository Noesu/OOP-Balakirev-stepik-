Необходимо объявить класс-декоратор с именем **HandlerGET**, который будет имитировать обработку GET-запросов на стороне сервера. Для этого сам класс **HandlerGET** нужно оформить так, чтобы его можно было применять к любой функции как декоратор. Например:

```python
@HandlerGET
def contact(request):
    return "Сергей Балакирев"
```

Здесь _request_ - это произвольный словарь с данными текущего запроса, например, такой: _{"method": "GET", "url": "contact.html"}_.  
А функция должна возвращать строку.

Затем, при вызове декорированной функции:

`res = contact({"method": "GET", "url": "contact.html"})`

должна возвращаться строка в формате:

`"GET: <данные из функции>"`

В нашем примере - это будет:

`"GET: Сергей Балакирев"`

Если ключ _method_ в словаре _request_ отсутствует, то по умолчанию подразумевается GET-запрос. Если же ключ _method_ принимает другое значение, например, _"POST"_, то декорированная функция _contact_ должна возвращать значение _None_.

Для реализации имитации GET-запроса в классе **HandlerGET** следует объявить вспомогательный метод со следующей сигнатурой:

```python
def get(self, func, request, *args, **kwargs): ...
```

Здесь _func_ - ссылка на декорируемую функцию;  
_request_ - словарь с переданными данными при вызове декорированной функции.  
Именно в этом методе следует формировать возвращаемую строку в указанном формате:

`"GET: Сергей Балакирев"`

P.S. В программе достаточно объявить только класс. Ничего на экран выводить не нужно.