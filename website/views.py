from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from django.http import JsonResponse
from django.db.models.aggregates import Count
from random import randint

from .models import *
from .forms import *


def home(request):
	items = Properties.objects.all().order_by('-id')
	items1 = None
	items2 = None
	items3 = None
	items4 = None

	searched = 'None'
	if request.method == 'POST':
		searched = request.POST.get('search')
		items = Properties.objects.filter(titre__icontains = searched)
		items1 = Properties.objects.filter(category__icontains = searched)
		items2 = Properties.objects.filter(description__icontains = searched)
		items3 = Properties.objects.filter(zone__icontains = searched)
		items4 = Properties.objects.filter(prix__icontains = searched)

		context = {
			'items': items,
			'items1': items1,
			'items2': items2,
			'items3': items3,
			'items4': items4
		}
		return render(request, 'website/search-results.html', context)

	context = {
		'items': items,
	}
	return render(request, 'website/index.html', context)

def contact(request):
	if request.method == 'POST':
		form = MessagesForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Votre message a été envoyé!')
			return redirect('contact')

	else:
		form = MessagesForm()
		return render(request, 'website/contact.html', {'form': form})

def favorites(request):
	return render(request, 'website/favorites.html')

def properties(request):
	items = Properties.objects.all().order_by('-id')
	items1 = None
	items2 = None
	items3 = None

	searched = 'None'
	if request.method == 'POST':
		searched = request.POST.get('search')
		items = Properties.objects.filter(titre__icontains = searched)
		items1 = Properties.objects.filter(category__icontains = searched)
		items2 = Properties.objects.filter(description__icontains = searched)
		items3 = Properties.objects.filter(zone__icontains = searched)

		context = {
			'items': items,
			'items1': items1,
			'items2': items2,
			'items3': items3
		}
		return render(request, 'website/search-results.html', context)

	context = {
		'items': items,
	}
	return render(request, 'website/properties.html', context)


def property(request, id):
	item = get_object_or_404(Properties, id=id)
	category = item.category
	count = Properties.objects.filter(category=category).aggregate(count=Count('id'))['count']
	range_one = randint(0, count - 1)
	range_two = randint(0, count - 1)
	range_three = randint(0, count - 1)
	similar = Properties.objects.filter(category=category)[range_one]
	similar1 = Properties.objects.filter(category=category)[range_two]
	similar2 = Properties.objects.filter(category=category)[range_three]

	context = {
		'object': item,
		'similar': similar,
		'similar1': similar1,
		'similar2': similar2,
	}

	return render(request, 'website/property-details.html', context)


def rent(request):
	items = Properties.objects.filter(mode__icontains = 'louer').order_by('-id')
	items1 = None
	items2 = None
	items3 = None

	searched = 'None'
	if request.method == 'POST':
		searched = request.POST.get('search')
		items = Properties.objects.filter(titre__icontains = searched)
		items1 = Properties.objects.filter(category__icontains = searched)
		items2 = Properties.objects.filter(description__icontains = searched)
		items3 = Properties.objects.filter(zone__icontains = searched)

		context = {
			'items': items,
			'items1': items1,
			'items2': items2,
			'items3': items3
		}
		return render(request, 'website/search-results.html', context)

	context = {
		'items': items,
	}
	return render(request, 'website/rent.html', context)


def buy(request):
	items = Properties.objects.filter(mode__icontains = 'vendre').order_by('-id')
	items1 = None
	items2 = None
	items3 = None

	searched = 'None'
	if request.method == 'POST':
		searched = request.POST.get('search')
		items = Properties.objects.filter(titre__icontains = searched)
		items1 = Properties.objects.filter(category__icontains = searched)
		items2 = Properties.objects.filter(description__icontains = searched)
		items3 = Properties.objects.filter(zone__icontains = searched)

		context = {
			'items': items,
			'items1': items1,
			'items2': items2,
			'items3': items3
		}
		return render(request, 'website/search-results.html', context)

	context = {
		'items': items,
	}
	return render(request, 'website/buy.html', context)


def appartments(request):
	items = Properties.objects.filter(category__icontains = 'appart').order_by('-id')
	items1 = None
	items2 = None
	items3 = None

	searched = 'None'
	if request.method == 'POST':
		searched = request.POST.get('search')
		items = Properties.objects.filter(titre__icontains = searched)
		items1 = Properties.objects.filter(category__icontains = searched)
		items2 = Properties.objects.filter(description__icontains = searched)
		items3 = Properties.objects.filter(zone__icontains = searched)

		context = {
			'items': items,
			'items1': items1,
			'items2': items2,
			'items3': items3
		}
		return render(request, 'website/search-results.html', context)

	context = {
		'items': items,
	}
	return render(request, 'website/properties.html', context)


def houses(request):
	items = Properties.objects.filter(category__icontains = 'maison').order_by('-id')
	items1 = None
	items2 = None
	items3 = None

	searched = 'None'
	if request.method == 'POST':
		searched = request.POST.get('search')
		items = Properties.objects.filter(titre__icontains = searched)
		items1 = Properties.objects.filter(category__icontains = searched)
		items2 = Properties.objects.filter(description__icontains = searched)
		items3 = Properties.objects.filter(zone__icontains = searched)

		context = {
			'items': items,
			'items1': items1,
			'items2': items2,
			'items3': items3
		}
		return render(request, 'website/search-results.html', context)

	context = {
		'items': items,
	}
	return render(request, 'website/properties.html', context)

def offices(request):
	items = Properties.objects.filter(category__icontains = 'bureau').order_by('-id')
	items1 = None
	items2 = None
	items3 = None

	searched = 'None'
	if request.method == 'POST':
		searched = request.POST.get('search')
		items = Properties.objects.filter(titre__icontains = searched)
		items1 = Properties.objects.filter(category__icontains = searched)
		items2 = Properties.objects.filter(description__icontains = searched)
		items3 = Properties.objects.filter(zone__icontains = searched)
		context = {
			'items': items,
			'items1': items1,
			'items2': items2,
			'items3': items3
		}
		return render(request, 'website/search-results.html', context)

	context = {
		'items': items,
	}
	return render(request, 'website/properties.html', context)

def terrains(request):
	items = Properties.objects.filter(category__icontains = 'terrain').order_by('-id')
	items1 = None
	items2 = None
	items3 = None

	searched = 'None'
	if request.method == 'POST':
		searched = request.POST.get('search')
		items = Properties.objects.filter(titre__icontains = searched)
		items1 = Properties.objects.filter(category__icontains = searched)
		items2 = Properties.objects.filter(description__icontains = searched)
		items3 = Properties.objects.filter(zone__icontains = searched)

		context = {
			'items': items,
			'items1': items1,
			'items2': items2,
			'items3': items3
		}
		return render(request, 'website/search-results.html', context)

	context = {
		'items': items,
	}
	return render(request, 'website/properties.html', context)


@login_required
def publish(request):
	if request.method == 'POST':
		form = PropertyForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('properties')

	else:
		form = PropertyForm()

	context = {
		'form': form,
	}

	return render(request, 'website/publish.html', context)
