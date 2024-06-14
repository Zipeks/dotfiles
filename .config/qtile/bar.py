from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep

def search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = [widget_defaults.copy()]
colors = ['#282738',
          '#353446',
          '#CAA9E0',
          '#4B427E',
          '#f7b5df'
          ]

from spotify import Spotify
def spawn_bar():
    return [

    Screen(
        top=bar.Bar(
            [
				widget.Spacer(length=15,
                    background=colors[0],
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background=colors[0],
                    mouse_callbacks={"Button1":power},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),


                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='line',
                    active=colors[2],
                    block_highlight_text_color="#91B1F0",
                    highlight_color=colors[3],
                    inactive=colors[0],
                    foreground=colors[3],
                    background=colors[1],
                    this_current_screen_border=colors[1],
                    this_screen_border=colors[1],
                    other_current_screen_border=colors[4],
                    other_screen_border=colors[4],
                    urgent_border=colors[1],
                    rounded=True,
                    disable_drag=True,
                ),


                widget.Spacer(
                    length=8,
                    background=colors[1],
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background=colors[1]
                ),


                widget.CurrentLayout(
                    background=colors[1],
                    foreground=colors[2],
                    fmt='{}',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),
                


                widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background=colors[0],
                    mouse_callbacks={"Button1": search},
                ),

                widget.TextBox(
                    fmt='Search',
                    background=colors[0],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground=colors[2],
                    mouse_callbacks={"Button1": search},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),


                widget.WindowName(
                    background = colors[1],
                    format = "{name}",
                    font='JetBrains Mono Bold',
                    foreground=colors[2],
                    empty_group_string = 'Desktop',
                    fontsize=13,
                    border =colors[0] 

                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),

                Spotify(
                    background = colors[1],
                    foreground=colors[2],
                    font="JetBrains Mono Bold",
                    fontsize=13,),
                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),
                widget.Systray(
                    background=colors[0],
                    fontsize=2,
                ),


                widget.TextBox(
                    text=' ',
                    background=colors[0],
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background=colors[1],
                ),


                widget.Image(
                filename='~/.config/qtile/Assets/Drop1.png',
                ),

                # widget.Net(
                # format=' {up}   {down} ',
                # background=colors[1],
                # foreground=colors[2],
                # font="JetBrains Mono Bold",
                # prefix='k',
                # ),

                # widget.Image(
                #     filename='~/.config/qtile/Assets/2.png',
                # ),

                # widget.Spacer(
                    # length=8,
                    # background=colors[1],
                # ),
                

                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background=colors[1],
                ),


                widget.Spacer(
                    length=-7,
                    background=colors[1],
                ),


                widget.Memory(
                    background=colors[1],
                    format='{MemUsed: .0f}{mm}',
                    foreground=colors[2],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),


                # widget.Image(
                # filename='~/.config/qtile/Assets/Drop2.png',
                # ),



                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background=colors[1],
                ),
                


                # widget.BatteryIcon(
                #     theme_path='~/.config/qtile/Assets/Battery/',
                #     background=colors[1],
                #     scale=1,
                # ),


                # widget.Battery(
                #     font='JetBrains Mono Bold',
                #     background=colors[1],
                #     foreground=colors[2],
                #     format='{percent:2.0%}',
                #     fontsize=13,
                # ),


                # widget.Image(
                #     filename='~/.config/qtile/Assets/2.png',
                # ),


                widget.Spacer(
                    length=8,
                    background=colors[1],
                ),


                # widget.Battery(format=' {percent:2.0%}',
                    # font="JetBrains Mono ExtraBold",
                    # fontsize=12,
                    # padding=10,
                    # background=colors[1],
                # ),                

                widget.Volume(
                    font='JetBrainsMonwo monitorso Nerd Font',
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    fontsize=13,
                    background=colors[1],
                ),


                widget.Spacer(
                    length=-5,
                    background=colors[1],
                    ),


                widget.Volume(
                    font='JetBrains Mono Bold',
                    background=colors[1],
                    foreground=colors[2],
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background=colors[1],
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background=colors[0],
                    margin_y=6,
                    margin_x=5,
                ),


                widget.Clock(
                    format='%d.%m.%Y %a %H:%M',
                    background=colors[0],
                    foreground=colors[2],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),


                widget.Spacer(
                    length=18,
                    background=colors[0],
                ),



            ],
            30,
            border_color = colors[0],
            border_width = [0,0,0,0],
            margin = [5,5,5,5],

        ),
    ),Screen(
        top=bar.Bar(
            [
				widget.Spacer(length=15,
                    background=colors[0],
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background=colors[0],
                    mouse_callbacks={"Button1":power},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),


                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='block',
                    active=colors[2],
                    block_highlight_text_color="#91B1F0",
                    highlight_color=colors[3],
                    inactive=colors[0],
                    foreground=colors[3],
                    background=colors[1],
                    this_current_screen_border=colors[1],
                    this_screen_border=colors[1],
                    other_current_screen_border=colors[1],
                    other_screen_border=colors[1],
                    urgent_border=colors[1],
                    rounded=True,
                    disable_drag=True,
                 ),


                widget.Spacer(
                    length=8,
                    background=colors[1],
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background=colors[1]
                ),


                widget.CurrentLayout(
                    background=colors[1],
                    foreground=colors[2],
                    fmt='{}',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background=colors[0],
                    mouse_callbacks={"Button1": search},
                ),

                widget.TextBox(
                    fmt='Search',
                    background=colors[0],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground=colors[2],
                    mouse_callbacks={"Button1": search},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),


                widget.WindowName(
                    background = colors[1],
                    format = "{name}",
                    font='JetBrains Mono Bold',
                    foreground=colors[2],
                    empty_group_string = 'Desktop',
                    fontsize=13,

                ),


                # widget.Image(
                #     filename='~/.config/qtile/Assets/3.png',
                # ),


                # widget.Systray(
                #     background=colors[0],
                #     fontsize=2,
                # ),


                # widget.TextBox(
                #     text=' ',
                #     background=colors[0],
                # ),


                # widget.Image(
                #     filename='~/.config/qtile/Assets/6.png',
                #     background=colors[1],
                # ),


                widget.Image(
                filename='~/.config/qtile/Assets/Drop1.png',
                ),

                # widget.Net(
                # format=' {up}   {down} ',
                # background=colors[1],
                # foreground=colors[2],
                # font="JetBrains Mono Bold",
                # prefix='k',
                # ),

                # widget.Image(
                #     filename='~/.config/qtile/Assets/2.png',
                # ),

                # widget.Spacer(
                    # length=8,
                    # background=colors[1],
                # ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background=colors[1],
                ),


                widget.Spacer(
                    length=-7,
                    background=colors[1],
                ),


                widget.Memory(
                    background=colors[1],
                    format='{MemUsed: .0f}{mm}',
                    foreground=colors[2],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),


                # widget.Image(
                # filename='~/.config/qtile/Assets/Drop2.png',
                # ),



                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background=colors[1],
                ),


                # widget.BatteryIcon(
                #     theme_path='~/.config/qtile/Assets/Battery/',
                #     background=colors[1],
                #     scale=1,
                # ),


                # widget.Battery(
                #     font='JetBrains Mono Bold',
                #     background=colors[1],
                #     foreground=colors[2],
                #     format='{percent:2.0%}',
                #     fontsize=13,
                # ),


                # widget.Image(
                #     filename='~/.config/qtile/Assets/2.png',
                # ),


                widget.Spacer(
                    length=8,
                    background=colors[1],
                ),


                # widget.Battery(format=' {percent:2.0%}',
                    # font="JetBrains Mono ExtraBold",
                    # fontsize=12,
                    # padding=10,
                    # background=colors[1],
                # ),

                # widget.Memory(format='﬙{MemUsed: .0f}{mm}',
                    # font="JetBrains Mono Bold",
                    # fontsize=12,
                    # padding=10,
                    # background='#4B4D66',
                # ),

                widget.Volume(
                    font='JetBrainsMonwo monitorso Nerd Font',
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    fontsize=13,
                    background=colors[1],
                ),


                widget.Spacer(
                    length=-5,
                    background=colors[1],
                    ),


                widget.Volume(
                    font='JetBrains Mono Bold',
                    background=colors[1],
                    foreground=colors[2],
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background=colors[1],
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background=colors[0],
                    margin_y=6,
                    margin_x=5,
                ),


                widget.Clock(
                    format='%d.%m.%Y %a %H:%M',
                    background=colors[0],
                    foreground=colors[2],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),


                widget.Spacer(
                    length=18,
                    background=colors[0],
                ),



            ],
            30,
            border_color = colors[0],
            border_width = [0,0,0,0],
            margin = [5,5,5,5],

        ),
    )
]
