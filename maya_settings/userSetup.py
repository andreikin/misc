import maya.cmds as cmds

# connect pycharm
if not cmds.commandPort(":4434", query=True):
    cmds.commandPort(name=":4434")

# load an_scriptManager
cmds.evalDeferred('from an_scriptManager import *')
cmds.evalDeferred('an_scriptManager()')
