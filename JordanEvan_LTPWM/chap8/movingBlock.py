from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def calculateMove():
    """Changes the x and z variabkes for a block. If the block in fornt of the block is less than 2 blocks higher, it will move forward; otherwise it will try to move left, then backward, then finally right."""
    