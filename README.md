<h1>
Housekeeper - <br><i>Optimize Toontown Textures</i>
</h1>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


**About**

This project started out as a fork of [this](https://github.com/RyanAWalters/PowerOf2ImageResizer) repository, but I ended up changing the original so much that I wanted to make a whole new program out of it.

This program was written to assist in Toontown projects, including server resources and content packs. It aims to eliminate common export errors en masse, such as
- Fixing textures with non power of two resolutions
- Embedded ICC profiles (Doesn't do much but makes Panda angry)
- Detects color profiles that aren't RGB/RGBA, such as Index
- Optimization feature

---

Description from the original author with some slight edits is below:

This program resizes images to a power of 2 `(256, 512, 1024, 2048, etc.)`. Many game engines cannot use textures without them being a power of 2. Some game engines will use them with poor optimization and limited features. For example, in Unreal Engine, textures that are not a power of 2 cannot use texture streaming and will appear horribly jarring from a distance.
This program will take an image, find the closest power of 2 (using a user-defined threshold), and resize that image. So an image that is 1080x1200 would be resized (stretched in this case - images are never cut or cropped) to 1024x1024. Then they are ready to be used in a game engine.

As images are not cut or cropped, seamless textures will still be seamless, so no worries. 

I made this program for my own use, as when working on game projects, I stumbled across thousands of wonderful free textures. The problem was that basically none of them were power of 2. Some would be 1000x1000 or 1200x1200 for example. So I found myself constantly opening bulky image editing programs, navigating through menus, finding the image resizing tool, manually typing in the new dimensions, and saving it. The whole process taking around 10 clicks and 30 seconds per file (if I was going fast). Going through hundreds of these, let alone thousands, is tedious, mind and finger numbing, and time-consuming. This takes care of everything for you *automatically!*

**Supported Image Types:**
* JPG
* PNG

This program is written in Python and uses [Pillow](https://github.com/python-pillow/Pillow) 


Compression is just the level of compression to apply. PIL's default is 6. The default here is 5. 0 is no compression at all (although metadata will still say the file is compressed, I promise it's not!). Compression does not apply to TGA files, as they are always saved uncompressed. Range is from 0-9

**License**
---
MIT License

Copyright (c) 2017 Ryan Andrew Walters

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
