#############################
from libqtile import widget #
from .theme import colors   #
#############################

# Función para verificar la IP
def get_ip():
    import subprocess
    try:
        ip = subprocess.check_output("hostname -I | awk '{print $1}'", shell=True).decode("utf-8").strip()
        return ip
    except Exception:
        return "No IP"

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=14, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",
        fontsize=37,
        padding=-2
    )

def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=17,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=10, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(bg="color4", text='󰩠 '),
    # IP
    widget.GenPollText(func=get_ip, update_interval=10, fontsize=14, foreground="#ffffff", background=colors['color4']),
    
    # Widget de las actualizaciones
    # widget.CheckUpdates(
    #     background=colors['color4'],
    #     colour_have_updates=colors['text'],
    #     colour_no_updates=colors['text'],
    #     no_update_string='0',
    #     display_format='{updates}',
    #     update_interval=1800,
    #     custom_command='checkupdates',
    # ),

    powerline('color3', 'color4'),

    icon(bg="color3", text='󱛆 '),
    
    widget.Net(**base(bg='color3'), interface='wlan0'),

    powerline('color2', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=15, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),

]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font',
    'fontsize': 12,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
