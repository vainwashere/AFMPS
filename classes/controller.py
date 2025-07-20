from classes.game_state import GameState
# Controller

class Controller:
    def __init__(self, main_state: GameState):
        if not isinstance(main_state, GameState):
            raise TypeError
        self.LOADED_STATES = {'main':main_state} #state names should be as short as possible.
        self.go_to(main_state)

    def get_state(self, state_name):
        if 

    def get_state(self, sts):
        parts = sts.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)            
        return m

    def go_to(self, next_state):
        self.current_state = next_state
        # self.current_state.ui_manager = pg_g.UIManager((screen_res), screen)
        # By design: All States have the responsibility to define their own UIManager.
        # This is done as some states may not even have the need for a UIManager. In any case, the UIManager will
        # be called to draw if it exists in the state's draw() function, otherwise not.
        self.current_state.CONTROLLER = self
        # This is a bit tricky. This is one of the reasons why the boot function exists - The CONTROLLER constant, by design, will be assigned after the state has already come into existence (and after its own innit function has ran). This is why the boot function is needed.
