This is a little tool I made for converting 3D LUTs stored as tiles in a 2D image into a 3D binary file. My use case is for cloud noise which I use in my Minecraft shader, [glint](https://github.com/jbritain/glint-shaders). (this repo is not yet public but will be once the shader is in a state I'm happy with)

Currently the program makes the following assumptions.
- The resulting LUT should be cubic, i.e all three axes have the same resolution
- The output texture is in the order x,y,z

If you're implementing this into a minecraft shader, your texture definition in `shaders.properties` will be something like

```properties
TEXTURE_3D RG8 32 32 32 RG UNSIGNED_BYTE
```

In this case, I have a 32x32x32 LUT and am using the R and G channels.