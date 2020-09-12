from manimlib.imports import *
class L20(GraphScene, Scene):
	def construct(self):
		z_color = BLUE_B
		s_color = ORANGE
		t_color = "#f9e79f"
		text1 = TextMobject("Let's visualize how s-transform and z-transform are related")
		text1.to_edge(UP)
		text1.set_color(t_color)
		text1.scale(0.7)
		text2 = TextMobject("$|z|$=1 circle corresponds to the imaginary axis in s-plane")
		text2.to_edge(UP)
		text2.set_color(t_color)
		text2.scale(0.5)
		text3 = TextMobject("when $\\omega$ = -$\\pi$ on the circle, s = -$\\infty$ on imaginary axis in s-plane")
		text3.to_edge(UP)
		text3.set_color(t_color)
		text3.scale(0.5)
		text4 = TextMobject("when $\\omega$ = 0 on the circle, s = 0 on imaginary axis in s-plane ")
		text4.to_edge(UP)
		text4.set_color(t_color)
		text4.scale(0.5)
		text41 = TextMobject("so lower semicircle corresponds to lower half of imaginary axis")
		text41.to_edge(UP)
		text41.set_color(t_color)
		text41.scale(0.5)
		text5 = TextMobject("when $\\omega$ = $\\pi$ on the circle, s = +$\\infty$ on imaginary axis in s-plane ")
		text5.to_edge(UP)
		text5.set_color(t_color)
		text5.scale(0.5)
		text6 = TextMobject("in this way whole circle $|z|=1$ corresponds to the complete imaginary axis")
		text6.to_edge(UP)
		text6.set_color(t_color)
		text6.scale(0.5)
		text7 = TextMobject("What if $|z|<1$?......the radius of circle is reduced essentially")
		text7.to_edge(UP)
		text7.set_color(t_color)
		text7.scale(0.5)
		text8 = TextMobject("$|z|^2 = \\left(\\frac{1+Re(s)}{1-Re(s)}\\right)^2$(derived in summary)")
		text8.to_edge(UP)
		text8.set_color(t_color)
		text8.scale(0.5)
		text9 = TextMobject("In this way the left-half s-plane maps to $|z|<1$ region")
		text9.to_edge(UP)
		text9.set_color(t_color)
		text9.scale(0.5)
		text10 = TextMobject("Similarly right-half s-plane maps to $|z|>1$ region")
		text10.to_edge(UP)
		text10.set_color(t_color)
		text10.scale(0.5)
		left_text = TextMobject("s-plane")
		left_text.set_color(s_color)
		left_text.to_edge(UP+LEFT)
		right_text = TextMobject("z-plane")
		right_text.set_color(z_color)
		right_text.to_edge(UP+RIGHT)
		axis1 = Axes(
		    x_min = -5,
		    x_max = 5,
		    y_min = -5,
		    y_max = 5,
        	axes_color = GREY_BROWN,
		    x_labelled_nums = list(range(-10,11)),
		    y_labelled_nums = [-1,1],
		    center_point = 3*LEFT,
		    x_axis_config={
		        "unit_size": 0.5,
		        "tick_frequency": 1,
		        "include_tip": False,
		        "label_direction": DOWN+0.5*LEFT
		    },
		    y_axis_config={
		            "unit_size": 0.5,
		            "tick_frequency": 1,
		            "include_tip": False,
		    })
		axis2 = Axes(
		    x_min = -5,
		    x_max = 5,
		    y_min = -5,
		    y_max = 5,
        	axes_color = GREY_BROWN,
		    x_labelled_nums = list(range(-10,11)),
		    y_labelled_nums = [-1,1],
		    center_point = 3*RIGHT,
		    x_axis_config={
		        "unit_size": 0.5,
		        "tick_frequency": 1,
		        "include_tip": False,
		        "label_direction": DOWN+0.5*LEFT
		    },
		    y_axis_config={
		            "unit_size": 0.5,
		            "tick_frequency": 1,
		            "include_tip": False,
		    })
		o = 3*RIGHT
		s = 0.5*RIGHT
		y = 0.5*UP
		dot1 = Dot()
		dot1.move_to(2.5*RIGHT)
		circ = ParametricFunction(
			lambda t:o+s*np.cos(t)+y*np.sin(t),
			t_min = -PI,
			t_max = 0,
			step_size = PI/20)
		circ.set_color(z_color)
		circ2 = ParametricFunction(
			lambda t:o+s*np.cos(t)+y*np.sin(t),
			t_min = 0,
			t_max = PI,
			step_size = PI/20)
		circ2.set_color(z_color)
		f = 0.9
		circ3 = ParametricFunction(
			lambda t:o+f*s*np.cos(t)+f*y*np.sin(t),
			t_min = -PI,
			t_max = PI,
			step_size = PI/20)
		circ3.set_color(z_color)
		f=0.8
		circ4 = ParametricFunction(
			lambda t:o+f*s*np.cos(t)+f*y*np.sin(t),
			t_min = -PI,
			t_max = PI,
			step_size = PI/20)
		circ4.set_color(z_color)
		f=0.7
		circ5 = ParametricFunction(
			lambda t:o+f*s*np.cos(t)+f*y*np.sin(t),
			t_min = -PI,
			t_max = PI,
			step_size = PI/20)
		circ5.set_color(z_color)
		f=0.3
		circ6 = ParametricFunction(
			lambda t:o+f*s*np.cos(t)+f*y*np.sin(t),
			t_min = -PI,
			t_max = PI,
			step_size = PI/20)
		circ6.set_color(z_color)
		dot2 = Dot()
		dot2.move_to(-10*y*UP)
		line = ParametricFunction(
			lambda t:-o+y*t,
			t_min = -10,
			t_max = 0,
			step_size=.1)
		line.set_color(s_color)
		line2 = ParametricFunction(
			lambda t:-o+y*t,
			t_min = 0,
			t_max = 10,
			step_size=.1)
		line2.set_color(s_color)
		f=0.4*RIGHT
		line3 = ParametricFunction(
			lambda t:-o+y*t-f,
			t_min = -10,
			t_max = 10,
			step_size=.1)
		line3.set_color(s_color)
		f=1*RIGHT
		line4 = ParametricFunction(
			lambda t:-o+y*t-f,
			t_min = -10,
			t_max = 10,
			step_size=.1)
		line4.set_color(s_color)
		f=2.2*RIGHT
		line5 = ParametricFunction(
			lambda t:-o+y*t-f,
			t_min = -10,
			t_max = 10,
			step_size=.1)
		line5.set_color(s_color)
		f=4.0*RIGHT
		line6 = ParametricFunction(
			lambda t:-o+y*t-f,
			t_min = -10,
			t_max = 10,
			step_size=.1)
		line6.set_color(s_color)
		kwargs = {
		"run_time" : 5
		}
		circ_f = Circle(radius = 0.5*1,color=z_color,fill_color=z_color,fill_opacity=0.5)
		circ_f.move_to(3*RIGHT)
		rect_f = Rectangle(color=s_color,height=20,width=8,fill_color=s_color,fill_opacity=0.5)
		rect_f2 = Rectangle(color=s_color,height=20,width=0.5*5,fill_color=s_color,fill_opacity=0.5,stroke_width=0)
		rect_f.move_to(7*LEFT)
		self.play(ShowCreation(axis1),ShowCreation(axis2),ShowCreation(text1),ShowCreation(left_text),ShowCreation(right_text))
		self.wait(3)
		self.play(ReplacementTransform(text1,text2))
		self.wait(3)
		self.play(ReplacementTransform(text2,text3))
		self.play(ShowCreation(dot1),ShowCreation(dot2))
		self.wait(3)
		self.play(ReplacementTransform(text3,text4))
		self.play(MoveAlongPath(dot1,circ,**kwargs),MoveAlongPath(dot2,line,**kwargs))
		self.wait(2)
		self.play(ShowCreation(circ),ShowCreation(line),run_time = 5)
		self.play(ReplacementTransform(text4,text41))
		self.wait(3)
		self.play(ReplacementTransform(text41,text5))
		self.wait(3)
		self.play(MoveAlongPath(dot1,circ2,**kwargs),MoveAlongPath(dot2,line2,**kwargs))
		self.wait(2)
		self.play(ShowCreation(circ2),ShowCreation(line2),run_time = 5)
		self.play(ReplacementTransform(text5,text6))
		self.wait(3)
		self.play(ReplacementTransform(text6,text7))
		self.wait(4)
		self.remove(dot1,dot2)
		self.play(ReplacementTransform(text7,text8))
		self.wait(3)
		self.play(ShowCreation(circ3),ShowCreation(line3),run_time = 5)
		self.wait()
		self.play(ShowCreation(circ4),ShowCreation(line4),run_time = 5)
		self.wait()
		self.play(ShowCreation(circ5),ShowCreation(line5),run_time = 5)
		self.wait()
		self.play(ShowCreation(circ6),ShowCreation(line6),run_time = 5)
		self.wait()
		self.play(ReplacementTransform(text8,text9))
		self.wait(3)
		self.remove(circ,circ2,circ3,circ4,circ5,circ6,line,line2,line3,line4,line5,line6)
		self.play(FadeIn(circ_f),FadeIn(rect_f),run_time = 5)
		self.wait()
		self.play(ReplacementTransform(text9,text10))
		self.wait(3)
		self.remove(circ_f,rect_f)
		annu = Annulus(inner_radius=0.5*1,outer_radius=0.5*5,stroke_width=0,fill_color=z_color,fill_opacity=0.5)
		annu.move_to(3*RIGHT)
		rect_f2.move_to(3*LEFT+2.5*0.5*RIGHT)
		self.play(FadeIn(annu),FadeIn(rect_f2),run_time = 5)
		self.wait()




