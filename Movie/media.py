import webbrowser

'''This DocString explains that this is a class named movie_info'''


class Movie():
    '''This DocString This is the class says about my fav movies
     And here we are also initilizing instance variables'''

    def __init__(self, title, storyline, poster_url, trailer_youtube_url):
        '''Here we are initilizing the movie attributes using constructor'''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_youtube_url

    '''This DocString is the instance method,this method is called by  instance
       that has been created for this class'''

    def show_trailer(self):
        '''This function Opens the youtube trailer'''
        webbrowser.open(self.trailer_youtube_url)
