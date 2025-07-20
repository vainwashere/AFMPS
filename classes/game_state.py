import pygame as pg
class GameState:
    def __init__(self, *args, **kwargs): #Can also pass constructor data.
        pass

    # Code to run when the GameState is called into the game for the first time. "First time" here is not persistent - 
    # if the state is flipped with another one and called again, this code runs again. It can be used, for example, to play some audio or display a transition effect when this state is called onto the program.
    def start(self, *args, **kwargs):
        pass

    # Extratenous method for setting up some important things that can't be handled in the init function.
    # This is defined after start, as it is usually called by the start function itself.
    def boot(self, *args, **kwargs):
        pass


    def handle_events(self, events):
        pass

    def update(self): # Game logic related proccessing is done here.
        pass

    #Draws graphics on the screen.
    # N.B. some Classes may require *args and **kwargs for this function, or really any other function.
    def draw(self, screen):
        pass

    # tick the clock and get the value of time_delta, used for the UI_MANAGER to update ui elements.
    def tick(self):
        pass

    # This function is called before switching to the next state - but it **does not** actually switch the state.
    # This function is meant to be called before **actually** switching over to the next state, to perform a *clean* exit.
    def clean_up(self):
        pass

    def close(self):
        pass