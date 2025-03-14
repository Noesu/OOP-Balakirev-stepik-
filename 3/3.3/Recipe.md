Объявите класс **Recipe** для представления рецептов. Отдельные ингредиенты рецепта должны определяться классом **Ingredient**. Объекты этих классов должны создаваться командами:
```python
ing = Ingredient(name, volume, measure)
recipe = Recipe()
recipe = Recipe(ing_1, ing_2,..., ing_N)
```
где _ing_1, ing_2,..., ing_N_ - объекты класса **Ingredient**.

В каждом объекте класса **Ingredient** должны создаваться локальные атрибуты:

_name_ - название ингредиента (строка);  
_volume_ - объем ингредиента в рецепте (вещественное число);  
_measure_ - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.; 

С объектами класса **Ingredient** должна работать функция:

_str(ing)_  # название: объем, ед. изм.

и возвращать строковое представление объекта в формате:

"название: объем, ед. изм."

Например:

```python
ing = Ingredient("Соль", 1, "столовая ложка")
s = str(ing) # Соль: 1, столовая ложка
```
Класс **Recipe** должен иметь следующие методы:

_add_ingredient(ing)_ - добавление нового ингредиента _ing_ (объект класса **Ingredient**) в рецепт (в конец);  
_remove_ingredient(ing)_ - удаление ингредиента по объекту _ing_ (объект класса **Ingredient**) из рецепта;  
_get_ingredients()_ - получение кортежа из объектов класса **Ingredient** текущего рецепта.

Также с объектами класса **Recipe** должна поддерживаться функция:

_len(recipe)_ - возвращает число ингредиентов в рецепте.

Пример использования классов (эти строчки в программе писать не нужно):
```python
recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3
```
P.S. На экран ничего выводить не нужно, только объявить классы.