# Scene Manager
class SceneManager:
    def __init__(self, initial_scene, ui_manager_reference):
        self.ui_manager_reference = ui_manager_reference
        self.go_to(initial_scene)
    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
        self.scene.ui_manager = self.ui_manager_reference