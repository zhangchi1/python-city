from safety.safety import draw_safety
from leisure.leisure import draw_leisure
from outdoors.outdoors import draw_outdoors
from education.education import draw_education
from infrastructure.road import draw_road

def draw_city():
    draw_safety()
    draw_road(2,'vertical')
    draw_leisure()
    draw_road(2,'vertical')
    draw_outdoors()
    draw_road(2,'vertical')
    draw_education()
    return
draw_city()
