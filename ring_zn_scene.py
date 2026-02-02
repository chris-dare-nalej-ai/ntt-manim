from manim import *


class RingZnScene(Scene):
    def construct(self):
        # Create the title with LaTeX
        title = MathTex(r"\text{The ring } \mathbb{Z}_n")
        title.to_edge(UP)
        
        # Create the subtitle showing the value of n
        n = 12  # Number of points in Z_n
        subtitle = MathTex(r"\text{(e.g. } n = " + str(n) + r"\text{)}", font_size=36)
        subtitle.to_edge(LEFT).shift(UP * 2.5)
        
        # Animate the title and subtitle
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        
        # Set up the circle parameters (5% smaller)
        radius = 2.375
        circle = Circle(radius=radius, color=BLUE, stroke_width=1.5, stroke_opacity=0.3)
        
        # Create points around the circle
        points = VGroup()
        labels = VGroup()
        
        for i in range(n):
            # Calculate angle for each point (starting from top, going clockwise)
            angle = -i * (2 * PI / n) + PI / 2
            
            # Create point position
            point_pos = radius * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Create dot
            dot = Dot(point_pos, color=YELLOW, radius=0.08)
            points.add(dot)
            
            # Create label
            label = MathTex(str(i), font_size=36)
            # Position label slightly outside the circle
            label_pos = (radius + 0.4) * np.array([np.cos(angle), np.sin(angle), 0])
            label.move_to(label_pos)
            labels.add(label)
        
        # Animate the circle appearing
        self.play(Create(circle))
        self.wait(0.5)
        
        # Animate points appearing
        self.play(LaggedStart(*[GrowFromCenter(dot) for dot in points], lag_ratio=0.1))
        
        # Animate labels appearing
        self.play(LaggedStart(*[FadeIn(label) for label in labels], lag_ratio=0.1))
        self.wait(1)
        
        # Write 15 on the far right of the screen
        number_15 = MathTex("15", font_size=48, color=RED)
        number_15.to_edge(RIGHT).shift(UP * 0.5)
        self.play(Write(number_15))
        self.wait(1)
        
        # Create a spiral arc that goes clockwise around the circle and then 90 degrees more
        # Starting from 0 (top) position
        start_angle = PI / 2  # 0 is at the top
        # One full rotation (360 degrees) plus 90 degrees more = 450 degrees = 2.5π
        # In clockwise direction (negative angle)
        total_angle = -(2 * PI + PI / 2)  # -450 degrees
        
        # Create a spiral by varying the radius as we go around
        num_points = 200
        spiral_points = []
        
        for i in range(num_points + 1):
            t = i / num_points  # Parameter from 0 to 1
            angle = start_angle + total_angle * t
            # Gradually decrease radius to create spiral effect
            current_radius = (radius - 0.2) - 0.4 * t  # Shrinks inward as it spirals
            x = current_radius * np.cos(angle)
            y = current_radius * np.sin(angle)
            spiral_points.append([x, y, 0])
        
        # Create the spiral path
        spiral_path = VMobject(color=RED, stroke_width=4)
        spiral_path.set_points_as_corners(spiral_points)
        spiral_path.make_smooth()
        
        # Add arrow tip manually
        arrow_tip = ArrowTriangleFilledTip(color=RED).scale(0.6)
        end_angle = start_angle + total_angle
        final_radius = (radius - 0.2) - 0.4  # Same as current_radius at t=1
        arrow_tip.move_to(final_radius * np.array([np.cos(end_angle), np.sin(end_angle), 0]))
        # Rotate to point in the direction of motion (tangent to circle, clockwise)
        arrow_tip.rotate(end_angle + PI/2)
        
        arc_with_arrow = VGroup(spiral_path, arrow_tip)
        arc_with_arrow = VGroup(spiral_path, arrow_tip)
        
        # Animate the spiral arc first, then show the arrow tip
        self.play(Create(spiral_path), run_time=3)
        self.play(FadeIn(arrow_tip), run_time=0.2)
        self.wait(2)
        
        # Add equivalence class notation under the 15
        equiv_class = MathTex(r"[3]_{12} = \{\ldots, -9, 3, 15, 27, \ldots\}", font_size=26, color=GRAY_C)
        equiv_class.next_to(number_15, DOWN, buff=0.7)
        equiv_class.shift(LEFT * 1.1)
        self.play(Write(equiv_class))
        self.wait(2)
        
        # Erase the equivalence class, then erase everything else
        self.play(FadeOut(equiv_class))
        self.play(FadeOut(spiral_path), FadeOut(arrow_tip), FadeOut(number_15))
        self.wait(1)
        
        # Write addition equation 6 + 11 =
        equation = MathTex("6", "+", "11", "=", font_size=48)
        equation[0].set_color(RED)  # 6 in red
        equation[2].set_color(PURPLE)  # 11 in purple
        equation.to_edge(RIGHT).shift(UP * 0.5)
        self.play(Write(equation))
        self.wait(1)
        
        # Create red spiral from 0 to 6
        # From 0 (top) clockwise to 6 (half way around, bottom)
        start_angle_red = PI / 2
        total_angle_red = -(6 * (2 * PI / n))  # 6 steps clockwise
        
        red_spiral_points = []
        for i in range(num_points + 1):
            t = i / num_points
            angle = start_angle_red + total_angle_red * t
            current_radius = (radius - 0.2) - 0.2 * t
            x = current_radius * np.cos(angle)
            y = current_radius * np.sin(angle)
            red_spiral_points.append([x, y, 0])
        
        red_spiral = VMobject(color=RED, stroke_width=4)
        red_spiral.set_points_as_corners(red_spiral_points)
        red_spiral.make_smooth()
        
        # No arrow tip for red spiral
        self.play(Create(red_spiral), run_time=2)
        
        # Create purple spiral from 6 to 5 (going 11 steps clockwise)
        # Starting from position 6, using the final radius from red spiral
        start_angle_purple = start_angle_red + total_angle_red
        start_radius_purple = (radius - 0.2) - 0.2  # Start where red spiral ended
        total_angle_purple = -(11 * (2 * PI / n))  # 11 steps clockwise
        
        purple_spiral_points = []
        for i in range(num_points + 1):
            t = i / num_points
            angle = start_angle_purple + total_angle_purple * t
            # Continue spiraling inward from where red left off
            current_radius = start_radius_purple - 0.3 * t
            x = current_radius * np.cos(angle)
            y = current_radius * np.sin(angle)
            purple_spiral_points.append([x, y, 0])
        
        purple_spiral = VMobject(color=PURPLE, stroke_width=4)
        purple_spiral.set_points_as_corners(purple_spiral_points)
        purple_spiral.make_smooth()
        
        purple_arrow_tip = ArrowTriangleFilledTip(color=PURPLE).scale(0.6)
        end_angle_purple = start_angle_purple + total_angle_purple
        final_radius_purple = start_radius_purple - 0.3
        purple_arrow_tip.move_to(final_radius_purple * np.array([np.cos(end_angle_purple), np.sin(end_angle_purple), 0]))
        purple_arrow_tip.rotate(end_angle_purple + PI/2)
        
        self.play(Create(purple_spiral), run_time=3)
        self.play(FadeIn(purple_arrow_tip), run_time=0.2)
        
        # Add the result 5 below the equation
        result_5 = MathTex("5", font_size=48, color=GREEN)
        result_5.next_to(equation, DOWN, buff=0.5)
        self.play(Write(result_5))
        self.wait(1)
        
        # Erase everything: equation, result, and spirals
        self.play(
            FadeOut(equation), 
            FadeOut(result_5), 
            FadeOut(red_spiral), 
            FadeOut(purple_spiral), 
            FadeOut(purple_arrow_tip)
        )
        self.wait(1)
        
        # Write multiplication equation 5 * 7 =
        mult_equation = MathTex("5", r"\cdot", "7", "=", font_size=48, color=RED)
        mult_equation.to_edge(RIGHT).shift(UP * 0.5)
        self.play(Write(mult_equation))
        self.wait(1)
        
        # Create spiral that goes around and lands at position 11
        # 5 * 7 = 35, and 35 mod 12 = 11
        # From 0, go 35 steps clockwise (2 full rotations + 11)
        start_angle_mult = PI / 2
        total_angle_mult = -(35 * (2 * PI / n))  # 35 steps clockwise
        
        mult_spiral_points = []
        for i in range(num_points + 1):
            t = i / num_points
            angle = start_angle_mult + total_angle_mult * t
            # Gradually decrease radius for spiral effect
            current_radius = (radius - 0.2) - 0.7 * t  # More inward spiral for longer path
            x = current_radius * np.cos(angle)
            y = current_radius * np.sin(angle)
            mult_spiral_points.append([x, y, 0])
        
        mult_spiral = VMobject(color=RED, stroke_width=4)
        mult_spiral.set_points_as_corners(mult_spiral_points)
        mult_spiral.make_smooth()
        
        mult_arrow_tip = ArrowTriangleFilledTip(color=RED).scale(0.6)
        end_angle_mult = start_angle_mult + total_angle_mult
        final_radius_mult = (radius - 0.2) - 0.7
        mult_arrow_tip.move_to(final_radius_mult * np.array([np.cos(end_angle_mult), np.sin(end_angle_mult), 0]))
        mult_arrow_tip.rotate(end_angle_mult + PI / 2)
        
        self.play(Create(mult_spiral), run_time=4)
        self.play(FadeIn(mult_arrow_tip), run_time=0.2)
        self.wait(1)
        
        # Add the result 11 below the equation
        result_11 = MathTex("11", font_size=48, color=RED)
        result_11.next_to(mult_equation, DOWN, buff=0.5)
        self.play(Write(result_11))
        self.wait(2)
        
        # Fade out the multiplication demonstration
        self.play(
            FadeOut(mult_spiral),
            FadeOut(mult_arrow_tip),
            FadeOut(mult_equation),
            FadeOut(result_11)
        )
        self.wait(1)
        
        # Display note about multiplicative inverse (multi-line)
        inverse_note = VGroup(
            Text("BUT", font_size=36, color=WHITE),
            MathTex(r"x^{-1} \text{ is NOT the}", font_size=36, color=WHITE),
            MathTex(r"\text{same as } \frac{1}{x}", font_size=36, color=WHITE),
            Text("here", font_size=36, color=WHITE)
        ).arrange(DOWN, center=True, buff=0.3)
        inverse_note.to_edge(RIGHT).shift(UP * 0.5)
        self.play(Write(inverse_note))
        self.wait(1)
        
        # Fade out everything except the title
        self.play(
            FadeOut(inverse_note),
            FadeOut(subtitle),
            FadeOut(circle),
            FadeOut(points),
            FadeOut(labels)
        )
        
        # Create a horizontal number line
        number_line = Line(LEFT * 4, RIGHT * 4, color=WHITE, stroke_width=2)
        self.play(Create(number_line))
        
        # Create dots for -3, -2, -1, 0, 1, 2, 3
        line_dots = VGroup()
        line_labels = VGroup()
        for i in range(-3, 4):
            # Adjust spacing to fit 7 points
            dot_pos = number_line.point_from_proportion(0.5 + i * (1/7))  # Evenly spaced
            dot = Dot(dot_pos, color=YELLOW, radius=0.1)
            line_dots.add(dot)
            
            label = MathTex(str(i), font_size=36)
            label.next_to(dot, DOWN, buff=0.3)
            line_labels.add(label)
        
        # Animate dots and labels appearing simultaneously
        self.play(
            LaggedStart(*[GrowFromCenter(dot) for dot in line_dots], lag_ratio=0.1),
            LaggedStart(*[FadeIn(label) for label in line_labels], lag_ratio=0.1)
        )
        
        # Add rational numbers definition below
        rationals_def = MathTex(
            r"\mathbb{Q} = \left\{\frac{p}{q} \mid p,q \in \mathbb{Z}, q \neq 0\right\}",
            font_size=40
        )
        rationals_def.shift(DOWN * 2.5)
        
        # Add fractional dots between 0 and 1, and repeat for all intervals
        # Fractions: 1/2, 1/3, 1/4, 1/5, 2/3, 2/5, 3/4, 3/5, 4/5
        fractional_dots = VGroup()
        fractions = [
            (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)
        ]
        
        # Create fractional dots in all intervals from -3 to 3
        for interval_start in range(-3, 3):
            # Get positions of interval_start and interval_start+1 dots
            start_pos = line_dots[interval_start + 3].get_center()  # +3 offset since range(-3,4)
            end_pos = line_dots[interval_start + 4].get_center()
            
            for num, denom in fractions:
                fraction_value = num / denom
                # Interpolate between start and end positions
                frac_pos = start_pos + fraction_value * (end_pos - start_pos)
                frac_dot = Dot(frac_pos, color=GREEN, radius=0.05)
                fractional_dots.add(frac_dot)
        
        # Animate Q definition and fractional dots appearing simultaneously
        self.play(
            Write(rationals_def),
            LaggedStart(*[GrowFromCenter(dot) for dot in fractional_dots], lag_ratio=0.02)
        )
        
        # Find and highlight the dot for 3 (index 6 in range(-3, 4))
        dot_3 = line_dots[6]
        
        # Find the dot for 1/3 in the interval [0, 1]
        # Fractions are ordered as: 1/2, 1/3, 1/4, 1/5, 2/3, 2/5, 3/4, 3/5, 4/5
        # In interval [0,1] (which is interval_start=0, so index 3 in range(-3, 3))
        # 1/3 is at index 1 within that interval's 9 fractions
        # Total fractional dots before interval 0: 3 intervals * 9 fractions = 27
        # So 1/3 is at index 27 + 1 = 28
        dot_1_3 = fractional_dots[28]
        
        # Transform their radius and color to pink, and bring 1/3 to foreground
        self.play(
            dot_3.animate.set_color(PINK).scale(1.5),
            dot_1_3.animate.set_color(PINK).scale(2.5)
        )
        # Bring the 1/3 dot to the front so it's not blocked
        self.bring_to_front(dot_1_3)
        
        # Add text above the line explaining 3^{-1}
        inverse_text = MathTex(
            r"\text{on the usual number line, } 3^{-1} \text{ is the number such that } 3 \cdot 3^{-1} = 3^{-1} \cdot 3 = 1",
            font_size=30
        )
        inverse_text.shift(UP * 2)
        self.play(Write(inverse_text))
        
        # Highlight the dot for 1 (index 4 in range(-3, 4)) in light blue
        dot_1 = line_dots[4]
        self.play(dot_1.animate.set_color(BLUE_C).scale(1.5))
        self.wait(2)
        
        # Fade out the number line and all associated elements
        self.play(
            FadeOut(number_line),
            FadeOut(line_dots),
            FadeOut(line_labels),
            FadeOut(fractional_dots),
            FadeOut(inverse_text),
            FadeOut(rationals_def)
        )
        self.wait(1)
        
        # Re-create the circle with points 0-11
        radius = 2.375
        circle_2 = Circle(radius=radius, color=BLUE, stroke_width=1.5, stroke_opacity=0.3)
        
        # Create points around the circle
        points_2 = VGroup()
        labels_2 = VGroup()
        
        for i in range(n):
            # Calculate angle for each point (starting from top, going clockwise)
            angle = -i * (2 * PI / n) + PI / 2
            
            # Create point position
            point_pos = radius * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Create dot
            dot = Dot(point_pos, color=YELLOW, radius=0.08)
            points_2.add(dot)
            
            # Create label
            label = MathTex(str(i), font_size=36)
            # Position label slightly outside the circle
            label_pos = (radius + 0.4) * np.array([np.cos(angle), np.sin(angle), 0])
            label.move_to(label_pos)
            labels_2.add(label)
        
        # Re-create the subtitle
        subtitle_2 = MathTex(r"\text{(e.g. } n = " + str(n) + r"\text{)}", font_size=36)
        subtitle_2.to_edge(LEFT).shift(UP * 2.5)
        
        # Animate the circle appearing
        self.play(Create(circle_2))
        self.wait(0.5)
        
        # Animate points, labels, and subtitle appearing simultaneously
        self.play(
            LaggedStart(*[GrowFromCenter(dot) for dot in points_2], lag_ratio=0.1),
            LaggedStart(*[FadeIn(label) for label in labels_2], lag_ratio=0.1),
            FadeIn(subtitle_2)
        )
        
        # Add notice text on the right side (multi-line)
        notice_text = VGroup(
            MathTex(r"\text{notice for any } x \in \mathbb{Z}_{12}^*", font_size=32),
            MathTex(r"\text{with}\ \gcd(x, 12) = 1,", font_size=32),
            MathTex(r"\text{we have}", font_size=32),
            MathTex(r"x^2 \equiv 1 \pmod{12}", font_size=32)
        )
        notice_text.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.2)
        notice_text.shift(RIGHT * 5.3 + UP * 0.5)
        
        # Add examples on the left side under the subtitle
        examples = VGroup(
            MathTex(r"5 \cdot 5 = 25 = 2(12) + 1", font_size=30, color=GRAY_C),
            MathTex(r"7 \cdot 7 = 49 = 4(12) + 1", font_size=30, color=GRAY_C),
            MathTex(r"11 \cdot 11 = 121 = 10(12) + 1", font_size=30, color=GRAY_C)
        )
        examples.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        examples.next_to(subtitle_2, DOWN, aligned_edge=LEFT, buff=0.8)
        examples.shift(DOWN * 1.5)
        
        # Write notice and examples simultaneously
        self.play(
            Write(notice_text),
            Write(examples)
        )
        
        # Highlight dot at position 5 and the corresponding example
        # Position 5 is at index 5 in points_2
        dot_5 = points_2[5]
        example_5 = examples[0]  # First example: 5 * 5 = 25 = 2(12) + 1
        
        self.play(
            dot_5.animate.set_color(PINK).scale(1.5),
            example_5.animate.set_color(PINK)
        )
        self.wait(2)
        
        # Fade out everything
        self.play(
            FadeOut(circle_2),
            FadeOut(points_2),
            FadeOut(labels_2),
            FadeOut(examples),
            FadeOut(notice_text),
            FadeOut(subtitle_2)
        )
        self.wait(1)
        
        # Create a new circle with n=15
        n_15 = 15
        radius_15 = 2.375
        circle_3 = Circle(radius=radius_15, color=BLUE, stroke_width=1.5, stroke_opacity=0.3)
        
        # Create points around the circle for n=15
        points_3 = VGroup()
        labels_3 = VGroup()
        
        for i in range(n_15):
            # Calculate angle for each point (starting from top, going clockwise)
            angle = -i * (2 * PI / n_15) + PI / 2
            
            # Create point position
            point_pos = radius_15 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Create dot
            dot = Dot(point_pos, color=YELLOW, radius=0.08)
            points_3.add(dot)
            
            # Create label
            label = MathTex(str(i), font_size=36)
            # Position label slightly outside the circle
            label_pos = (radius_15 + 0.4) * np.array([np.cos(angle), np.sin(angle), 0])
            label.move_to(label_pos)
            labels_3.add(label)
        
        # Create subtitle for n=15
        subtitle_3 = MathTex(r"\text{(e.g. } n = " + str(n_15) + r"\text{)}", font_size=36)
        subtitle_3.to_edge(LEFT).shift(UP * 2.5)
        
        # Animate the circle appearing
        self.play(Create(circle_3))
        self.wait(0.5)
        
        # Animate points, labels, and subtitle appearing simultaneously
        self.play(
            LaggedStart(*[GrowFromCenter(dot) for dot in points_3], lag_ratio=0.1),
            LaggedStart(*[FadeIn(label) for label in labels_3], lag_ratio=0.1),
            FadeIn(subtitle_3)
        )
        self.wait(2)
