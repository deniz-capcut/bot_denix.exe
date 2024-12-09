import random
import discord

def gen_pass():
    elements = "+-/*!&$#?=@<>qwertyuopasdfghjklizxcvbnmQWERTYUIOPASDFGHJKLZXCVBNNM"
    password = ""
    for i in range(10):
        password += random.choice(elements)
    return password
