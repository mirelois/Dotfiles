# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage

import os
import socket
from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
import subprocess
import shlex
import fontawesome as fa
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration


mod = "mod4"
terminal = 'gnome-terminal'
browser = 'firefox'


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn('bin/launcher.sh'),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout."),
    Key([mod], "b", lazy.spawn(browser)),
    Key([mod], "d", lazy.spawn('discord')),
    Key([mod], "g", lazy.spawn('github')),
    Key([mod], "y", lazy.spawn(browser+' https://www.youtube.com/')),
    Key([mod], "t", lazy.spawn(browser+' https://www.twitch.tv/')),
    Key([mod], "p", lazy.spawn(
        "bin/eww open-many weather_side time_side smol_calendar player_side sys_side sliders_side")),
    Key([mod], "c", lazy.spawn(
        "bin/eww open-many weather profile quote search_full disturb-icon vpn-icon home_dir screenshot power_full reboot_full lock_full logout_full suspend_full")),
    Key([mod], "Escape", lazy.spawn("bin/eww close-all")),

    # Treetab controls
    Key([mod, "shift"], "h",
        lazy.layout.move_left(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "shift"], "l",
        lazy.layout.move_right(),
        desc='Move down a section in treetab'),
    # window controls
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'),
    Key([mod], "F5", lazy.spawn("brightnessctl set +1%")),
    Key([mod], "F4", lazy.spawn("brightnessctl set 1%-")),

    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    Key(["control"], "F1", lazy.spawn(
        "pactl set-source-mute @DEFAULT_SOURCE@ toggle")),
    Key(["control"], "F3", lazy.spawn(
        "pactl set-source-volume @DEFAULT_SOURCE@ +10%")),
    Key(["control"], "F2", lazy.spawn(
        "pactl set-source-volume @DEFAULT_SOURCE@ -10%")),
    Key([], "Print", lazy.spawn("gnome-screenshot -wi")),
    Key([mod], "s", lazy.hide_show_bar("bottom")),
]

group_names = ['', '', '',
               '', '', '',
               '7', '8', '9']

groups = [Group(group_names[0]),
          Group(group_names[1], spawn=terminal),
          Group(group_names[2]),
          Group(group_names[3]),
          Group(group_names[4], spawn="discord"),
          Group(group_names[5]),
          Group(group_names[6]),
          Group(group_names[7]),
          Group(group_names[8])]

for indx, name in enumerate(group_names, start=1):
    i = str(indx)
    keys += [
        Key([mod], i, lazy.group[name].toscreen()),
        Key([mod, 'shift'], i, lazy.window.togroup(name))
    ]

    colors = [["#121212", "#121212"],  # ["#282c34", "#282c34"],
              ["#1c1f24", "#1c1f24"],
              ["#dfdfdf", "#dfdfdf"],
              ["#ff6c6b", "#ff6c6b"],
              ["#98be65", "#98be65"],
              ["#da8548", "#da8548"],
              ["#51afef", "#51afef"],
              ["#c678dd", "#c678dd"],
              ["#46d9ff", "#46d9ff"],
              ["#a9a1e1", "#a9a1e1"]]

layout_theme = {"border_width": 2,
                "margin": 20,
                "border_focus": "e1acff",
                "border_normal": "1D2330",
                "margin_on_single": 1,
                }

layouts = [
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.RatioTile(**layout_theme),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=10,
        sections=["1", "2", "3", "4"],
        section_fontsize=10,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=100
    ),
    layout.Floating(**layout_theme)
]


prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


