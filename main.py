from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line = Line(Point(50,400), Point(400,400))
    win.draw_line(line, "white")
    win.wait_for_close()

main()