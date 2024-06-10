    
#       █████████     ███████    ███████████ █████ █████ ███████████ █████ █████       ██████████
#      ███░░░░░███  ███░░░░░███ ░█░░░░░░███ ░░███ ░░███ ░█░░░███░░░█░░███ ░░███       ░░███░░░░░█
#     ███     ░░░  ███     ░░███░     ███░   ░░███ ███  ░   ░███  ░  ░███  ░███        ░███  █ ░ 
#    ░███         ░███      ░███     ███      ░░█████       ░███     ░███  ░███        ░██████   
#    ░███         ░███      ░███    ███        ░░███        ░███     ░███  ░███        ░███░░█   
#    ░░███     ███░░███     ███   ████     █    ░███        ░███     ░███  ░███      █ ░███ ░   █
#     ░░█████████  ░░░███████░   ███████████    █████       █████    █████ ███████████ ██████████
#      ░░░░░░░░░     ░░░░░░░    ░░░░░░░░░░░    ░░░░░       ░░░░░    ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░ 
#
#                                                                                    - DARKKAL44
  


from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep

mod = "mod4"
terminal = "kitty"

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█


from keybind import keybinds

keys = keybinds()



# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█



groups = [Group(f"{i+1}", label="●") for i in range(8)]

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )

# SCRATCHPADS

from libqtile.config import Group, ScratchPad, DropDown, Key
import re
groups.append(ScratchPad("scratchpad", [
    DropDown("spotify", "flatpak run com.spotify.Client", width = 0.8, height = 0.8, x = 0.1, y = 0.1, opacity = 1)
    # DropDown("spotify","flatpak run com.spotify.Spotify", match=Match(wm_class=['Spotify']) opacity=1, height=0.8, width=0.8,x=0.1,y=0.1)
]))
#Match(wm_class=re.compile(r"^(Spotify)$")),


keys.extend([
    Key([mod],"s",lazy.group['scratchpad'].dropdown_toggle('spotify'))
])


# L A Y O U T S
color_focused = '#eb434d'
color_normal = '#133247'
layouts = [
    # layout.Tile(	             
    #     border_focus=color_focused,
	#     border_normal=color_normal,
    #     margin=10,
	#     border_width=5,
    # ),
    layout.Columns( 
        margin= 10, 
        border_focus=color_focused,
	    border_normal=color_normal,
        border_width=5,
    ),

    # layout.Max(	    
    #     border_focus=color_focused,
	#     border_normal=color_normal,
	#     margin=10,
	#     border_width=5,
    # ),

    layout.Floating(	
        border_focus=color_focused,
	    border_normal=color_normal,
	    margin=10,
	    border_width=5,
	),
    # Try more layouts by unleashing below layouts
   #  layout.Stack(num_stacks=2),
   #  layout.Bsp(),
     layout.Matrix(	
        border_focus=color_focused,
	    border_normal=color_normal,
	    margin=10,
	    border_width=5,
	),
     layout.MonadTall(	
        border_focus=color_focused,
	    border_normal=color_normal,
        margin=10,
	    border_width=5,
	),
    layout.MonadWide(	
        border_focus=color_focused,
	    border_normal=color_normal,
        margin=10,
	    border_width=5,
	),
   #  layout.RatioTile(),
     
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄


from bar import spawn_bar
screens = spawn_bar()


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
	border_focus=color_focused,
	border_normal=color_normal,
	border_width=5,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)




from libqtile import hook
# some other imports
import os
import subprocess
# stuff
@hook.subscribe.startup_once
def autostart_once():
    # subprocess.run('~/.config/qtile/autostart_once.sh')# path to my script, under my user directory
    # subprocess.call([home])
    home = os.path.expanduser('~/.config/qtile/autostart_once.sh')
    subprocess.call([home])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



# E O F
