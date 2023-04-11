from django.shortcuts import render
import requests

def music_search(request):
    return render(request, 'music_search.html')

def search_results(request):
    search_term = request.GET.get('term')
    url = f'https://itunes.apple.com/search?term={search_term}&media=music&entity=album'
    response = requests.get(url)
    data = response.json()
    return render(request, 'search_results.html', {'data': data})
