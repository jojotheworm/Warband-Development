###################################################
# header_triggers.py
# This file contains declarations for triggers
# DO NOT EDIT THIS FILE!
###################################################

# SIMPLE TRIGGERS (used in module_simple_triggers)

#ti_on_game_start              =  -2.0
ti_simulate_battle            =  -5.0 # DEPRECATED
ti_on_party_encounter         =  -6.0 # DEPRECATED


# GENERIC TRIGGERS (used in module_items)

ti_question_answered          =  -8.0 # Player selected an option in (question_box, ...) dialog. Commonly used in module_mission_templates, but should be usable on the global map as well.
    # trigger param #1 = player's selected response: 0 = first button (usually "Yes"), 1 = second button (usually "No").

ti_on_switch_to_map           = -75.0 # Patch 1.165+. UNTESTED.


# ITEM TRIGGERS (used in module_items.py)

ti_on_init_item               = -50.0 # Item mesh has been created.
    # trigger param #1 = agent_id who has this item equipped (-1 if none)
    # trigger param #2 = troop_id who has this item equipped (-1 if none)

ti_on_weapon_attack           = -51.0 # Agent has performed an attack with this item.
    # trigger param #1 = attacking agent_id
    # pos1             = weapon item position

ti_on_missile_hit             = -52.0 # Missile has hit something.
    # trigger param #1 = shooter agent_id
    # trigger param #2 = hit object type:
        # 0 = world (landscape)
        # 1 = hostile agent
        # 2 = dynamic prop
        # 3 = world object (trees, stones, scene interior basic mesh)
        # 4 = mission object (most scene props)
        # 8 = friendly agent
        # 9 = neutral agent
        # 10 = under water
    # pos1             = Missile Position

ti_on_shield_hit              = -80.0 #
    # trigger param 1 = defender agent_id
    # trigger param 2 = attacker agent_id
    # trigger param 3 = inflicted damage
    # trigger param 4 = weapon item_id (ranged weapon in case of ranged attack)
    # trigger param 5 = missile item_id (ammo in case of ranged attack)
    # If (set_trigger_result) is used in the code, operation parameter will override the damage dealt to the shield


# MAP ICON TRIGGERS (used in module_map_icons.py)

ti_on_init_map_icon           = -70.0 # Map icon mesh has been created.
    # trigger param 1 = party_id that is using this icon


# MISSION TEMPLATE TRIGGERS (used in module_mission_templates)

ti_server_player_joined       = -15.0 # Multiplayer server-side trigger. New player has connected to the server.
    # trigger param 1 = player_id of joined player

ti_on_player_exit             = -29.0 # Multiplayer server-side trigger. A player is leaving the multiplayer mission.
    # trigger param 1 = leaving player_id

ti_on_multiplayer_mission_end = -16.0 # Multiplayer client-side trigger. Multiplayer mission has completed.

ti_battle_window_opened       = -24.0 # Multiplayer client-side trigger. UNDOCUMENTED.

ti_before_mission_start       = -19.0 # Scene has been loaded, but mission hasn't started yet. Called before initialization of all scene objects.

ti_after_mission_start        = -20.0 # Scene has been loaded and all objects have been initialized.

ti_tab_pressed                = -21.0 # Player has clicked `Leave location/Retreat` game key ('Tab' by default).

ti_inventory_key_pressed      = -22.0 # Player has clicked `Inventory` game key ('I' by default).

ti_escape_pressed             = -23.0 # Player has clicked 'Escape' button.

ti_on_agent_spawn             = -25.0 # A new agent has been spawned on the scene.
    # trigger param 1 = agent_id of spawned agent

ti_on_agent_killed_or_wounded = -26.0 # Agent has been defeated in battle (killed or wounded)
    # trigger param 1 = defeated agent_id
    # trigger param 2 = attacker agent_id
    # trigger param 3 = wounded flag: 0 = agent is killed, 1 = agent is wounded

ti_on_agent_knocked_down      = -27.0 # Agent has been knocked down, used in combination with (agent_set_no_death_knock_down_only) operation.
    # trigger param 1 = defeated agent_id
    # trigger param 2 = attacker agent_id

ti_on_agent_hit               = -28.0 # Agent has been damaged with a weapon attack
    # trigger param 1 = damage inflicted agent_id
    # trigger param 2 = attacker agent_id
    # trigger param 3 = inflicted damage
    # reg0            = weapon item_id
    # pos0            = position of the hit area, rotation fields contain the direction of the blow
    # If (set_trigger_result) is used in the code with operation parameter equal or greater than zero, it will override the inflicted damage.

ti_on_leave_area              = -30.0 # Player has walked to scene border and activated it to leave the area.

ti_on_item_picked_up          = -53.0 # An agent has picked an item from the ground
    # trigger param 1 = agent_id who picked the item
    # trigger param 2 = item_id that was picked up
    # trigger param 3 = item's instance_id at the moment of being picked up, can be used to retrieve item's position on the scene. Will be deleted after trigger fires.

ti_on_item_dropped            = -54.0 # An agent has dropped an item on the ground
    # trigger param 1 = agent_id
    # trigger param 2 = item_id
    # trigger param 3 = item's instance_id

