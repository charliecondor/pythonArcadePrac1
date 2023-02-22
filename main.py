"""
Practice Python application utilizing the Python Arcade Library
This application draws a dynamically generated hexagon/honeycomb grid
"""
import arcade


# Creates a honeycomb grid
def main_loop():
    print('Starting Application...')
    main_window_width = 1000
    main_window_height = 800
    arcade.open_window(main_window_width, main_window_height, "Honeycomb Grid").center_window()

    arcade.set_background_color(arcade.csscolor.AQUAMARINE)

    arcade.start_render()
    hexagon_side_length = 75
    generate_honeycomb_grid([50, ((main_window_height / 2) - hexagon_side_length)], hexagon_side_length)
    arcade.finish_render()

    arcade.run()


# Creates a list of origin points for each honeycomb within a honeycomb style grid
def generate_honeycomb_grid_tuples(grid_base_point, side_length):
    hc1o_point = grid_base_point
    hc2o_point = [(grid_base_point[0] + (3 * side_length)), grid_base_point[1]]
    hc3o_point = [(grid_base_point[0] + (6 * side_length)), grid_base_point[1]]
    hc4o_point = [(grid_base_point[0] + (9 * side_length)), grid_base_point[1]]
    hcXo_points = [hc1o_point, hc2o_point, hc3o_point, hc4o_point]

    hc1b_point = [(grid_base_point[0] + (side_length / 2) + side_length), (grid_base_point[1] - side_length)]
    hc2b_point = [(grid_base_point[0] + (3 * ((side_length / 2) + side_length))), (grid_base_point[1] - side_length)]
    hc3b_point = [(grid_base_point[0] + (5 * ((side_length / 2) + side_length))), (grid_base_point[1] - side_length)]
    hc4b_point = [(grid_base_point[0] + (3 * side_length)), (grid_base_point[1] - (2 * side_length))]
    hc5b_point = [(grid_base_point[0] + (6 * side_length)), (grid_base_point[1] - (2 * side_length))]
    hcXb_points = [hc1b_point, hc2b_point, hc3b_point, hc4b_point, hc5b_point]

    hc1a_point = [(grid_base_point[0] + (side_length / 2) + side_length), (grid_base_point[1] + side_length)]
    hc2a_point = [(grid_base_point[0] + (3 * ((side_length / 2) + side_length))), (grid_base_point[1] + side_length)]
    hc3a_point = [(grid_base_point[0] + (5 * ((side_length / 2) + side_length))), (grid_base_point[1] + side_length)]
    hc4a_point = [(grid_base_point[0] + (3 * side_length)), (grid_base_point[1] + (2 * side_length))]
    hc5a_point = [(grid_base_point[0] + (6 * side_length)), (grid_base_point[1] + (2 * side_length))]
    hcXa_points = [hc1a_point, hc2a_point, hc3a_point, hc4a_point, hc5a_point]

    all_points = hcXo_points + hcXb_points + hcXa_points
    # print(all_points)
    return all_points


# Creates a honeycomb grid and draws the honeycombs
def generate_honeycomb_grid(grid_base_point, honeycomb_side_length):
    grid_tuples = generate_honeycomb_grid_tuples(grid_base_point, honeycomb_side_length)
    for hc_tuple in grid_tuples:
        generate_honeycomb(hc_tuple, honeycomb_side_length)
    return True


# Draws a filled hexagon and outline of hexagon in the style of a honeycomb
def generate_honeycomb(base_point, side_length):
    arcade.draw_polygon_filled(generate_hexagon_tuples(base_point, side_length), arcade.csscolor.GOLD)
    arcade.draw_polygon_outline(generate_hexagon_tuples(base_point, side_length), arcade.csscolor.GOLDENROD, 2)
    return True


# Generates a list of polygon points for a perfectly symmetrical hexagon given an origin point and length of side
def generate_hexagon_tuples(base_point, side_length):
    point1 = [base_point[0], base_point[1] + side_length]
    point2 = [(base_point[0] + (side_length / 2)), (base_point[1] + (2 * side_length))]
    point3 = [(base_point[0] + (side_length / 2) + side_length), (base_point[1] + (2 * side_length))]
    point4 = [(base_point[0] + (2 * side_length)), (base_point[1] + side_length)]
    point5 = [(base_point[0] + (side_length / 2) + side_length), base_point[1]]
    point6 = [(base_point[0] + (side_length / 2)), base_point[1]]
    # print(point1, "|", point2, "|", point3, "|", point4, "|", point5, "|", point6)
    return [point1, point2, point3, point4, point5, point6]


if __name__ == '__main__':
    main_loop()