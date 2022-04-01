## CSS-селекторы ##
'''
<!DOCTYPE html>
<html>
<body>
  <h1>Look at my favorite cat memes:</h1>
  <p>If there's one thing that the internet was made for, it's funny cat memes.</p>
  <div class = "column">
      <div class="card-body">
          <img class="picture" src="https://www.dailydot.com/wp-content/uploads/2018/10/olli-the-polite-cat.jpg">
          <h3 id="polite"> Polite cat </h3>
          <p data-type="description"> Nice cat </p>
      	  <div class="btn-group">
	          <button type="button" class="btn btn-sm">View</button>
	          <button type="button" class="btn btn-sm">Edit</button>
	      </div>
      </div>
      <div class="card-body">
          <img class="picture" src="https://i.kym-cdn.com/photos/images/newsfeed/001/328/469/2a0.jpg">
          <h3 id="banana"> Banana cat </h3>
          <div class="btn-group">
	          <button type="button" class="btn btn-sm">View</button>
	          <button type="button" class="btn btn-sm">Edit</button>
          </div>
      </div>
   <div class="card-body">
      <img class="picture" src="https://i.redd.it/vnpkq1rk31811.jpg">
      <h3 id="melon"> Watermelon cat </h3>
      <div class="btn-group">
	      <button type="button" class="btn btn-sm">View</button>
	      <button type="button" class="btn btn-sm">Edit</button>
	  </div>
   </div>
</div>
</body>
</html>
'''
## 1.5-2 ##
'''
Добавьте заголовку "Polite cat" синий цвет в файле CSS с помощью ID-селектора

#polite
{
    color:blue;
}
'''
## 1.5-3 ##
'''
Добавьте тексту с описанием карточки "Polite cat" синий цвет

.card-body:nth-child(1) p
{
    color:blue;
}
'''
## 1.5-4 ##
'''
Добавьте тексту в подзаголовке страницы синий цвет

p.text 
{
    color:blue;
}
'''
## 1.5-5 ##
'''
Текст "Watermelon story" стал синим

.card-body.watermelon:nth-child(3) p.description
{
    color:blue;
}
'''
## 1.5-6 ##
'''
Добавьте тексту "Cat doesn't like bananas!" синий цвет

.banana.card-body:nth-child(2) p
{
    color:blue;
}
'''
## 1.5-7 ##
'''
Текст кнопки "Edit" на карточке с бананом синий

[name="banana"] .btn.btn-sm:nth-child(2)
{
    color:blue;
}
'''