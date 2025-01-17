from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep

mod = "mod4"
terminal = "kitty"
file_manager = "nemo"

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█


from keybind import keybinds

keys = keybinds()



# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█



groups = [Group("1", label="●",matches=[Match(wm_class="firefox")]),
          Group("2", label="●",matches=[Match(wm_class="code")]),
          Group("3", label="●"),
          Group("4", label="●",matches=[Match(wm_class="steam"),Match(wm_class="heroic"),Match(wm_class="lutris")]),
          Group("5", label="●",matches=[Match(wm_class="discord")]),
          Group("6", label="●",matches=[Match(wm_class="gimp")]),
          Group("7", label="●",matches=[Match(wm_class="qbittorrent")]),
          Group("8", label="●"),
          Group("9", label="●"),
          Group("0", label="●"),]

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
                    lazy.window.togroup(i.name, switch_group=False),
                    desc="Move focused window to group {}".format(i.name),
                    ),
                ]
            )

# SCRATCHPADS

from libqtile.config import Group, ScratchPad, DropDown, Key
import re
groups.append(ScratchPad("scratchpad", [
    DropDown("spotify", "flatpak run com.spotify.Client",match=Match(wm_class=re.compile(r"^(Spotify)$")), width = 0.8, height = 0.8, x = 0.1, y = 0.1, opacity = 1),  
    DropDown("file_manager", f"{terminal} yazi", width = 0.8, height = 0.8, x = 0.1, y = 0.1, opacity = 1),  
    DropDown("bpytop", f"{terminal} -e bpytop", width = 0.8, height = 0.8, x = 0.1, y = 0.1, opacity = 1),  
    DropDown("terminal", f"{terminal}", width = 0.8, height = 0.8, x = 0.1, y = 0.1, opacity = 1),  
    # DropDown("calendar", f"{terminal} cal -m -3", width = 0.2, height = 0.2, x = 0.8, y = 0.1, opacity = 1),  
    
]))


keys.extend([
    Key([],"F4",lazy.group['scratchpad'].dropdown_toggle('spotify')),
    # Key([mod],"e",lazy.group['scratchpad'].dropdown_toggle('file_manager')),
    Key([mod],"b",lazy.group['scratchpad'].dropdown_toggle('bpytop')),
    Key([mod],"t",lazy.group['scratchpad'].dropdown_toggle('terminal')),
    # Key([mod],"l",lazy.group['scratchpad'].dropdown_toggle('calendar')),
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
        margin= 2, 
        border_focus=color_focused,
	    border_normal=color_normal,
        border_width=5,
        initial_ratio=1.6
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
follow_mouse_focus = False
bring_front_click = True
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
    home = os.path.expanduser('~/.config/qtile/autostart_once.sh')
    subprocess.call([home])
auto_fullscreen = True
focus_on_window_activation = "never"
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
