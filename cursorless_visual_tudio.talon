app: visual_studio
-

scout <user.cursorless_target>:
  user.cursorless_command("setSelection", cursorless_target)
  user.run_rpc_command("VSCommand","Edit.Find")
