# Lab4 graficas
# Jessica Ortiz 20192


from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

#lee los archivos
def read_shader_file(file):
  with open(file) as f:
    return f.read()

#obtiene el shader del archivo leido
def get_shader(shader):
  vertex_data = read_shader_file("vertex.vert")
  fragment_shader = read_shader_file(f"{shader}")
  cvs = compileShader(vertex_data, GL_VERTEX_SHADER)
  cfs = compileShader(fragment_shader, GL_FRAGMENT_SHADER)

  shader = compileProgram(cvs, cfs)
  return shader
