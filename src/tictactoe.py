import datetime, random, pygame, sys, time

class Player: 
        'This is a player yo!'

        def __init__(self, name, players, move): 
            self.move = move
            self.score = 0
            self.name = name
            for player in players:
                if(player.hasName(name)): 
                    self.name += str(int(random.random()*10000))

        def __str__(self): 
            return self.name + " - Score:" + str(self.score)

        def increaseScore(self):
            self.score += 1

        def displayPlayer(self):
            print(self)
        
        def hasName(self, name):
            return self.name == name

class Game: 
    'This is supposed to represent a game with two players and a board with states'
    
    def __init__(self, player1, player2):
        self.board = [[0]*3 for i in range(3)]
        self.player1 = player1
        self.player2 = player2

class GameUI: 
    
    def __init__(self): 
        


    def setupGameBoard(self):
        pygame.init()
        size = width, height = 1280, 720
        screen = pygame.display.set_mode(size)

        topRatio = 2/7
        bottomRatio = 5/7

        gameColor = pygame.Color(83, 178, 162)
        menuColor = pygame.Color(247, 247, 247)
        borderColor = pygame.Color(144, 148, 150)
        #247x3
        gameArea = screen.subsurface(screen.fill(gameColor, pygame.Rect(0, screen.get_height()*topRatio, screen.get_width(), screen.get_height()*bottomRatio)))
        gameMenu = screen.subsurface(screen.fill(menuColor, pygame.Rect(0, 0, screen.get_width(), screen.get_height()*topRatio)))
        border   = pygame.draw.line(screen, borderColor, (0, screen.get_height()*topRatio), (screen.get_width(), screen.get_height()*topRatio), 3)

        return screen, gameArea, gameMenu


players = []
p1 = Player("Filip", players, 1)
players.append(p1)
p2 = Player("Filip", players, -1)
players.append(p2)
game = Game(p1, p2)

pygame.init()
screen, gameArea, gameMenu = setupGameBoard()

start_time = time.time()
while 1: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if time.time()-start_time > 1:
        pygame.display.flip()
        start_time = time.time()
