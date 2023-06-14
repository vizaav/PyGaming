from pygame import image

# BRAJANEK
# image class
bieg_A_lewanoga = image.load("assets/brajanek/bieg_A_lewanoga.png")
bieg_A_prawanoga = image.load("assets/brajanek/bieg_A_prawanoga.png")
bieg_D_lewanoga = image.load("assets/brajanek/bieg_D_lewanoga.png")
bieg_D_prawanoga = image.load("assets/brajanek/bieg_D_prawanoga.png")
bieg_S_lewanoga = image.load("assets/brajanek/bieg_S_lewanoga.png")
bieg_S_prawanoga = image.load("assets/brajanek/bieg_S_prawanoga.png")
bieg_W_lewanoga = image.load("assets/brajanek/bieg_W_lewanoga.png")
bieg_W_prawanoga = image.load("assets/brajanek/bieg_W_prawanoga.png")
stanie_A = image.load("assets/brajanek/stanie_A.png")
stanie_D = image.load("assets/brajanek/stanie_D.png")
stanie_S = image.load("assets/brajanek/stanie_S.png")
stanie_W = image.load("assets/brajanek/stanie_W.png")
porazka = image.load("assets/brajanek/porazka.png")
bieg_lewo_gif = image.load("assets/brajanek/bieg_lewo.gif")

# dictionary
wyglady = {"bieg_A_lewanoga": bieg_A_lewanoga,
           "bieg_A_prawanoga": bieg_A_prawanoga,
           "bieg_D_lewanoga": bieg_D_lewanoga,
           "bieg_D_prawanoga": bieg_D_prawanoga,
           "bieg_S_lewanoga": bieg_S_lewanoga,
           "bieg_S_prawanoga": bieg_S_prawanoga,
           "bieg_W_lewanoga": bieg_W_lewanoga,
           "bieg_W_prawanoga": bieg_W_prawanoga,
           "stanie_LEFT": stanie_A,
           "stanie_RIGHT": stanie_D,
           "stanie_DOWN": stanie_S,
           "stanie_UP": stanie_W,
           "porazka": porazka,
           "bieg_lewo_gif": bieg_lewo_gif}

# WHITE CAT

# dictionary
wyglady_white_cat = {"down_left_leg": image.load("assets/cats/white/down_left_leg.png"),
                     "down_right_leg": image.load("assets/cats/white/down_right_leg.png"),
                     "down_stand": image.load("assets/cats/white/down_stand.png"),
                     "left_left_leg": image.load("assets/cats/white/left_left_leg.png"),
                     "left_right_leg": image.load("assets/cats/white/left_right_leg.png"),
                     "left_stand": image.load("assets/cats/white/left_stand.png"),
                     "right_left_leg": image.load("assets/cats/white/right_left_leg.png"),
                     "right_right_leg": image.load("assets/cats/white/right_right_leg.png"),
                     "right_stand": image.load("assets/cats/white/right_stand.png"),
                     "up_left_leg": image.load("assets/cats/white/up_left_leg.png"),
                     "up_right_leg": image.load("assets/cats/white/up_right_leg.png"),
                     "up_stand": image.load("assets/cats/white/up_stand.png")}

# BLACK CAT

# dictionary
wyglady_black_cat = {"down_left_leg": image.load("assets/cats/black/down_left_leg.png"),
                        "down_right_leg": image.load("assets/cats/black/down_right_leg.png"),
                        "down_stand": image.load("assets/cats/black/down_stand.png"),
                        "left_left_leg": image.load("assets/cats/black/left_left_leg.png"),
                        "left_right_leg": image.load("assets/cats/black/left_right_leg.png"),
                        "left_stand": image.load("assets/cats/black/left_stand.png"),
                        "right_left_leg": image.load("assets/cats/black/right_left_leg.png"),
                        "right_right_leg": image.load("assets/cats/black/right_right_leg.png"),
                        "right_stand": image.load("assets/cats/black/right_stand.png"),
                        "up_left_leg": image.load("assets/cats/black/up_left_leg.png"),
                        "up_right_leg": image.load("assets/cats/black/up_right_leg.png"),
                        "up_stand": image.load("assets/cats/black/up_stand.png")}

# BULLET

# dictionary
wyglady_bullet = {"bullet": image.load("assets/bullet.png")}

# COIN

# dictionary
wyglady_coin = {"coin": image.load("assets/coin/coin.png")}


# HEART

# dictionary
wyglady_heart = {"heart": image.load("assets/coin/heart.png")}