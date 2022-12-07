from manim import *
class BeamScene(Scene):
    def construct(self):
        beam=VMobject()
        dots=self.get_dots(6)
        points= np.array(list(map(Mobject.get_center,dots)))
        beam.set_points_as_corners(points)
        anims=[
            self.get_beam_anim(beam)
        ]
        self.play(Create(dots))
        self.play(*anims)
        self.wait()
        func=lambda t: t[0]*UL+t[1]*DR
        stream_line=StreamLines(func, max_anchors_per_line=20)
        self.add(stream_line)
        stream_line.start_animation(
            warm_up=False,
            flow_speed=1.5
        )
        self.wait(stream_line.virtual_time/stream_line.flow_speed)
        self.play(FadeOut(stream_line))
    def get_dots(self,num):
        dots=VGroup(*[
            Dot() for _ in range(num**2)
        ]).arrange_in_grid(col=num, row=num)
        return dots
    def get_beam_anim(self,beam):
        return AnimationGroup(
            ShowPassingFlash(
                beam,
                run_time=5,
                rate_func=lambda t: smooth(t,5),
                time_width=0.07
            ),
        )
class BeamScene2(Scene):
    def construct(self):
        box=Square(side_length=4)
        