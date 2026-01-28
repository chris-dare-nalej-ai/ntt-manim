from manim import *


class TitleScene(Scene):
    def construct(self):
        # Create the title text
        title = Text("The Number Theoretic Transform", font_size=48)
        
        # Animate the title appearing
        self.play(Write(title), run_time=2)
        
        # Wait for 2 seconds
        self.wait(2)
        
        # Fade out
        self.play(FadeOut(title))
