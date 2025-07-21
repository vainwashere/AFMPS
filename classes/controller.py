from classes.game_state import GameState
from typing import Optional
# Controller

state_map = {
    
    'partial_menu':'classes.partial_menu.PartialMenu',
    'menu': 'classes.menu.Menu'
}


class Controller:
    def __init__(self, main_state: str) -> None:
        if not isinstance(main_state, str):
            raise TypeError
        self.breakloop = False
        self.current_state_key: str
        self.current_state: GameState
        self.LOADED_STATES : dict = {}
        self.go_to(main_state) 

    def fetch_state(self, state_name: str) -> Optional[GameState]:
        if state_name in self.LOADED_STATES:
            return self.LOADED_STATES[state_name]
        else:
            try:
                s = self.import_state(state_map[state_name])
                self.LOADED_STATES[state_name] = s
                return s
            except Exception as e: #modulenotfounderror
                print(e)

    def import_state(self, sts: str) -> GameState:
        print("attempting import...")
        parts = sts.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)    
        print(m)        
        return m()

    def go_to(self, next_state_str: str):
        next_state = self.fetch_state(next_state_str)
        print(next_state)
        self.dump()
        self.current_state = next_state #type:ignore #fix these later.
        self.current_state.CONTROLLER = self #type:ignore
        self.current_state_key = next_state_str
        self.breakloop = True
        
    
    # dump the current state's data.
    def dump(self) -> None:
        try:
            self.LOADED_STATES[self.current_state_key] = self.current_state
        except Exception as e:
            print(e)
            print("dump exeption^^")