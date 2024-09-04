from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # Lock the system
    ([mod], "l", lazy.spawn("/home/codintdev/i3lock-fancy/i3lock-fancy -f Hack-Nerd-Font-Regular -t FBI")),

    # ------------ App Configs ------------

    # Menu apps
    ([mod], "d", lazy.spawn("rofi -show drun")),

    # Window Navigator
    ([mod, "shift"], "d", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "f", lazy.spawn("brave-browser")),
    ([mod, "shift"], "f", lazy.spawn("firefox")),

    # File Explorer
    ([mod], "e", lazy.spawn("nautilus")),

    # Terminal
    ([mod], "Return", lazy.spawn("kitty")),
    ([mod, "shift"], "Return", lazy.spawn("alacritty")),

    # Screenshot
    ([mod], "s", lazy.spawn("flameshot gui")),

    # Obsidian
    ([mod], "o", lazy.spawn("obsidian")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
