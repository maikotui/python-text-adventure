import re

re_dict = {
    'use_obj': re.compile(r'^use (\w+)$'),
    'use_obj_on_obj': re.compile(r'^use (\w+) on (\w+)$'),
    'take_obj': re.compile(r'^take (\w+)$'),
    'take_obj_from_obj': re.compile(r'^take (\w+) from (\w+)$'),
    'inspect_obj': re.compile(r'^inspect (\w+)$')
}

actions = {
    'use': "use interact operate weild utilize",
    'take': "take store grab hold",
    'inspect': "inspect examine investigate check probe survey",
    'turn': "turn look glance peer"
}

directions = ["north", "south", "east", "west", "up", "down", "left", "right", "in", "out", "forward", "back"]

def simple_parse(command):
    parsed_command = {
        'valid_command': False,
        'action': None,
        'direction': None,
        'primary_object': None,
        'secondary_object': None
    }

    split_command = command.split()
    if len(split_command) < 1:
        return split_command

    if any(x in split_command[0].lower() for x in actions['use'].split()):
        parsed_command['action'] = 'use'
        m1 = re_dict['use_obj_on_obj'].match(command)
        m2 = re_dict['use_obj'].match(command)
        if(m1):
            parsed_command['primary_object'] = m1.group(1)
            parsed_command['secondary_object'] = m1.group(2)
            parsed_command['valid_command'] = True
            return parsed_command
        elif(m2):
            parsed_command['primary_object'] = m2.group(1)
            parsed_command['valid_command'] = True
            return parsed_command
        
    if any(x in split_command[0].lower() for x in actions['take'].split()):
        parsed_command['action'] = 'take'
        m1 = re_dict['take_obj_from_obj'].match(command)
        m2 = re_dict['take_obj'].match(command)
        if(m1):
            parsed_command['primary_object'] = m1.group(1)
            parsed_command['secondary_object'] = m1.group(2)
            parsed_command['valid_command'] = True
            return parsed_command
        elif(m2):
            parsed_command['primary_object'] = m2.group(1)
            parsed_command['valid_command'] = True
            return parsed_command

    if any(x in split_command[0].lower() for x in actions['inspect'].split()):
        parsed_command['action'] = 'inspect'
        m1 = re_dict['inspect_obj'].match(command)
        if(m1):
            parsed_command['primary_object'] = m1.group(1)
            parsed_command['valid_command'] = True
            return parsed_command

    if any(x in split_command[0].lower() for x in actions['turn'].split()):
        parsed_command['action'] = 'turn'

    return parsed_command