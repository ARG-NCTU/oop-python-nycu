import argparse
import time
import numpy as np
import math
import itertools
import pyivp


from env import EmptyEnv


def parseArgs():
    parser = argparse.ArgumentParser()
    # env 
    parser.add_argument('--env_dim', default=[100, 100], type=int, nargs='+', help='[width, height], unit = meter')
    parser.add_argument('--env_px', default=1000, type=int, help='pixel size about display window')
    parser.add_argument('--fps', default=100, type=int, help='frame per second for display update usage')

    args = parser.parse_args()
    return args


def getPatternWaypoint(pattern_point, pattern_type, stride):
    wp_with_deg = []


    for i in range(pattern_point.size()):
        if i == pattern_point.size()-1:
            if pattern_type == "polygon":
                x1 = int(pattern_point.get_vx(i))
                y1 = int(pattern_point.get_vy(i))
                x2 = int(pattern_point.get_vx(0))
                y2 = int(pattern_point.get_vy(0))
            elif pattern_type == "pattern_block":
                break
        else:
            x1 = int(pattern_point.get_vx(i))
            y1 = int(pattern_point.get_vy(i))

            x2 = int(pattern_point.get_vx(i+1))
            y2 = int(pattern_point.get_vy(i+1))

        
        resolution = round(math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2)) / stride)

        degree = 0
        if x2-x1 == 0:
            if y2-y1 >= 0:
                degree = 90
            else:
                degree = -90
        else:
            degree = abs(np.rad2deg(math.atan((y2-y1)/(x2-x1))))

            if y2-y1 == 0:
                if x2-x1 >= 0:
                    degree = 0
                else:
                    degree = 180
            else:
                if x2-x1 < 0 and y2-y1 >= 0:
                    degree = 180 - degree
                elif x2-x1 >= 0 and y2-y1 < 0:
                    degree = -degree
                elif x2-x1 < 0 and y2-y1 < 0:
                    degree = degree - 180
            
        waypoints = list(zip(
            np.linspace(x1, x2, resolution+1),
            np.linspace(y1, y2, resolution+1),
        ))

        for waypoint in waypoints:
            new_waypoint = waypoint + (degree,)
            wp_with_deg.append(new_waypoint)

    return wp_with_deg


def plotPattern(env, script_set):
    screen = env.displayInit()
    character1 = env.characterInit("./img/duck.png", 200)
    character2 = env.characterInit("./img/duckie.png", 100)
    character3 = env.characterInit("./img/duckie.png", 100)

    while True:
        for single_script in script_set:
            for step in itertools.count(start=0):
                if step >= len(single_script):
                    break
                env.renderBackground(screen)
                env.renderPath(screen, single_script, step)
                env.renderCharacter(screen, character1, single_script, step)
                env.renderCharacter(screen, character2, single_script, step-25)
                env.renderCharacter(screen, character3, single_script, step-40)
                env.renderUpdate()
            
            env.clearPath()
        
    env.close()
    return


if __name__ == "__main__":
    arg = parseArgs()

    env = EmptyEnv(arg)

    script_set = []
    # pyivp - get pattern block vertices
    pattern_1 = pyivp.string2SegList("format=lawnmower, x=0, y=0, height=70, \
                                    width=50, lane_width=10, rows=north-south, startx=0, starty=0, degs=0")
    # pyivp - get pattern block vertices
    pattern_2 = pyivp.string2SegList("format=lawnmower, x=0, y=0, height=60, \
                                    width=60, lane_width=6, rows=north-south, startx=0, starty=0, degs=25")
    # pyivp - get polygon vertices
    poly_init_1 = pyivp.string2Poly("x=0, y=0, format=radial, radius=25, pts=9")
    poly_1 = poly_init_1.exportSegList(-10, 10)
    # pyivp - get polygon vertices
    poly_init_2 = pyivp.string2Poly("x=10, y=10, format=radial, radius=20, pts=8")
    poly_2 = poly_init_2.exportSegList(10, -10)
    # pyivp - get polygon vertices
    poly_init_3 = pyivp.string2Poly("x=0, y=0, format=radial, radius=10, pts=6")
    poly_3 = poly_init_3.exportSegList(-10, -10)

    # transfer vertices to waypoints
    wp_pattern_1 = getPatternWaypoint(pattern_1, "pattern_block", 0.5)
    wp_pattern_2 = getPatternWaypoint(pattern_2, "pattern_block", 0.5)
    wp_poly_1  = getPatternWaypoint(poly_1, "polygon",  0.5)
    wp_poly_2  = getPatternWaypoint(poly_2, "polygon",  0.5)
    wp_poly_3  = getPatternWaypoint(poly_3, "polygon",  0.5)


    script_set.append(wp_pattern_1)
    script_set.append(wp_poly_1)
    script_set.append(wp_poly_2)
    script_set.append(wp_pattern_2)
    script_set.append(wp_poly_3)
    

    plotPattern(env, script_set)


    


    
    
    

    

    
