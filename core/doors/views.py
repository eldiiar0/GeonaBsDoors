from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, SubCategory, DoorType, Door, News, Message
from .forms import MessageForm
from django.db.models import Q


def main(request):
	categories = Category.objects.all()
	news = News.objects.all()
	form = MessageForm()
	context = {'categories': categories, 'news': news, 'form': form}
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Ваше сообщение отправлено!')
			return redirect('doors:main')
		else:
			messages.success(request, 'Ошибка!')
			return redirect('doors:main')
	else:
		return render(request, 'doors/main.html', context)

	


def category(request, pk):
	category = Category.objects.get(id=pk)
	# description = category.description.split(':')
	# print(description)
	# print(dir(category))
	# print(category.subcategory_set)
	return render(request, 'doors/category.html', {'category': category})


def subcategory(request, pk):
	subcategory = SubCategory.objects.get(id=pk)
	return render(request, 'doors/subcategory.html', {'subcategory': subcategory})


def doortype(request, pk):
	doortype = DoorType.objects.get(id=pk)
	# doors = Door.objects.filter(doortype=doortype).values()[0]
	# print(doortype.door_set.all().first)
	# print(dir(doortype.door_set.all().first))
	# print(dir(doortype.door_set.first))
	return render(request, 'doors/doortype.html', {'doortype': doortype})


def catalog(request):
	categories = Category.objects.all()
	return render(request, 'doors/catalog.html', {'categories': categories})


def news_dtl(request, pk):
	news = News.objects.get(id=pk)
	return render(request, 'news/news_dtl.html', {'news': news})


def conf(request):
	return render(request, 'conf.html')



def search_doors(request):
	search_post = request.GET.get('search')
	results = DoorType.objects.filter(
			Q(title__icontains=search_post) | Q(description__icontains=search_post)|
			Q(title__istartswith=search_post)
		)	
	return render(request, 'doors/search_result.html', {'results': results, 'search':search_post})