ti_on_agent_mount             = -55.0 # An agent has mounted a horse
    # trigger param 1 = agent_id
    # trigger param 2 = horse agent_id

ti_on_agent_dismount          = -56.0 # An agent has dismounted a horse
    # trigger param 1 = agent_id
    # trigger param 2 = horse agent_id

ti_on_item_wielded            = -57.0 # An agent has selected a weapon to wield
    # trigger param 1 = agent_id
    # trigger param 2 = item_id

ti_on_item_unwielded          = -58.0 # An agent has sheathed his current weapon or switched to another one
    # trigger param 1 = agent_id
    # trigger param 2 = item_id

ti_on_order_issued            = -71.0 # An agent has issued a tactical order
    # trigger param 1 = order_code (see mordr_* constants in header_mission_templates.py)
    # trigger param 2 = agent_id


# PRESENTATION TRIGGERS (used in module_presentations)

ti_on_presentation_load               = -60.0 # Presentation has been loaded by the engine. Use this trigger to initialize the presentation and it's overlays.

ti_on_presentation_run                = -61.0 # This trigger is activated every frame while the presentation is running. Use it to handle real-time behavior within the presentation.
    # trigger param 1 = how much time has passed since presentation has been started (in milliseconds)

ti_on_presentation_event_state_change = -62.0 # Some overlay has changed it's state (button clicked, checkbox switched state, slider moved, list has it's active element changed etc).
    # trigger param 1 = overlay_id of the object that initiated the event
    # trigger param 2 = new overlay value (if appropriate)

ti_on_presentation_mouse_enter_leave  = -63.0 # Reports that mouse cursor has entered or left an overlay.
    # trigger param 1 = overlay_id of the object that mouse enters/leaves
    # trigger param 2 = 0 if mouse enters, 1 if mouse leaves

ti_on_presentation_mouse_press        = -64.0 # A mouse click has been detected on one of presentation overlays.
    # trigger param 1 = overlay_id of the object that mouse is pressed on
    # trigger param 2 = 0: left mouse button, 1 right mouse button, 2 middle mouse button


# SCENE PROP TRIGGERS (used in module_scene_props)

ti_on_scene_prop_init               = -40.0 # A scene prop instance has been created on the scene.
ti_on_init_scene_prop               = ti_on_scene_prop_init # Alternate syntax
    # trigger param 1 = prop instance_id reference

ti_on_scene_prop_hit                = -42.0 # A scene prop has been hit by some agent.
    # trigger param 1 = prop instance_id reference
    # trigger param 2 = amount of damage delivered to the scene prop
    # pos1            = position of the hit area
    # pos2            = X field holds attacker's agent_id reference

ti_on_scene_prop_destroy            = -43.0 # A destructible scene prop has been destroyed by some agent.
    # trigger param 1 = prop instance_id reference
    # trigger param 2 = attacker agent_id

ti_on_scene_prop_start_use          = -47.0 # An agent is attempting to activate a usable scene prop. Useful if you want a scene prop to be activated instantly without any timeout.
    # trigger param 1 = agent_id of the agent who has started using the scene prop
    # trigger param 2 = prop instance_id reference

ti_on_scene_prop_cancel_use         = -48.0 # An agent has cancelled using the scene prop.
    # trigger param 1 = agent_id of the agent who cancelled using the scene prop
    # trigger param 2 = prop instance_id reference

ti_on_scene_prop_use                = -44.0 # A usable scene prop has been activated by some agent.
    # trigger param 1 = agent_id of the agent who activated the scene prop
    # trigger param 2 = prop instance_id reference

ti_on_scene_prop_is_animating       = -45.0 # Called each frame when a scene prop is animating.
    # trigger param 1 = prop instance_id reference
    # trigger param 2 = remaining animation time (apparently in 1/100th of second).

ti_on_scene_prop_animation_finished = -46.0 # Animation sequence has been completed for a scene prop.
    # trigger param 1 = prop instance_id reference

ti_scene_prop_deformation_finished  = -76.0 # Deformation sequence has been completed for a scene prop.
    # trigger param 1 = prop instance_id reference



ti_once        = 100000000.0

# Keys that can be checked by key_is_down and key_clicked

