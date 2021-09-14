print(' ')
print('Info: Local "userSetup.py" starting execution..')
print('Info: ------------------------------------------------------')
import sys
sys.path.append('D:/rigging_tools/')
print('Info: Script path "D:/rigging_tools/" successfully appended.')

import maya.cmds as cmds


cmds.evalDeferred('from an_scriptManager2 import *')
cmds.evalDeferred('an_scriptManager2()')

print('Info: ------------------------------------------------------')
print('Info: Local "userSetup.py" successfully complete execution.')
print(' ')