import random
import glob
import gizeh as gz  # type: ignore
from numpy.random import choice
from moviepy.editor import ImageClip, TextClip, ColorClip, VideoClip, VideoFileClip  # type: ignore


# from https://zulko.github.io/blog/2014/09/20/vector-animations-with-python/
def make_frame(t):
    W, H = 200, 75
    D = 3
    r = 10  # radius of the ball
    DJ, HJ = 50, 35  # distance and height of the jumps
    ground = 0.75 * H  # y-coordinate of the ground

    gradient = gz.ColorGradient(type="radial",
                                stops_colors=[(0, (1, 0, 0)), (1, (0.1, 0, 0))],
                                xy1=[0.3, -0.3], xy2=[0, 0], xy3=[0, 1.4])

    surface = gz.Surface(W, H, bg_color=(1, 1, 1))
    x = (-W / 3) + (5 * W / 3) * (t / D)
    y = ground - HJ * 4 * (x % DJ) * (DJ - (x % DJ)) / DJ ** 2
    coef = (HJ - y) / HJ
    shadow_gradient = gz.ColorGradient(type="radial",
                                       stops_colors=[(0, (0, 0, 0, .2 - coef / 5)), (1, (0, 0, 0, 0))],
                                       xy1=[0, 0], xy2=[0, 0], xy3=[0, 1.4])
    shadow = (gz.circle(r=(1 - coef / 4), fill=shadow_gradient)
              .scale(r, r / 2).translate((x, ground + r / 2)))
    shadow.draw(surface)
    ball = gz.circle(r=1, fill=gradient).scale(r).translate((x, y))
    ball.draw(surface)
    return surface.get_npimage()


static_media = lambda t: f'../static/{t}'
image_files = glob.glob(static_media('image/*'))
video_files = glob.glob(static_media('video/*'))
print(image_files, video_files)
random_image = choice(image_files)
random_video = choice(video_files)
sample_texts = ["wingardium leviosa", "🥰🥰🥰🥰", "E=mc^2", "haha"]

random_int = random.randrange(0, 255)
random_rgb = [random_int, random_int, random_int]
random_length = lambda: random.randrange(1, 100)
random_size = (random_length(), random_length())
random_text = lambda: choice(sample_texts)

random_square_args = {
    'size': random_size,
    'color': random_rgb,
    'duration': random.randint(1, 5)
}

random_text_args = {
    'fontsize': random.randrange(8, 60, 4),
    'font': choice(TextClip.list('font')),
    'color': choice(TextClip.list('color')[3:]),
    'duration': random.randint(1, 5)
}

vector_anim_args = {
    'make_frame': make_frame
}

hardcoded_layers = [
    (VideoFileClip, random_video),
    (ImageClip, random_image),
    (TextClip, random_text(), random_text_args),
    # (ColorClip, random_square_args),
    # (VideoClip, make_frame)
]
