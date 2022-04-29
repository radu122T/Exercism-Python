# Instructions
# Given an age in seconds, calculate how old someone would be on:

# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Earth: orbital period 1.0 Earth years, 365.25 Earth days, or 31557600 seconds
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you were told someone were 1,000,000,000 seconds old, you should be able to say that they're 31.69 Earth-years old.

# If you're wondering why Pluto didn't make the cut, go watch this youtube video.

class SpaceAge:
    def __init__(self, seconds):
        self.years = seconds / 60/ 60 /24 /365.25
    
    def on_earth(self):
        return round(self.years,2)
    def on_mercury(self):
        return round(self.years/0.2408467,2)
    def on_venus(self):
        return round(self.years/0.61519726,2)
    
    def on_mars(self):
        return round(self.years/1.8808158,2)
    def on_jupiter(self):
        return round(self.years/11.862615,2)
    def on_saturn(self):
        return round(self.years/29.447498,2)
    def on_uranus(self):
        return round(self.years/84.016846,2)
    
    def on_neptune(self):
        return round(self.years/164.79132,2)

        