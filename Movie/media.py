import webbrowser

'''This DocString explains that this is a class named movie_info'''


class movie_info():
    '''This DocString is the constructor which initialize the instance and
     here we are also initializing instance variables'''

    def __init__(self, title, Storyline, poster_url, trailer_youtube_url):
        self.title = title
        self.storyline = Storyline
        self.poster = poster_url
        self.trailer = trailer_youtube_url

    '''This DocString is the instance method,this method is called by  instance
       that has been created for this class'''

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
