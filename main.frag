#version 460
layout(location = 0) out vec4 fragColor;
in vec2 mytexture;
in float intensity_light;
uniform sampler2D tex;

void main()
{
  fragColor = intensity_light*1.5*texture(tex,mytexture);
}
