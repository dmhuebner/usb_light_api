from blinkstick import blinkstick

all_blink_sticks = blinkstick.find_all()

if len(all_blink_sticks) > 0:
    for bstick in all_blink_sticks:
        bstick.morph(hex='#00ff00', duration=1000)
else:
    print("No BlinkSticks found...")
