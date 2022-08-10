from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .models import Profile, Video, Movie, CustomUser
from .forms import ProfileForm


# Create your views here.



def index(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    return render(request, 'index.html') 



@login_required
def profile_list(request):
    profiles = request.user.profiles.all()

    context = {'profiles': profiles}
    return render(request, 'profile_list.html', context)


@login_required
def profile_create(request):
    if request.method == 'GET':
        profiles = request.user.profiles.all()
        form = ProfileForm()
        context = {
            'form': form,
            'profiles': profiles
        }
        return render(request, 'profile_create.html', context)
    
    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            profile = Profile(**form.cleaned_data)
            profile.save()
            if profile:
                request.user.profiles.add(profile)
            return redirect('/profile/')
        context = {
            'form': form, 
            'profiles': profiles
        }
        return render(request, 'profile_create.html', context)


@login_required
def watch(request, pk):
    try:
        profile = Profile.objects.get(uuid=pk)
        movies = Movie.objects.filter(age_limit=profile.age_limit)

        if profile not in request.user.profiles.all():
            return redirect('/profile/')
        else:
            context = {
                'movies': movies
            }
            return render(request, 'movie_list.html', context)

    except Profile.DoesNotExist:
        return redirect('/profile/')


@login_required
def show_movie_detail(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(uuid=pk)
            context = {
                'movie': movie
            }
            return render(request, 'movie_detail.html', context)
        except Movie.DoesNotExist:
            # return redirect('/profile/')
            return render(request, 'movie_detail.html')



@login_required
def show_movie(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(uuid=pk)
            movie_videos = movie.videos.values()
            context = {
                'movie_videos': list(movie_videos)
            }
            return render(request, 'show_movie.html', context)
        except Movie.DoesNotExist:
            # return redirect('/profile/')
            return render(request, 'show_movie.html')

