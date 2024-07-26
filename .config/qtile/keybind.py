from libqtile.config import Key
from libqtile.lazy import lazy

# from libqtile.utils import guess_terminal
# from libqtile.dgroups import simple_key_binder
# from time import sleep

mod = "mod4"
terminal = "kitty"


def keybinds():
    return [
        #  D E F A U L T
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key(
            [mod], "space", lazy.layout.next(), desc="Move window focus to other window"
        ),
        Key(
            [mod, "control"],
            "h",
            lazy.layout.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            [mod, "control"],
            "l",
            lazy.layout.shuffle_right(),
            desc="Move window to the right",
        ),
        Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        Key(
            [mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"
        ),
        Key(
            [mod, "shift"],
            "l",
            lazy.layout.grow_right(),
            desc="Grow window to the right",
        ),
        Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
        Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
        Key(
            [mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key(
            [mod],
            "d",
            lazy.spawn("rofi -show drun"),
            desc="Spawn a command using a prompt widget",
        ),
        Key(
            [mod],
            "p",
            lazy.spawn("sh -c ~/.config/rofi/scripts/power"),
            desc="powermenu",
        ),
        Key(
            [mod],
            "F1",
            lazy.spawn("sh -c ~/.config/picom/picom_togle.sh"),
            desc="toggle picom",
        ),
        # Key([mod], "t", lazy.spawn("sh -c ~/.config/rofi/scripts/themes"), desc='theme_switcher'),
        # C U S T O M
        Key([], "F11", lazy.spawn("amixer sset Master 5%+"), desc="Volume Up"),
        Key([], "F10", lazy.spawn("amixer sset Master 5%-"), desc="volme down"),
        Key([], "F9", lazy.spawn("pulsemixer --toggle-mute"), desc="Volume Mute"),
        # Key([], "F7", lazy.spawn("playerctl play-pause"), desc='playerctl'),
        # Key([], "F5", lazy.spawn("playerctl previous"), desc='playerctl'),
        # Key([], "F6", lazy.spawn("playerctl next"), desc='playerctl'),
        Key(
            [],
            "XF86MonBrightnessUp",
            lazy.spawn("brightnessctl s 10%+"),
            desc="brightness UP",
        ),
        Key(
            [],
            "XF86MonBrightnessDown",
            lazy.spawn("brightnessctl s 10%-"),
            desc="brightness Down",
        ),
        # Key([mod],"e", lazy.spawn("nemo"), desc='file manager'),
        Key(
            [mod, "shift"],
            "v",
            lazy.spawn(
                'rofi -modi "clipboard:greenclip print" -show clipboard -run-command "{cmd}"'
            ),
            desc="greenclip",
        ),
        Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Screenshot"),
        Key([mod], "Escape", lazy.spawn("i3lock -e -c 000000"), desc="Screenshot"),
    ]
