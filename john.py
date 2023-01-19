from numbers import Number
import os
from talon import Context, Module, actions

module = Module()
context = Context()

@module.action_class
class Actions:
    def pick(value: int):
        """Pick an item from a drop down list

        Args:
        value (int): The number of the item to choose
        """
        # for i in range(1,value):
        #   actions.key("down")
        # actions.key("enter")