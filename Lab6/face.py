def draw_face_at(canvas, x_center, y_center, radius):
    ''' Draws a face on canvas with the given center coordinate and radius.'''
    
    x_lft = x_center - radius
    y_top = y_center - radius
    width = 2 * radius
    height = 2 * radius
    draw_face_shifted(canvas, x_lft, y_top, width, height)


def draw_face_shifted(canvas, x_lft, y_top, width, height):
    ''' Draws a face on canvas with the given top-left coordinate,
    width and height (in pixels).'''

    scale_x = width/400
    scale_y = height/400

    # Face background
    canvas.create_oval(
        0 * scale_x + x_lft, 0 * scale_y + y_top,
        400 * scale_x + x_lft, 400 * scale_y + y_top,
        fill='pink'
    )

    # Eyes
    canvas.create_oval(
        100 * scale_x + x_lft, 100 * scale_y + y_top,
        130 * scale_x + x_lft, 150 * scale_y + y_top,
        fill='red'
    )
    canvas.create_oval(
        270 * scale_x + x_lft, 100 * scale_y + y_top,
        300 * scale_x + x_lft, 150 * scale_y + y_top,
    fill='red')

    # Mouth
    canvas.create_line(
        100 * scale_x + x_lft, 300 * scale_y + y_top,
        200 * scale_x + x_lft, 370 * scale_y + y_top,
        300 * scale_x + x_lft, 300 * scale_y + y_top,
        fill='red', width=8, smooth=True
    )