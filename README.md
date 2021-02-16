# FF XV 4K Movie Enabler  
This script enables 4K movies for any screen resolution. The additional 4K resource pack that comes free with the game adds 4K movies. The default movies are 1080p. For some reason, the game will try to play default movies on 1080p or 1440p monitors even if the user has the resource pack activated. FF XV 4K Movie Enabler will switch 4K files with the default ones. Therefore, the game will always play 4K movies.  

# Usage  
```
python 4k_movie_enabler.py "<ff_xv_root>"
```

Please make sure to add the game root path argument in quotes since the default game folder name contains spaces.  

# Warnings
This script hasn't been tested in 4K screens. If the user has the resource pack activated and plays in 4K resolution, the result is untested. The game will either default to 1080p movies (which will be 4K after the script runs so nothing weird will happen), or it will skip them since it doesn't find the files. Or it might just crash, of course.