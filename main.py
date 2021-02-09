while True:
    if input.light_level()+ 130 > 500:
        light.set_all(light.rgb(0, 0, 250))
