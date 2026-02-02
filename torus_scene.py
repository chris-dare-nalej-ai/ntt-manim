from manim import *


class TorusScene(ThreeDScene):
    def construct(self):
        # Set up the 3D camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        # Create a torus
        torus = Surface(
            lambda u, v: np.array([
                (2 + np.cos(v)) * np.cos(u),
                (2 + np.cos(v)) * np.sin(u),
                np.sin(v)
            ]),
            u_range=[0, TAU],
            v_range=[0, TAU],
            resolution=(32, 32),
            fill_opacity=0.8,
            stroke_width=0.5
        )
        
        # Set the color of the torus
        torus.set_color(BLUE)
        
        # Add the torus to the scene
        self.play(Create(torus), run_time=1)
        
        # Create a circular patch on the torus surface using a grid of curves
        # This represents the region where the disk chart would be "cut from"
        patch_curves = VGroup()
        
        # Define the center and size of the patch
        u_center = PI/3  # Position around the torus (0 to 2π)
        v_center = PI/4  # Position around the tube (0 to 2π)
        patch_radius = 0.6  # Radius in parameter space
        
        # Draw concentric circles in (u,v) parameter space mapped to torus surface
        for r in np.linspace(0.1, patch_radius, 3):
            circle_points = []
            for theta in np.linspace(0, TAU, 50):
                u = u_center + r * np.cos(theta)
                v = v_center + r * np.sin(theta)
                point = np.array([
                    (2 + np.cos(v)) * np.cos(u),
                    (2 + np.cos(v)) * np.sin(u),
                    np.sin(v)
                ])
                circle_points.append(point)
            
            curve = VMobject(color=YELLOW, stroke_width=4)
            curve.set_points_as_corners(circle_points + [circle_points[0]])
            patch_curves.add(curve)
        
        # Draw radial lines from center to edge
        for theta in np.linspace(0, TAU, 8, endpoint=False):
            radial_points = []
            for r in np.linspace(0, patch_radius, 20):
                u = u_center + r * np.cos(theta)
                v = v_center + r * np.sin(theta)
                point = np.array([
                    (2 + np.cos(v)) * np.cos(u),
                    (2 + np.cos(v)) * np.sin(u),
                    np.sin(v)
                ])
                radial_points.append(point)
            
            curve = VMobject(color=YELLOW, stroke_width=4)
            curve.set_points_as_corners(radial_points)
            patch_curves.add(curve)
        
        self.play(Create(patch_curves), run_time=2)
        
        # Rotate the camera around the torus
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(1)
        self.stop_ambient_camera_rotation()
        self.wait(2)
        
        # Create a wavy torus with variation in the z-axis
        wavy_torus = Surface(
            lambda u, v: np.array([
                (2 + np.cos(v)) * np.cos(u),
                (2 + np.cos(v)) * np.sin(u),
                np.sin(v) + 0.8 * np.sin(3 * u) * np.cos(v)  # Add wave variation (increased from 0.3 to 0.8)
            ]),
            u_range=[0, TAU],
            v_range=[0, TAU],
            resolution=(32, 32),
            fill_opacity=0.8,
            stroke_width=0.5
        )
        wavy_torus.set_color(BLUE)
        
        # Create the transformed patch on the wavy torus
        wavy_patch_curves = VGroup()
        
        for r in np.linspace(0.1, patch_radius, 3):
            circle_points = []
            for theta in np.linspace(0, TAU, 50):
                u = u_center + r * np.cos(theta)
                v = v_center + r * np.sin(theta)
                point = np.array([
                    (2 + np.cos(v)) * np.cos(u),
                    (2 + np.cos(v)) * np.sin(u),
                    np.sin(v) + 0.8 * np.sin(3 * u) * np.cos(v)  # Apply wave
                ])
                circle_points.append(point)
            
            curve = VMobject(color=YELLOW, stroke_width=4)
            curve.set_points_as_corners(circle_points + [circle_points[0]])
            wavy_patch_curves.add(curve)
        
        for theta in np.linspace(0, TAU, 8, endpoint=False):
            radial_points = []
            for r in np.linspace(0, patch_radius, 20):
                u = u_center + r * np.cos(theta)
                v = v_center + r * np.sin(theta)
                point = np.array([
                    (2 + np.cos(v)) * np.cos(u),
                    (2 + np.cos(v)) * np.sin(u),
                    np.sin(v) + 0.8 * np.sin(3 * u) * np.cos(v)  # Apply wave
                ])
                radial_points.append(point)
            
            curve = VMobject(color=YELLOW, stroke_width=4)
            curve.set_points_as_corners(radial_points)
            wavy_patch_curves.add(curve)
        
        # Transform the torus and patch to the wavy version
        self.play(
            Transform(torus, wavy_torus),
            Transform(patch_curves, wavy_patch_curves),
            run_time=2
        )
        self.wait(2)
        
        # Fade out torus and patch
        self.play(FadeOut(torus), FadeOut(patch_curves))
        self.wait(1)
        
        # Create a unit disk (chart map for the torus manifold)
        disk = Surface(
            lambda u, v: np.array([
                v * np.cos(u),
                v * np.sin(u),
                0
            ]),
            u_range=[0, TAU],
            v_range=[0, 1],
            resolution=(32, 16),
            fill_opacity=0.8,
            stroke_width=0.5
        )
        disk.set_color(GREEN)
        
        # Show the unit disk
        self.play(Create(disk), run_time=1.5)
        self.wait(3)
        
        # Create a wavy disk with similar wave pattern (mirrored to match torus deformation)
        wavy_disk = Surface(
            lambda u, v: np.array([
                v * np.cos(u),
                v * np.sin(u),
                0.3 * np.sin(3 * u) * v  # Negated to mirror the wave pattern
            ]),
            u_range=[0, TAU],
            v_range=[0, 1],
            resolution=(32, 16),
            fill_opacity=0.8,
            stroke_width=0.5
        )
        wavy_disk.set_color(GREEN)
        
        # Transform the disk to the wavy version with camera rotation
        self.begin_ambient_camera_rotation(rate=PI)  # rate=PI gives ~360 degrees in 2 seconds
        self.play(Transform(disk, wavy_disk), run_time=2)
        self.stop_ambient_camera_rotation()
        self.wait(2)
