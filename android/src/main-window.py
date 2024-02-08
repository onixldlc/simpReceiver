from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (1080/2.5 ,2340/2.5)


layout = """
MDScreen:
    name: "screen1"
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            type: "small"

            MDTopAppBarLeadingButtonContainer:
                
                MDActionTopAppBarButton:
                    icon: "menu"
            
            MDTopAppBarTitle:
                text: "AppBar Center-aligned"
                pos_hint: {"center_x": .5}

        MDLabel:
            text: 'Hello World'
            halign: 'center'
"""

class Demo(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.theme_style = "Teal"
        return Builder.load_string(layout)
        # screen = Builder.load_string(layout)
        # return screen
    
    # def on_start(self):
    #     super().on_start()
    #     self.fps_monitor_start()

    def on_touch_move(self, touch):
        print(touch)
        # if touch.grab_current is not self:
        #     return
        # ud = touch.ud
        # ud['lines'][0].pos = touch.x, 0
        # ud['lines'][1].pos = 0, touch.y
    
Demo().run()