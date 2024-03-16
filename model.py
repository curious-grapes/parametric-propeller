import numpy as np
import cadquery as cq

class Model:
    def __init__(self, blade_type, num_blade_input, attack_angle_input, hub_diameter_input, out_diameter_input, height_input):
        self.blade_type = blade_type
        self.num_blade_input = num_blade_input
        self.attack_angle_input = attack_angle_input
        self.hub_diameter_input = hub_diameter_input
        self.out_diameter_input = out_diameter_input
        self.height_input = height_input
    def model(self):
        # Airfoil points
        points = self.blade_type
        # Cylinder radius
        cylinder_radius = self.hub_diameter_input / 2
        # Cylinder height
        cylinder_height = self.height_input
        # Blade length
        blade_length = self.out_diameter_input /2 - cylinder_radius
        # Angle of attack
        angle_attack = self.attack_angle_input
        # Number of blades
        num_copies = self.num_blade_input
        # Multiply list by scale parameter
        modified_tuple_list = [(item[0] * cylinder_height, item[1] * cylinder_height) for item in points]
        # get initial height when blade is staight
        # cylinder_height = modified_tuple_list[0][0]
        # new height of cylinder based on the height of tilted blades
        cylinder_new_height = cylinder_height * np.cos(np.radians(angle_attack)) + 0.01
        # create cylinder
        cylinder = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_new_height)
        cylinder = cylinder.mirror()
        # create blade from foil data and extrude by specified length
        blade = cq.Workplane("left", origin=(blade_length, 0, 0)).spline(modified_tuple_list).close().extrude(blade_length + 1)
        # create the angle of attack
        anlge_blade = blade.rotate((0, 0, 0), (1, 0, 0), angle_attack)
        # Create copies and rotate around the cylinder
        for i in range(num_copies):
            angle = i * (360 / num_copies)
            rotated_model = anlge_blade.rotate((0, 0, 0), (0, 0, 1), angle)
            copied_model = rotated_model.mirror("XY").translate((cylinder_radius * np.cos(np.radians(angle)),
                                                                cylinder_radius * np.sin(np.radians(angle)),
                                                                0))
            cylinder = cylinder.union(copied_model) 
        # Mirror propeller
        propeller = cylinder.mirror()
        # Display the final result
        #show_object(cylinder)
        cq.exporters.export(propeller, "C:/Users/Roman/Desktop/Result/propeller.step")
        return "12312"