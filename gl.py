# Lab4 graficas
# Jessica Ortiz 20192


import numpy
from OpenGL.GL import *
import glm
from shaders import *
from obj import *


def prepare_data(shader,t_data,width, height):

  texture = glGenTextures(1)
  glBindTexture(GL_TEXTURE_2D, texture)
  glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, t_data)
  glGenerateMipmap(GL_TEXTURE_2D)

#cargamos el modelo
  model = Obj('oreo.obj')

  vertices = []
  texture = []
  norm = []
  for face in (model.faces):
            for v in range(len(face)):
                vertices.append((model.vertices[face[v][0]-1]))
                texture.append((model.texcoords[face[v][1]-1]))

                norm.append((model.normals[face[v][2]-1]))

  vertex_data = numpy.hstack([
    numpy.array(vertices, dtype=numpy.float32),
    numpy.array(texture, dtype=numpy.float32),
    numpy.array(norm, dtype=numpy.float32)
  ])

  vertex_buffer_object = glGenBuffers(1)
  glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
  glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)


  vertex_array_object = glGenVertexArrays(1)
  glBindVertexArray(vertex_array_object)

  #Vertices
  glVertexAttribPointer(
    #posicion inicial
    0,
    #tamaño
    4,
    #tipo
    GL_FLOAT,
    #normalizados
    GL_FALSE,
    #stride
    4 * 8,
    ctypes.c_void_p(0)
  )
  glEnableVertexAttribArray(0)


  glVertexAttribPointer(
    1, 
    2,
    GL_FLOAT,
    GL_FALSE,
    4 * 8,
    ctypes.c_void_p(4*3)
  )
  glEnableVertexAttribArray(1)

  #Normales
  glVertexAttribPointer(
    #posicion inicial
    2,
    #tamaño
    4,
    #tipo
    GL_FLOAT,
    #normalizados
    GL_FALSE, 
    #stride
    4 * 8,
    ctypes.c_void_p(4*5)
  )
  glEnableVertexAttribArray(2)

  #definiendo shader
  glUseProgram(shader)
  glDrawArrays(GL_TRIANGLES,0,len(vertex_data))

#Matrices
def renderMatrix(a2,shader,pos_x,pos_y,pos_z):
  i = glm.mat4(1)
  light = glm.vec3(-160,280,4)
  #modelo obj
  translate = glm.translate(i, glm.vec3(0,0,3.5))
  scale = glm.scale(i, glm.vec3(0.007,0.007,0.007))
  rotate = glm.rotate(i, 0,glm.vec3(glm.radians(pos_x),glm.radians(pos_y),glm.radians(pos_z)))
  model = translate * rotate * scale


  #view
  view = glm.lookAt(
    #posicion
    glm.vec3(pos_x,pos_y,pos_z),
    glm.vec3(0,0,0),
    glm.vec3(0,0.5,0)
  )

  projection = glm.perspective(glm.radians(55), 1200/720, 0.1, 100.0)
  theMatrix = projection * view * model

  #Viewport
  glViewport(0, 0, 800, 600)
  glUniformMatrix4fv(glGetUniformLocation(shader, "theMatrix"), 1, GL_FALSE, glm.value_ptr(theMatrix))
  glUniform3f(glGetUniformLocation(shader, "light"), light.x, light.y, light.z)
  glUniform1i(glGetUniformLocation(shader, "time"), a2)

