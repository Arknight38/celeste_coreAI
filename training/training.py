import pymem

# Attach to the Celeste process
pm = pymem.Pymem("celeste.exe")

# Read player X position (replace 0x123456 with the actual address)
player_x = pm.read_float(0x123456)
print(f"Player X Position: {player_x}")