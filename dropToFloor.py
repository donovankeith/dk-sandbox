"""Name-en-US: Drop to Floor
Description-en-US: Drops the selected object(s) so that they are each resting on the first floor object in your scene."""

import c4d
from c4d import gui
# Welcome to the world of Python


# Script state in the menu or the command palette
# Return True or c4d.CMD_ENABLED to enable, False or 0 to disable
# Alternatively return c4d.CMD_ENABLED|c4d.CMD_VALUE to enable and check/mark
#def state():
#    return True

# Main function
def main():
    gui.MessageDialog('Hello World!')

# Execute main()
if __name__=='__main__':
    main()