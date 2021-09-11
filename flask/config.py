import os

class Config:
    '''
    General configuration parent class
    '''
    # MOVIE_API_KEY = 'c5c3ce0bad05b780c923dd51a93ff19a'
    
    SECRET_KEY = 'hfbsj67gkjSBjkbvk'
    
    
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key=c5c3ce0bad05b780c923dd51a93ff19a'
    



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
        
    '''
    
    
    pass



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}