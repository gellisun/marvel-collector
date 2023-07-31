from django.shortcuts import render

comics = [
    {'name': 'The Amazing Spider-Man (2018) #1', 'published': '2018-07-11', 'writer': 'Nick Spencer', 'penciler': 'Ryan Ottley, Humberto Ramos', 'cover': 'Ryan Ottley', 'img_url': 'https://i.imgur.com/GHZZCPh.png'},
    {'name': 'Avengers (2018) #1', 'published': '2018-05-02', 'writer': 'Jason Aaron', 'penciler': 'Ed Mcguinness', 'cover': 'Ed Mcguinness', 'img_url': 'https://i.imgur.com/q2eR88c.png'},
    {'name': 'Black Widow (2014)) #1', 'published': '2014-01-08', 'writer': 'Nathan Edmonson', 'penciler': '', 'cover': 'Philip J. Noto', 'img_url': 'https://i.imgur.com/4O2dsEo.png'},
    {'name': 'Vision (2015) #1', 'published': '2015-11-04', 'writer': 'Tom King', 'penciler': '', 'cover': 'Mike Del Mundo', 'img_url': 'https://i.imgur.com/FjoFUKn.png'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def comics_index(request):
    return render(request, 'comics/index.html', {'comics': comics})
