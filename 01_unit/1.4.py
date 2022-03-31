## CSS-selectors AND searching by elements ##
'''
#moto - Поиск по ID
article - Поиск по tag
[title="one-thing"] - Поиск по attribute
[name="moto"] - Поиск по name
.lead - Поиск по class
'''
## 1.4-6
'''
http://suninjuly.github.io/cats.html.
article.text-muted.lead - Поиск по составному CSS-селектору
div.card-body - потомок для "div.col-sm-4"
p.card-text - дочерний элемент для "div.card-body"
div.card - родитель для "div.card-body"
'''
## 1.4-7
'''
Задание: поиск потомка
Откройте страницу http://suninjuly.github.io/cats.html. Откройте консоль разработчика и вкладку Elements в ней. 
Напишите минимально достаточный CSS-селектор, который найдет элемент с картинкой серьезного кота (Serious cat). 
Для поиска подходящего элемента в каталоге картинок используйте родительский элемент div.col-sm-4 
вместе с псевдо-классом :nth-child(n), чтобы выбрать n-й по счету элемент, а также селектор для картинки по тегу img.

div.col-sm-4:nth-child(2) img
'''
## 1.4-8
'''
Отметьте те селекторы, которые позволят найти только элемент с текстом "Lenin cat" 
на странице http://suninjuly.github.io/cats.html. 

.col-sm-4:nth-child(3) p
#politic
[data-name="Vladimir"]
'''
## 1.4-9
'''
Отметьте только те уникальные селекторы, которые позволят найти элемент, содержащий текст "Lenin cat" 
на странице http://suninjuly.github.io/cats.html

.lenin-cat
.card-text.lenin-cat
'''
## XPATH ##
'''
CSS-селекторы: сlass, id или name — лучше использовать их вместо поиска по XPath
XPath запрос всегда начинается с символа / или //
1. Символ / аналогичен символу > в CSS-селекторе, а символ // — пробелу.
el1/el2 — выбирает элементы el2, являющиеся прямыми потомками el1;
el1//el2 — выбирает элементы el2, являющиеся потомками el1 любой степени вложенности.
2.  Символ [ ] — это команда фильтрации
по любому атрибуту - //img[@id='bullet'] - 
по порядковому номеру - //div[@class="row"]/div[2] - вторая по порядку карточка
по полному совпадению текста - //p[text()="Lenin cat"] 
по частичному совпадению текста (функция contains) - //p[contains(text(), "cat")]
                                                     //div[contains(@class, "navbar")] 
можно использовать булевы операции (and, or, not) 
3. Символ * — команда выбора всех элементов
4. Поиск по классу в XPath регистрозависим
'''
## 1.4-11
'''
http://suninjuly.github.io/xpath_examples
8 одинаковых кнопок. Подберите такой XPath-селектор, чтобы выбрать только кнопку с текстом Gold

//button[contains(text(), "Gold")]
'''