widget_defaults = dict(
    font="Ubuntu",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        # wallpaper='~/.config/qtile/background/dracula-mnt-bd93f9.png',
        # wallpaper_mode='fill',
        top=bar.Gap(25),
        bottom=bar.Bar(
            [
                widget.Sep(
                    linewidth=1718,
                    background="#00000000",
                    foreground="#00000000",
                ),
                widget.CapsNumLockIndicator(
                    font="Ubunto",
                    padding=5,
                ),
                widget.KeyboardLayout(
                    foreground="ffffff",
                    background="#00000000",
                    display_map={
                        'pt nodeadkeys': fa.icons['keyboard'] + '1', 'pt': fa.icons['keyboard'] + '0'
                    },
                    configured_keyboards=['pt nodeadkeys', 'pt'],
                    padding=5,
                    fontsize=18,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser(
                        "~/.config/qtile/icons")],
                    foreground=colors[9],
                    background="#00000000",
                    padding=5,
                    scale=1
                ),
            ],
            24,
            background="#00000000",
            margin=[0, 0, 5, 0],
        ),
        # top=bar.Bar(
        #    [
        #        widget.Sep(
        #            linewidth=0,
        #            padding=6,
        #            foreground=colors[2],
        #            background=colors[0]
        #        ),
        #        widget.Sep(
        #            linewidth=0,
        #            padding=6,
        #            foreground=colors[2],
        #            background=colors[0]
        #        ),
        #        widget.GroupBox(
        #            font="Ubuntu",
        #            fontsize=16,
        #            margin_y=3,
        #            margin_x=3,
        #            padding_y=5,
        #            padding_x=3,
        #            borderwidth=3,
        #            active=colors[2],
        #            inactive=colors[9],
        #            rounded=False,
        #            highlight_color=colors[1],
        #            highlight_method="line",
        #            this_current_screen_border=colors[6],
        #            this_screen_border=colors[4],
        #            other_current_screen_border=colors[6],
        #            other_screen_border=colors[4],
        #            foreground=colors[2],
        #            background=colors[0]
        #        ),
        #        widget.TextBox(
        #            text='|',
        #            font="Ubuntu Mono",
        #            background=colors[0],
        #            foreground='474747',
        #            padding=2,
        #            fontsize=14
        #        ),
        #        widget.CurrentLayoutIcon(
        #            custom_icon_paths=[os.path.expanduser(
        #                "~/.config/qtile/icons")],
        #            foreground=colors[2],
        #            background=colors[0],
        #            padding=0,
        #            scale=0.7
        #        ),
        #        widget.CurrentLayout(
        #            foreground=colors[2],
        #            background=colors[0],
        #            padding=5
        #        ),
        #        widget.TextBox(
        #            text='|',
        #            font="Ubuntu Mono",
        #            background=colors[0],
        #            foreground='474747',
        #            padding=2,
        #            fontsize=14
        #        ),
        #        widget.Prompt(
        #            foreground=colors[2],
        #            background=colors[0]
        #        ),
        #        widget.WindowName(
        #            foreground=colors[6],
        #            background=colors[0],
        #            padding=0
        #        ),
        #        widget.Systray(
        #            background=colors[0],
        #            padding=5
        #        ),
        #        widget.Sep(
        #            linewidth=0,
        #            padding=6,
        #            foreground=colors[0],
        #            background=colors[0]
        #        ),
        #        widget.Net(
        #            interface='wlo1',
        #            format=' {down} ↓↑ {up}',
        #            foreground=colors[3],
        #            background=colors[0],
        #            padding=5,
        #            decorations=[
        #                   BorderDecoration(
        #                       colour=colors[3],
        #                       border_width=[0, 0, 2, 0],
        #                       padding_x=5,
        #                       padding_y=None,
        #                   )
        #            ],


        #        ),
        #        widget.Sep(
        #            linewidth=0,
        #            padding=6,
        #            foreground=colors[0],
        #            background=colors[0]
        #        ),
        #        widget.CPU(
        #            background=colors[0],
        #            foreground=colors[5],
        #            format="CPU:{load_percent}%",
        #            mouse_callbacks={
        #                'Button1': lambda: qtile.cmd_spawn("gnome-system-monitor")
        #            },
        #            decorations=[
        #                BorderDecoration(
        #                    colour=colors[5],
        #                    border_width=[0, 0, 2, 0],
        #                    padding_x=5,
        #                    padding_y=None,
        #                )
        #            ],

        #        ),
        #        widget.Sep(
        #            linewidth=0,
        #            padding=6,
        #            foreground=colors[0],
        #            background=colors[0]
        #        ),
        #        widget.KeyboardLayout(
        #            foreground=colors[8],
        #            background=colors[0],
        #            configured_keyboards=['pt nodeadkeys', 'pt'],
        #            fmt=fa.icons['keyboard'] + ' {}',
        #            padding=5,
        #            decorations=[
        #                BorderDecoration(
        #                    colour=colors[8],
        #                    border_width=[0, 0, 2, 0],
        #                    padding_x=5,
        #                    padding_y=None,
        #                )
        #            ],

        #        ),
        #        widget.Sep(
        #            linewidth=0,
        #            padding=6,
        #            foreground=colors[0],
        #            background=colors[0]
        #        ),
        #        widget.Memory(
        #            foreground=colors[9],
        #            background=colors[0],
        #            mouse_callbacks={
        #                'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
        #            fmt=' {}',
        #            padding=5,
        #            decorations=[
        #                BorderDecoration(
        #                    colour=colors[9],
        #                    border_width=[0, 0, 2, 0],
        #                    padding_x=5,
        #                    padding_y=None,
        #                )
        #            ],

        #        ),
        #        widget.Sep(
        #            linewidth=0,
        #            padding=6,
        #            foreground=colors[0],
        #            background=colors[0]
        #        ),
        #        widget.Volume(
        #            foreground=colors[7],
        #            background=colors[0],
        #            fmt='Vol:{}',
        #            padding=2,
        #            volume_app="pactl",
        #            mute_command="pactl set-sink-mute @DEFAULT_SINK@ toggle",
        #            volume_up_command="pactl set-sink-volume @DEFAULT_SINK@ +10%",
        #            volume_down_command="pactl set-sink-volume @DEFAULT_SINK@ -10%",
        #            get_volume_command="./.config/qtile/scripts/get_volume.sh",
        #            decorations=[
        #                BorderDecoration(
        #                       colour=colors[7],
        #                       border_width=[0, 0, 2, 0],
        #                       padding_x=5,
        #                       padding_y=None,
        #                )
        #            ],


        #        ),
        #        widget.Volume(
        #            foreground=colors[7],
        #            background=colors[0],
        #            fmt='Mic:{}',
        #            padding=2,
        #            volume_app="pactl",
        #            get_volume_command="./.config/qtile/scripts/get_mic.sh",
        #            decorations=[
        #                BorderDecoration(
        #                       colour=colors[7],
        #                       border_width=[0, 0, 2, 0],
        #                       padding_x=5,
        #                       padding_y=None,
        #                )
        #            ],


        #        ),
        #        widget.Sep(
        #            linewidth=0,
        #            padding=6,
        #            foreground=colors[0],
        #            background=colors[0]
        #        ),
        #        widget.UPowerWidget(
        #            background=colors[0],
        #            foreground='8C9720',
        #            border_colour='8C9720',
        #            border_charge_colour='8C9720',
        #            fill_normal='8C9720',
        #            fill_low='8C9720',
        #            decorations=[
        #                BorderDecoration(
        #                        colour='8C9720',
        #                        border_width=[0, 0, 2, 0],
        #                        padding_x=2,
        #                        padding_y=None,
        #                )
        #            ],


        #        ),
        #        widget.Sep(
        #            linewidth=0,
        #            padding=6,
        #            foreground=colors[0],
        #            background=colors[0]
        #        ),

        #        widget.Clock(
        #            foreground=colors[6],
        #            background=colors[0],
        #            format="%A, %B %d - %H:%M ",
        #            mouse_callbacks={
        #                'Button1': lambda: qtile.cmd_spawn("gnome-calendar")},
        #            decorations=[
        #                BorderDecoration(
        #                    colour=colors[6],
        #                    border_width=[0, 0, 2, 0],
        #                    padding_x=5,
        #                    padding_y=None,
        #                )
        #            ],

        #        ),
        #        widget.AnalogueClock(
        #            background=colors[0],
        #            face_shape="square",
        #            face_background=colors[6],
        #            face_border_colour=colors[6],
        #            face_border_width=4,
        #            padding=5
        #        ),
        #        widget.Sep(
        #            linewidth=0,
        #            padding=6,
        #            foreground=colors[0],
        #            background=colors[0]
        #        ),
        #    ],
        #    24,
        #    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        #    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        # ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
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


@ hook.subscribe.startup
def startup():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/startup.sh'])
    lazy.cmd_hide_show_bar("all")
    Screen.bottom.show(False)
