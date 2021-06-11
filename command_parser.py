import re

# A collection of regex searches used by the command parser
re_dict = {
    'use_obj': re.compile(r'^use (\w+)$'),
    'use_obj_on_obj': re.compile(r'^use (\w+) on (\w+)$'),
    'take_obj': re.compile(r'^take (\w+)$'),
    'take_obj_from_obj': re.compile(r'^take (\w+) from (\w+)$'),
    'inspect_obj': re.compile(r'^inspect (\w+)$')
}

# Alternative names for each of the four key actions
action_aliases = {
    'use': "use interact operate weild utilize",
    'take': "take store grab hold",
    'inspect': "inspect examine investigate check probe survey",
    'turn': "turn look glance peer"
}

# Accepted directions used by the "turn" command
directions = ["north", "south", "east", "west", "up", "down", "left", "right", "in", "out", "forward", "back"]

def simple_parse(command):
    """Parses given command without using NLP.
    
    Returns a dictionary with the following values:
    valid_command -- whether the command was correctly formatted
    action -- the main action the user wants to take (see 'command_parser.action_aliases')
    direction -- if the action is turn, this is the direction to turn towards
    primary_object -- the name of the object that is being used by the action (if applicable)
    secondary_object -- the name of the second object that is being used by the action (if applicable)
    """

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

    # This section parses the 'use' command.
    # It accepts both "use x" and "use x on y" statements
    if any(x in split_command[0].lower() for x in action_aliases['use'].split()):
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

    # This section parses the 'take' command.
    # It accepts both "take x" and "take x from y" statements
    if any(x in split_command[0].lower() for x in action_aliases['take'].split()):
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

    # This section parses the 'inspect' command.
    # It accepts the statement "inspect x".
    if any(x in split_command[0].lower() for x in action_aliases['inspect'].split()):
        parsed_command['action'] = 'inspect'
        m1 = re_dict['inspect_obj'].match(command)
        if(m1):  # TODO: Add 'inspect direction' implementation
            parsed_command['primary_object'] = m1.group(1)
            parsed_command['valid_command'] = True
            return parsed_command

    # This section parses the 'turn' command.
    # It accepts the statement "turn x" where x is a direction.
    if any(x in split_command[0].lower() for x in action_aliases['turn'].split()):
        parsed_command['action'] = 'turn'

    return parsed_command