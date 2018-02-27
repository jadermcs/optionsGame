from asciimatics.effects import Print
from asciimatics.renderers import FigletText, BarChart
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from random import randint

import math
import time
import sys

def wv(x, s=2):
    return lambda: 50 + 50* math.sin(math.pi * (s*time.time()+x) / 5)

def wvc(x, s=2):
    return lambda: 100 - (50 + 50*math.sin(math.pi * (s*time.time()+x) / 5)
)

def fn():
    return randint(0,40)

def ui(screen):
    scenes = []
    if screen.width != 70 or screen.height != 53:
        effects = [Print(screen, FigletText("Resize to 70x53"),
                         y=screen.height//2-3)]
    else:
        effects = [
            Print(screen, FigletText("OptionsGAME"), y=0),
            Print(screen,
                  BarChart(8, 68, [wvc(9, 8), wv(9, 8)],
                           scale=100.0,
                           labels=True,
                           intervals=25.0,
                           border=False,
                           bg=[1,2],
                           colour=[1,2],
                           axes=BarChart.X_AXIS),
                  x=1, y=7, transparent=False, speed=1),
            Print(screen,
                  BarChart(20, 68, [wv(7), wv(8), wv(9)],
                           char="x",
                           scale=100.0,
                           labels=True,
                           intervals=25.0,
                           axes=BarChart.X_AXIS,
                           gradient=[(50, Screen.COLOUR_GREEN),
                                     (75, Screen.COLOUR_YELLOW),
                                     (100, Screen.COLOUR_RED)]
                           ),
                  x=1, y=15, transparent=False, speed=1)
        ]

    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)



if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(ui)
            sys.exit(0)
        except ResizeScreenError:
            pass
