import os, random
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def home(request):
    return render(request, 'contest/home.html')


def select_gender(request):
    return render(request, 'contest/select_gender.html')

def select_ethnicity(request, gender):
    return render(request, 'contest/select_ethnicity.html', {'gender': gender})

def compare_faces(request, folder):
    img_dir = os.path.join(settings.BASE_DIR, f'members/static/images/{folder}')
    images = os.listdir(img_dir)
    pool_a = random.sample(images, len(images)//2)
    pool_b = list(set(images) - set(pool_a))
    img_a = random.choice(pool_a)
    img_b = random.choice(pool_b)
    return render(request, 'contest/compare.html', {
        'img_a': img_a,
        'img_b': img_b,
        'folder': folder
    })


def compare_movies(request):
    img_dir = os.path.join(settings.BASE_DIR, 'members/static/images/movies')
    images = os.listdir(img_dir)
    pool_a = random.sample(images, len(images)//2)
    pool_b = list(set(images) - set(pool_a))
    img_a = random.choice(pool_a)
    img_b = random.choice(pool_b)
    return render(request, 'contest/compare.html', {
        'img_a': img_a,
        'img_b': img_b,
        'folder': 'movies'
    })

def compare_places(request):
    img_dir = os.path.join(settings.BASE_DIR, 'members/static/images/places')
    images = os.listdir(img_dir)
    pool_a = random.sample(images, len(images)//2)
    pool_b = list(set(images) - set(pool_a))
    img_a = random.choice(pool_a)
    img_b = random.choice(pool_b)
    return render(request, 'contest/compare.html', {
        'img_a': img_a,
        'img_b': img_b,
        'folder': 'places'
    })


def vote(request):
    if request.method == 'POST':
        folder = request.POST.get('folder')
        winner = request.POST.get('winner')
        img_dir = os.path.join(settings.BASE_DIR, f'members/static/images/{folder}')
        images = os.listdir(img_dir)
        pool_a = random.sample(images, len(images)//2)
        pool_b = list(set(images) - set(pool_a))
        new_img = random.choice(pool_b if winner == 'img_a' else pool_a)
        return JsonResponse({'new_image': new_img})
