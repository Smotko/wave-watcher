class Weather(object):

  def __init__(self, **kw):
    self.__dict__.update(kw)

  def is_strong_jugo(self):
    return self.windDirection > 112.5 and\
        self.windDirection < 225.5 and\
        self.windSpeed > 5.5
