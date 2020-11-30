for event in pygame.event.get():
    if event.type == pygame.QUIT:
        finished = True
    elif event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if what_field_is(x, y) == 1:
            player_name = 'player'
        else:
            player_name = 'bot'
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:   '''нажата ЛКМ - событие связано с бомбой'''
            if player_name != 'bot':
                player_name.catch(x, y)
            else:
                player_name.bomb(x, y)
        if pressed[2]:   '''нажата ПКМ - событие связано с полем'''
            if player_name == 'player':
                player_name.repair(x, y)
            
            
