#!/user/bin/python
# vim: et sw=2 ts=2 sts=2
#
# Lower Floor:
#
# ---> NORTH
#           -----------------------------
#           | Maga's | Laura's | living |
#           | room   | room    | room   |
# --------------O---------O---------O----
# | Kitchen O         Hallway           |
# |         |                           |
# -----------        ---------------O----
#           | Stairs O Rest-   |   Exit
#           |        | room    |
#           -----O--------------
#           | Bath-  |
#           | room   |
#           ----------
#
# Upper Floor:
#
# ---> NORTH
# --------------------------------------
# | Marco's O Stairs O Andz's  O Attic  |
# | room    |        | room    |        |
# -------O-------------------------------
# | Closet  |
# |         |
# -----------


from advent import *
from advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

# Create the game

print("                       ~~~ Welcome to ~~~                       ")
print("    ___       __                 __                     ___  ___")
print("   /   | ____/ /   _____  ____  / /___  __________     |__ \<  /")
print("  / /| |/ __  / | / / _ \/ __ \/ __/ / / / ___/ _ \    __/ // / ")
print(" / ___ / /_/ /| |/ /  __/ / / / /_/ /_/ / /  /  __/   / __// /  ")
print("/_/  |_\__,_/ |___/\___/_/ /_/\__/\__,_/_/   \___/   /____/_/   ")
print("                                                                ")
print("                       ~~~~~~~~~~~~~~~~~~                       ")
print("                                                                ")
print("For a list of commands, just enter 'commands' or 'verbs'...     ")
print("                                                                ")

game = Game("Adventure 21")


# Create all Rooms

room_hallway_north = game.new_location(
  "Hallway North",
  """You find yourself in a hallway. In the west, you see the open door to the living room.
In the east, you look at a door with a combination lock. 
The hallway extends towards south.""")

room_hallway_middle = game.new_location(
  "Center Hallway",
""" You still walk through the hallway. There is a closed door in the west.
The hallway is open to south and north.""")

room_hallway_south = game.new_location(
  "Hallway South",
"""You find yourself at the south end of the hallway. There is an open door towards west.
The kitchen is placed in the south. 
The hallway still extends towards east.""")

room_hallway_east = game.new_location(
  "Hallway East",
"""The east wing of the hallway looks higher than the rest. The bathroom is in the east.
Towards north you can find the restroom.
You see circular staris heading upwards. 
Westbound you see all the far way back.""")

room_living_room = game.new_location(
  "Living Room",
"""A living room where no one ever lived.""")

room_laura = game.new_location(
  "Laura's Room",
"""You see a big, cozy bed.""")

room_maga = game.new_location(
  "Maga's Room",
"""Art, everywhere is art on the walls.""")

room_kitchen = game.new_location(
  "Kitchen",
"""Cooking time.""")

room_bath = game.new_location(
  "Bathroom",
"""Hmmm...""")

room_klo = game.new_location(
  "Restroom",
"""Sometimes you need your time.""")

room_oben = game.new_location(
  "Circular staircase, upper level",
"""There is an upstairs!?!?
You see a wall full of skateboards in front of you.
You can enter two rooms in the south and north""")

room_marco = game.new_location(
  "Marco's Room",
"""You find yourself inside an curiosity shop.
There is an closet eastbound""")

room_closet = game.new_location(
  "Closet",
""":-o""")

room_andz = game.new_location(
  "Andz's Room",
"""Chaos, Chaos everywhere.
There is a closed door in the north""")

room_attic = game.new_location(
  "Attic",
"""An Attic!""")

# connect the rooms

game.new_connection("hallway", room_hallway_north, room_hallway_middle, SOUTH, NORTH)
game.new_connection("hallway", room_hallway_middle, room_hallway_south, SOUTH, NORTH)
game.new_connection("hallway", room_hallway_south, room_hallway_east, EAST, WEST)

game.new_connection("door", room_hallway_north, room_living_room, WEST, EAST)
game.new_connection("door", room_hallway_middle, room_laura, WEST, EAST)
game.new_connection("door", room_hallway_south, room_maga, WEST, EAST)
game.new_connection("door", room_hallway_south, room_kitchen, SOUTH, NORTH)
game.new_connection("door", room_hallway_east, room_bath, EAST, WEST)
game.new_connection("door", room_hallway_east, room_klo, NORTH, SOUTH)

game.new_connection("circular stairs", room_hallway_east, room_oben, UP, DOWN)

game.new_connection("door", room_oben, room_marco, SOUTH, NORTH)
game.new_connection("door", room_marco, room_closet, EAST, WEST)
game.new_connection("door", room_oben, room_andz, NORTH, SOUTH)
game.new_connection("door", room_andz, room_attic, NORTH, SOUTH)

# Create Objects

skateboard = room_oben.new_object("skateboard", "Wanna ride?")

def death_by_skateboard(self, actor, noun, words):
  if actor == hero:
    self.game.output("You are skating throgh '" + actor.location.name + "' but you can't skate. You broke your neck.")
    hero.terminate()
  else:
    self.game.output(actor.name + " is skating through " + actor.location.name + ".")
  return True

skateboard.add_verb(Verb(death_by_skateboard, "skate"))

# Now we are going to add our player at the starting location:

hero = Player()
hero.set_location(room_hallway_north)

egon = Pet("Egon")
egon.set_location(room_hallway_east)
egon.add_verb(SayOnSelf("Egon shakes his leaves for joy.", "water"))

game.add_actor(hero)
game.add_actor(egon)

game.run()
