from django.shortcuts import render
import requests
apiKey = "7e8288518047419c9336d20c62a9f9b2"


# Create your views here.
def index(request):

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={apiKey}"
    response = requests.get(url)
    data = response.json()
    firstHeadline = data['articles'][0:1]
    headlines = data['articles'][1:4]
    rightContentHeadline = data['articles'][4:8]

    url2 = f"https://newsapi.org/v2/everything?q=apple&from=2022-10-23&to=2022-10-23&sortBy=popularity&apiKey={apiKey}"
    response2 = requests.get(url2)
    data2 = response2.json()
    weeklyTop = data2['articles'][0:5]
    weeklyTopSecond = data2['articles'][5:10]
    # print('weekyTopSecond', weeklyTopSecond)

    # get top articles
    url3 = f"https://newsapi.org/v2/top-headlines/sources?apiKey={apiKey}"

    context = {
        'headlines': headlines,
        'firstHeadline': firstHeadline,
        'rightContentHeadline': rightContentHeadline,
        'weeklyTopNews': weeklyTop,
        'weeklyTopSecond': weeklyTopSecond,
    }
    return render(request, 'newsFeed/index.html', context)


def about(request):
    return render(request, 'newsFeed/about.html')


def contact(request):
    return render(request, 'newsFeed/contact.html')


def blog(request):
    return render(request, 'newsFeed/blog.html')


def category(request):
    return render(request, 'newsFeed/category.html')


def latestNews(request):
    return render(request, 'newsFeed/latest_news.html')