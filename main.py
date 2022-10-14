# Import thư viện sử dụng
import pygame as pg
import random
from sprites import *
from thongsogame import *
from os import path


class Game:
    def __init__(self):
        # Khởi tạo màn hình game,...
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

        self.running = True
        self.font_name = pg.font.match_font('inkfree',bold=True)
        self.load_data()

    def load_data(self):
        # Điểm cao
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_File), 'w') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        # Âm thanh
        # self.snd_dir = path.join(self.dir, 'sound')
        # self.go_sound = pg.mixer.Sound(path.join(self.snd_dir,'GO.wav'))
        # self.boost_sound = pg.mixer.Sound(path.join(self.snd_dir,'Boost.wav'))

    def new(self):
        # Bắt đầu

        self.score = 0
        self.all_sprites = pg.sprite.Group()

        self.ball = Ball(self)
        self.all_sprites.add(self.ball)

        self.nail = Nail(0, 0)
        self.all_sprites.add(self.nail)

        self.plat = pg.sprite.Group()
        for plat in PlAT_LIST:
            p = Plat(*plat)
            self.all_sprites.add(p)
            self.plat.add(p)
        self.star = pg.sprite.Group()
        for str in STAR_LIST:
            s = Star(*str)
            self.all_sprites.add(s)
            self.star.add(s)
        self.crack = pg.sprite.Group()
        for crack in CRACK_LIST:
            cr = Crack(*crack)
            self.all_sprites.add(cr)
            self.crack.add(cr)
        # pg.mixer.music.load(path.join(self.snd_dir,'Background.wav'))
        self.run()

    def run(self):
        # Vòng lặp game
        # pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        # pg.mixer.music.fadeout(500)

    def update(self):
        # Vòng lặp game - Cập nhật
        self.all_sprites.update()
        # Kiểm tra bóng khi va chạm với nền đất
        if self.ball.vel.y > 0:
            hits = pg.sprite.spritecollide(self.ball, self.plat, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.ball.pos.y < lowest.rect.bottom:
                    self.ball.pos.y = lowest.rect.top
                    self.ball.vel.y = 0


        # if self.ball.vel.y > 0:
        #     hits2 = pg.sprite.spritecollide(self.ball, self.star, True)
        #     if hits2:
        #         self.score += 300

        pg.sprite.groupcollide(self.plat,self.crack,True,False)
        pg.sprite.groupcollide(self.plat, self.star, True, False)
        pg.sprite.groupcollide(self.star, self.crack, True, False)

        # Create new plat
        for plat in self.plat:
            if plat.rect.y < 0:
                plat.kill()

        while len(self.plat) < 6:
            width = random.randrange(50, 100)
            p = Plat(random.randrange(0, WIDTH - width),
                     random.randrange(1049, 1094, 45))
            self.plat.add(p)
            self.all_sprites.add(p)

        for st in self.star:
            if st.rect.y < 0:
                st.kill()
        while len(self.star) < 2:
            width = random.randrange(50, 100)
            s = Star(random.randrange(0, WIDTH - width),
                      random.randrange(1049, 1094, 45))
            self.star.add(s)
            self.all_sprites.add(s)

        # Create new crack
        for crack in self.crack:
            if crack.rect.y < 0:
                crack.kill()
        while len(self.crack) < 2:
            width = random.randrange(50, 100)
            cr = Crack(random.randrange(0, WIDTH - width),
                       random.randrange(1049, 1124, 45))
            self.crack.add(cr)
            self.all_sprites.add(cr)

        # Scored
        if self.ball.vel.y != 0:
            self.score += 1
        for pl in self.plat:
            if pl.rect.top <= 0:
                pl.kill()

        # Xử lý va chạm
        hit2 = pg.sprite.spritecollide(self.ball, self.crack, False)
        if hit2:
            # self.go_sound.play()
            self.playing = False
            # self.go_sound.fadeout(2000)

        hit2 = pg.sprite.spritecollide(self.ball, self.star, True)
        if hit2:
            self.score += 100
            # self.boost_sound.play()
            # self.go_sound.fadeout(2000)

        # GO!
        if self.ball.rect.bottom > HEIGHT:
            # for sprite in self.all_sprites:
            #     sprite.rect.y += max(self.ball.vel.y, 10)
            #     if sprite.rect.bottom < 0:
            #         sprite.kill()
            # if (len(self.plat) & len(self.crack)) != 0:
            # self.go_sound.play()
            # self.go_sound.fadeout(2000)
            self.playing = False

        self.all_sprites.update()

        # Xử lý va chạm với thép gai
        if self.ball.rect.top < self.nail.rect.bottom:
            # for sprite in self.all_sprites:
            #     sprite.rect.y += max(self.ball.vel.y, 10)
            #     if sprite.rect.bottom < 0:
            #         sprite.kill()
            # if (len(self.plat) & len(self.crack)) != 0:
            self.go_sound.play()
            self.go_sound.fadeout(2000)
            self.playing = False

        self.all_sprites.update()

    def events(self):
        # Vòng lặp game - các events trong game
        for event in pg.event.get():
            # Kiểm tra tắt cửa sổ game
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if self.score > self.highscore:
                self.highscore = self.score


    def draw(self):

        # Vòng lặp game - Vẽ chuyển động
        self.screen.fill('LIGHTBLUE')
        self.draw_text('Score: ' + str(self.score), 22, (0, 0, 0), 50, 40)
        self.draw_text('High Score: ' + str(self.highscore), 22, (0, 0, 0), 500, 40)
        # self.screen.blit(background,(0,0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        # Màn hình tạm dừng,khởi động game
        self.screen.fill('LIGHTBLUE')
        self.draw_text(TITLE, 50, black, WIDTH / 2, HEIGHT / 4)
        self.draw_text('<- to Left -> to Right', 25, black, WIDTH / 2, HEIGHT / 2)
        self.draw_text('STAR = 100 points', 20, black, WIDTH / 2, HEIGHT / 2 + 100)
        self.draw_text('Press Any key to play', 22, black, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text('High Score:' + str(self.highscore), 22, black, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # Màn hình kết thúc, tiếp tục game
        if not self.running:
            return
        self.screen.fill('LIGHTBLUE')
        self.draw_text('GAME OVER!!!', 50, black, WIDTH / 2, HEIGHT / 4)
        self.draw_text('Score: ' + str(self.score), 25, black, WIDTH / 2, HEIGHT / 2)
        self.draw_text('Press Any key to play again', 22, black, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text('New High score:', 22, black, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_File), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text('High Score:' + str(self.highscore), 22, black, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
