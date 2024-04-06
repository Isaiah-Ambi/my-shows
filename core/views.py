from django.shortcuts import render, redirect
from .models import Show, WatchListShow
import requests

# Create your views here.

def search(request):
    # query = request.GET.get('q')
    if request.method == 'POST':
        query = request.POST.get('search_query')
        url = f'https://api.tvmaze.com/search/shows?q={query}'
        response = requests.get(url)
        data = response.json()

        shows = []

        for show in data:
            shows.append({
                'name': show['show']['name'],
                'tvmaze_id': show['show']['id'],
                'image_url': show['show']['image']['medium'] if show['show']['image'] else 'No image',
                'summary': show['show']['summary'],
                'rating': show['show']['rating']['average'],
                'status': show['show']['status'],
                'genres': show['show']['genres'],
                'premiered': show['show']['premiered'],
            })
        context = {
            'results': shows
        }
        return render(request, 'core/search_results.html', context)
    return render(request, 'core/search.html')

# def search_results(request):
#     return render(request, 'search_results.html')

def add_show(request, id):
    try:
        show = Show.objects.get(tvmaze_id=id)
    except Show.DoesNotExist:
    # Show not found, create a new one
        url = f"https://api.tvmaze.com/shows/{id}"
        response = requests.get(url)
        show_data = response.json()
        show = Show.objects.create(
            tvmaze_id = show_data['id'],
            name = show_data['name'],
            genres = show_data['genres'],
            status = show_data['status'],
            image_url = show_data['image']['medium'] if show_data['image'] else 'No image',
            premiered = show_data['premiered'],
            rating = show_data['rating']['average'],
            summary = show_data['summary'],
        )

    try:
        watchlist_show = WatchListShow.objects.get(user=request.user, show=show)
        message = f"'{show.name}' show already exists in your watchlist."
    except WatchListShow.DoesNotExist:
            watchlist_show = WatchListShow.objects.create(
                user=request.user,
                show=show,
                watch_status="TO_WATCH",
            )
            message = f"'{show.name}' added to your watchlist."

            context = {
                'message': message,
            }
            return render(request, 'core/add_show_to_list.html', context)

    except requests.exceptions.RequestException as e:
        # Handle API errors ...
        return render(request, 'core/add_show_to_list.html', {'message': "Error retrieving show information. Please try again."})

    return redirect('search')

def watchlist(request):
    shows = WatchListShow.objects.filter(user=request.user)
    context = {'watchlist_shows': shows}

    return render(request, 'core/watchlist.html', context)
    