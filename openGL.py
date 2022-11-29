# Lab4 graficas
# Jessica Ortiz 20192


import pygame
from OpenGL.GL import *
from math import sin
from gl import *
from shaders import *


pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
max_cam = 3
min_cam = -1

#zbuffer
glEnable(GL_DEPTH_TEST)
glEnable(GL_TEXTURE_2D)
clock = pygame.time.Clock()

texture = pygame.image.load('Oreo.bmp')
t_data = pygame.image.tostring(texture, "RGB", 1)
width = texture.get_width()
height = texture.get_height()


angle2 = 0
running = True

shader = get_shader('main.frag')
pos_x,pos_y,pos_z = 1,1,5

while running:
  glClearColor(1, 1,1, 1.0)
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  #aqui le aplica la textura al object
  glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
  angle2 +=1

  prepare_data(shader,t_data,width,height)
  renderMatrix(angle2,shader,pos_x,pos_y,pos_z)

  pygame.display.flip()

  #movimientos de la camara y teclas designados a los shaders
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_1:
          shader = get_shader('exampleShader.frag')

      if event.key == pygame.K_2:
          shader = get_shader('exampleShader2.frag')
      
      if event.key == pygame.K_3:
          shader = get_shader('main.frag')

      if event.key == pygame.K_w or event.key == pygame.K_UP:
          if(pos_y+0.1<=max_cam and pos_y+0.1 >=min_cam):
              pos_y += 0.1

      if event.key == pygame.K_s or event.key == pygame.K_DOWN:
          if(pos_y-0.1<=max_cam and pos_y-0.1 >=min_cam):
              pos_y -= 0.1
      if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
          if(pos_x+0.1<=max_cam and pos_x+0.1 >=min_cam):
              pos_x += 0.1

      if event.key == pygame.K_a or event.key == pygame.K_LEFT:
          if(pos_x-0.1<=max_cam and pos_x-0.1 >=min_cam):
              pos_x -= 0.1
