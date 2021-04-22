#diese funktion ist nur da, um es "nah am MatLabCode" zu halten
import Parameter
import units

def initialize():
    pm = Parameter.Parameter()  #Parameter werden initialisiert (in Parameter.py)
    us =units.units(pm)           #noch units initialiseren
    return (pm,us)

    #als Rückgabewert noch Parameter und units zurückgeben