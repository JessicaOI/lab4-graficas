#version 460

layout(location = 0) out vec4 fragColor;
in vec2 mytexture;
in vec4 posi;
uniform sampler2D tex;
uniform int time;
in float intensity_light;


void main()
{
    vec4 neg = vec4(1.0, 1.0, 1.0, 1.0);
    fragColor = texture(tex, mytexture);
    fragColor = neg - texture(tex, mytexture);

}