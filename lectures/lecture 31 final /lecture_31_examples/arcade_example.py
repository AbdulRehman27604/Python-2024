import arcade

'''
To install arcade, run the following lines in your Python Shell:

import pip
pip.main(['install', 'arcade'])

or from your command line:
pip install arcade

Intro Tutorial:    https://realpython.com/arcade-python-game-framework/
Further Tutorials: https://api.arcade.academy/en/latest/get_started.html
Examples:          https://api.arcade.academy/en/latest/examples/index.html
'''

SCREEN_TITLE = 'Example'
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,
                         SCREEN_TITLE, resizable=False)
        
        self.planets = [{"x": 250, "y": 250, "size": 50},
                        {"x": 100, "y": 400, "size": 25},
                        {"x": 400, "y": 100, "size": 25}]
        
        self.new_size = 25
        
        
    def setup(self) -> None:
        """
        Set up the game.
        """
        arcade.set_background_color(arcade.color.BLACK)
    
    
    def on_draw(self) -> None:
        """
        Render stuff on the screen.
        """
        self.clear()
        
        # Draw the planets
        for planet in self.planets:
            arcade.draw_circle_filled(planet['x'], 
                                      planet['y'], 
                                      planet['size'], 
                                      (255, 255, 0))
            
        # Draw some text onto the screen.
        arcade.draw_text(f'New planet size: {self.new_size}', 10, 25)
        arcade.draw_text(f'Press + or - to change size.', 10, 10)
        arcade.draw_text(f'Press r to remove the last planet added.', 250, 10)
        
        
    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        if self.new_size < 100 and \
           (key == arcade.key.EQUAL or key == arcade.key.PLUS):
            self.new_size += 5
            
        elif self.new_size > 5 and key == arcade.key.MINUS:
            self.new_size -= 5
            
        elif key == arcade.key.R and len(self.planets) > 0:
            self.planets.pop()
    
    
    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.planets.append({'x': x, 'y': y, 'size': self.new_size})


if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()
    
    
"""
You could extend this example by:
- Creating a class for Planet with x, y, and size.
- Loading planets from a text file, where data is stored as x,y,size, one 
  planet per line.
- Saving created planets to a text file. 
- Adding the ability to clear all of the planets.
- Adding the ability to change the colour of a newly added planet (and storing 
  colours inside of the Planet class, as red, green, and blue color values)
"""