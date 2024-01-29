import pygame
pygame.init()

# Ekraani seaded
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ülesanne 2")

# Taustapildi laadimine
bg = pygame.image.load("bg_shop.png")

# Taustapildi kuvamine ekraanil koordinaatidega [0, 0]
screen.blit(bg, [0, 0])


# Poemüüja pildi laadimine ja suuruse muutmine
seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, [254, 305])

# Poemüüja kuvamine ekraanil koordinaatidega [105, 159]
screen.blit(seller, [105, 159])


# Jutumulli pildi laadimine ja suuruse muutmine
chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [258, 202])

# Jutumulli kuvamine ekraanil koordinaatidega [245, 66]
screen.blit(chat, [245, 66])


# Teksti font ja renderdamine
font = pygame.font.Font(None, 30)
text = font.render("Tere, olen Erki Kütt ", True, (255, 255, 255))

# Teksti kuvamine ekraanil koordinaatidega [280, 145]
screen.blit(text, [280, 145])


# Mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Ekraani värskendamine
    pygame.display.flip()



# Mängu lõpetamine
pygame.quit()