key_1 = 0x02
key_2 = 0x03
key_3 = 0x04
key_4 = 0x05
key_5 = 0x06
key_6 = 0x07
key_7 = 0x08
key_8 = 0x09
key_9 = 0x0a
key_0 = 0x0b
key_a = 0x1e
key_b = 0x30
key_c = 0x2e
key_d = 0x20
key_e = 0x12
key_f = 0x21
key_g = 0x22
key_h = 0x23
key_i = 0x17
key_j = 0x24
key_k = 0x25
key_l = 0x26
key_m = 0x32
key_n = 0x31
key_o = 0x18
key_p = 0x19
key_q = 0x10
key_r = 0x13
key_s = 0x1f
key_t = 0x14
key_u = 0x16
key_v = 0x2f
key_w = 0x11
key_x = 0x2d
key_y = 0x15
key_z = 0x2c
key_numpad_0 = 0x52
key_numpad_1 = 0x4f
key_numpad_2 = 0x50
key_numpad_3 = 0x51
key_numpad_4 = 0x4b
key_numpad_5 = 0x4c
key_numpad_6 = 0x4d
key_numpad_7 = 0x47
key_numpad_8 = 0x48
key_numpad_9 = 0x49
key_num_lock        = 0x45
key_numpad_slash    = 0xb5
key_numpad_multiply = 0x37
key_numpad_minus    = 0x4a
key_numpad_plus     = 0x4e
key_numpad_enter    = 0x9c
key_numpad_period   = 0x53
key_insert    = 0xd2
key_delete    = 0xd3
key_home      = 0xc7
key_end       = 0xcf
key_page_up   = 0xc9
key_page_down = 0xd1
key_up      = 0xc8
key_down    = 0xd0
key_left    = 0xcb
key_right   = 0xcd
key_f1  = 0x3b
key_f2  = 0x3c
key_f3  = 0x3d
key_f4  = 0x3e
key_f5  = 0x3f
key_f6  = 0x40
key_f7  = 0x41
key_f8  = 0x42
key_f9  = 0x43
key_f10 = 0x44
key_f11 = 0x57
key_f12 = 0x58
key_space         = 0x39
key_escape        = 0x01
key_enter         = 0x1c
key_tab           = 0x0f
key_back_space    = 0x0e
key_open_braces   = 0x1a
key_close_braces  = 0x1b
key_comma         = 0x33
key_period        = 0x34
key_slash         = 0x35
key_back_slash    = 0x2b
key_equals        = 0x0d
key_minus         = 0x0c
key_semicolon     = 0x27
key_apostrophe    = 0x28
key_tilde         = 0x29
key_caps_lock     = 0x3a
key_left_shift     = 0x2a
key_right_shift    = 0x36
key_left_control   = 0x1d
key_right_control  = 0x9d
key_left_alt       = 0x38
key_right_alt      = 0xb8
key_left_mouse_button   = 0xe0
key_right_mouse_button  = 0xe1
key_middle_mouse_button = 0xe2
key_mouse_button_4      = 0xe3
key_mouse_button_5      = 0xe4
key_mouse_button_6      = 0xe5
key_mouse_button_7      = 0xe6
key_mouse_button_8      = 0xe7
key_mouse_scroll_up     = 0xee
key_mouse_scroll_down   = 0xef
key_xbox_a              = 0xf0
key_xbox_b              = 0xf1
key_xbox_x              = 0xf2
key_xbox_y              = 0xf3
key_xbox_dpad_up        = 0xf4
key_xbox_dpad_down      = 0xf5
key_xbox_dpad_right     = 0xf6
key_xbox_dpad_left      = 0xf7
key_xbox_start          = 0xf8
key_xbox_back           = 0xf9
key_xbox_rbumper        = 0xfa
key_xbox_lbumper        = 0xfb
key_xbox_ltrigger       = 0xfc
key_xbox_rtrigger       = 0xfd
key_xbox_rstick         = 0xfe      
key_xbox_lstick         = 0xff

# Game keys that can be checked by game_key_is_down and game_key_clicked

gk_move_forward = 0
gk_move_backward = 1
gk_move_left = 2
gk_move_right = 3
gk_action = 4
gk_jump = 5
gk_attack = 6
gk_defend = 7
gk_kick = 8
gk_toggle_weapon_mode = 9
gk_equip_weapon_1 = 10
gk_equip_weapon_2 = 11
gk_equip_weapon_3 = 12
gk_equip_weapon_4 = 13
gk_equip_primary_weapon = 14
gk_equip_secondary_weapon = 15
gk_drop_weapon = 16
gk_sheath_weapon = 17
gk_leave = 18
gk_zoom = 19
gk_view_char = 20
gk_cam_toggle = 21
gk_view_orders = 22
gk_order_1 = 23
gk_order_2 = 24
gk_order_3 = 25
gk_order_4 = 26
gk_order_5 = 27
gk_order_6 = 28
gk_everyone_hear = 29
gk_infantry_hear = 30
gk_archers_hear = 31
gk_cavalry_hear = 32
gk_group0_hear = gk_infantry_hear
gk_group1_hear = gk_archers_hear
gk_group2_hear = gk_cavalry_hear
gk_group3_hear = 33
gk_group4_hear = 34
gk_group5_hear = 35
gk_group6_hear = 36
gk_group7_hear = 37
gk_group8_hear = 38
gk_reverse_order_group = 39
gk_everyone_around_hear = 40
gk_mp_message_all = 41
gk_mp_message_team = 42
gk_character_window = 43
gk_inventory_window = 44
gk_party_window = 45
gk_quests_window = 46
gk_game_log_window = 47
gk_quick_save = 48
gk_crouch = 49
gk_order_7 = 50
gk_order_8 = 51

#trigger positions
#------------------------------------------------------
#trigger_check_pos = 0 
#trigger_delay_pos = 1
#trigger_rearm_pos = 2
#trigger_conditions_pos = 3
#trigger_consequences_pos = 4
