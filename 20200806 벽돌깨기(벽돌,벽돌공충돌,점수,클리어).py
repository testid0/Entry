import pygame as p

p.init()
w =(255,255,255)
size = (600,800)
sc = p.display.set_mode(size)
p.display.set_caption("벽돌깨기")
playing = True
#판생성 
pan = p.image.load("pan.png")
p_rect = pan.get_rect(left = 245, top = 725)
px = 0
#배경생성
bg = p.image.load("bg3.png")
#공생성 
bl = p.image.load("ball.png")
bl_rect = bl.get_rect(left = 270, top = 370)
#공 스피드 
bx=2
by=2
#게임오버
font = p.font.SysFont("malgungothic",50)
#벽돌
block = p.image.load("block.png")
block_list = []
for x in range(10):
    for y in range(5):
        blo_rect = block.get_rect(left= 60*x, top = 50*y)
        block_list.append(blo_rect)
        
font2 = p.font.SysFont("malgungothic",25)
score = 0

while playing:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                px = -5
            if event.key == p.K_RIGHT:
                px = 5
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                px = 0
            if event.key == p.K_RIGHT:
                px = 0
                
    p_rect.left += px

    sc.fill(w)
    sc.blit(bg,(0,0))
    sc.blit(pan,p_rect)
    
    if p_rect.left >= 500:
        p_rect.left = 500
    if p_rect.left <= 0:
        p_rect.left = 0
    sc.blit(bl,bl_rect)

    bl_rect.top += by
    bl_rect.left += bx
    if bl_rect.top >=770:
        by = -by  
    if bl_rect.top <=10:
        by = -by
    if bl_rect.left >=550:
        bx = -bx
    if bl_rect.left <=10:
        bx = -bx        
    if bl_rect.top >=770:
        sc.blit(text,(200,400))
        playing = False

    text = font.render("Game Over",True,(102,0,102))
    text2 = font2.render("점수: {}".format(score),True,(255,255,0))
    text3 = font.render("Clear",True,(0,255,0))

    if p_rect.colliderect(bl_rect):
        by = -2
    for blo_rect in block_list:
        sc.blit(block,blo_rect)
        
    #공이랑 벽 충돌했을때 
    for blo_rect in block_list:
        if bl_rect.colliderect(blo_rect):
            by = 2
            block_list.remove(blo_rect)
    
    sc.blit(text2,(0,760))

    if len(block_list) <= 10:
        sc.blit(text3,(200,400))
        playing = False
    
        
    p.display.flip()
