ffmpeg -framerate 30 -pattern_type glob -i '*.png' -vf "scale=320:320" -c:v libx264 -pix_fmt yuv420p out.mp4
