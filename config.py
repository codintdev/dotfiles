from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ---------- Windows Config ----------
    ([mod], "k", lazy.layout.up()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),

    ([mod, "control"], "k", lazy.layout.grow_up()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),

    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    ([mod], "w", lazy.window.kill()),

    ([mod, "control"], "r", lazy.reload_config()),
    
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ---------- Apps Config ----------
    ([mod], "b", lazy.spawn("firefox &> /dev/null &")),

    ([mod], "c", lazy.spawn("code")),

    ([mod], "Return", lazy.spawn("kitty")),

    ([mod], "m", lazy.spawn("rofi -show drun")),

    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    ([mod], "e", lazy.spawn("thunar")),

    # -------- Hardware Config ----------
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]

groups = [Group(i) for i in [
    "  ", "  ", " 󰨞 ", "  ", "  ", "  ", "  ", "  ", "  "
]]

for i,group in enumerate(groups):
    actual_key=str(i+1)
    keys.extend([
            # Switch to workspace N
            Key([mod], actual_key, lazy.group[group.name].toscreen()),
            # Send window to workspace N
            Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
        ])

# ---------- Items ----------
tamano_barra_principal=20
tamano_fuente=9
tamano_iconos=12
color_barra="#181818"
color_activo="#ffffff"
color_inactivo="#3C4048"
color_border="#E84545"
color_ip="#93BFCF"
color_wlan="#F8F988"
color_layout="#472183"
color_battery="#F99417"
color_fecha="#E14541"
color_other_screen="#181818"
color_tercery_screen="#181818"
fuente_predeterminada="JetBrainsMono Nerd Font"

def init_layout_conf_theme():
    return {
    'border_focus': color_border,
    'border_normal': color_barra,
    'border_width': 1,
    'margin': 5
    }
layout_conf = init_layout_conf_theme()

layouts = [
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Max(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=fuente_predeterminada,
    fontsize=tamano_fuente,
    padding=2,
)
extension_defaults = widget_defaults.copy()

def separador():
    return widget.Sep(
        linewidth=0,
        padding=5
    )

def powerline(fg, bg):
    return widget.TextBox(
        text="",
        fontsize=60,
        padding=-4,
        foreground=fg,
        background=bg
    )

def icon(text, fg, bg, fontsize=12):
    return widget.TextBox(
        text=text,
        fontsize=fontsize,
        foreground=fg,
        background=bg
    )

# ---------- Screen Primary ----------
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=color_activo,
                    inactive=color_inactivo,
                    font=fuente_predeterminada,
                    fontsize=tamano_iconos,
                    margin_y=3,
                    margin_x=1,
                    padding_y=1,
                    padding_x=2,
                    borderwidth=2,
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    active_highlight_color='active',
                    #urgent_border=color_border,
                    this_current_screen_border=color_border,
                    this_screen_border=color_border,
                    other_current_screen_border=color_other_screen,
                    other_screen_border=color_tercery_screen,
                    disable_drag=True
                ),
                separador(),
                widget.Prompt(),
                widget.WindowName(foreground=color_border, fontsize=10, padding=5),
                powerline(color_wlan, color_barra),
                icon("  ", color_barra, color_wlan),
                widget.Net(background=color_wlan, foreground=color_barra),
                powerline(color_layout, color_wlan),
                widget.CurrentLayoutIcon(background=color_layout, scale=0.65),
                widget.CurrentLayout(foreground="#FFFFFF", background=color_layout, padding=5),
                powerline(color_battery, color_layout),
                icon("   ", color_barra, color_battery),
                widget.Battery(background=color_battery, foreground=color_barra),
                powerline(color_fecha, color_battery),
                icon("  ", color_barra, color_fecha),
                widget.Clock(foreground=color_barra, background=color_fecha,format="%Y-%m-%d %a %I:%M %p"),
                powerline(color_barra, color_fecha),
                widget.Systray(background=color_barra, padding=5),
            ],
            tamano_barra_principal,
            background=color_barra,
        ),
    ),
]

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

autostart = [
    "picom --no-vsync &",
    "nm-applet &",
    "feh --bg-fill /home/andres-felipe/Desktop/andres-felipe/wallpapers/demon_anime.jpg",
]

for x in autostart:
    os.system(x)
