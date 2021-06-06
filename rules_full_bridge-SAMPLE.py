'''
THIS EXAMPLE WILL NOT WORK AS IT IS - YOU MUST SPECIFY YOUR OWN VALUES!!!

This file is organized around the "Conference Bridges" that you wish to use. If you're a c-Bridge
person, think of these as "bridge groups". You might also liken them to a "reflector". If a particular
system is "ACTIVE" on a particular conference bridge, any traffid from that system will be sent
to any other system that is active on the bridge as well. This is not an "end to end" method, because
each system must independently be activated on the bridge.

The first level (e.g. "WORLDWIDE" or "STATEWIDE" in the examples) is the name of the conference
bridge. This is any arbitrary ASCII text string you want to use. Under each conference bridge
definition are the following items -- one line for each HBSystem as defined in the main HBlink
configuration file.

    * SYSTEM - The name of the sytem as listed in the main hblink configuration file (e.g. hblink.cfg)
        This MUST be the exact same name as in the main config file!!!
    * TS - Timeslot used for matching traffic to this confernce bridge
        XLX connections should *ALWAYS* use TS 2 only.
    * TGID - Talkgroup ID used for matching traffic to this conference bridge
        XLX connections should *ALWAYS* use TG 9 only.
    * ON and OFF are LISTS of Talkgroup IDs used to trigger this system off and on. Even if you
        only want one (as shown in the ON example), it has to be in list format. None can be
        handled with an empty list, such as " 'ON': [] ".
    * TO_TYPE is timeout type. If you want to use timers, ON means when it's turned on, it will
        turn off afer the timout period and OFF means it will turn back on after the timout
        period. If you don't want to use timers, set it to anything else, but 'NONE' might be
        a good value for documentation!
    * TIMOUT is a value in minutes for the timout timer. No, I won't make it 'seconds', so don't
        ask. Timers are performance "expense".
    * RESET is a list of Talkgroup IDs that, in addition to the ON and OFF lists will cause a running
        timer to be reset. This is useful   if you are using different TGIDs for voice traffic than
        triggering. If you are not, there is NO NEED to use this feature.
'''
# REQUIRED! - Path to your full_bridge.cfg
config_file = './full_bridge.cfg'

BRIDGES_TEMPLATE = {
    'STATEWIDE': [
            {'SYSTEM': 'MASTER-1',    'TS': 2, 'TGID': 3129, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [4,], 'OFF': [7,10], 'RESET': []},
            {'SYSTEM': 'PEER-2',    'TS': 2, 'TGID': 3129, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [4,], 'OFF': [7,10], 'RESET': []},
        ],
    'ECHO': [
            {'SYSTEM': 'MASTER-1',    'TS': 2, 'TGID': 9999,    'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'ON',  'ON': [9999,], 'OFF': [9,10], 'RESET': []},
            {'SYSTEM': 'PEER-1',    'TS': 2, 'TGID': 9999, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'ON',  'ON': [9999,], 'OFF': [9,10], 'RESET': []},
            # For proxy MASTERs, just put in the name of the stanza, and rules will be generated automatically
            {'SYSTEM': 'HOTSPOT',    'TS': 2, 'TGID': 9, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [4], 'OFF': [7,10], 'RESET': []},
        ]
}

'''
list the names of each system that should NOT be bridged unit to unit (individual) calls.
'''

EXCLUDE_FROM_UNIT = ['OBP-1', 'PEER-1']

'''
Unit Call flood timeout:
The amount of time to keep sending private calls to a single system before
flooding all systems with the call. A higher value should be set for systems where subscribers
are not moving between systems often. A lower value should be set for systems that have subscribers
moving between systems often.

Time is in minutes.
'''
UNIT_TIME = 1

'''
Input the DMR ID and SYSTEM of a subscriber that you would like to have always have private calls routed.
This will not flood all systems. The last item in the entry is the timeslot. It has no effect on STATIC_UNIT. It
is only there to prevent an error in another function.
'''
STATIC_UNIT = [
#     [ 9099, 'MASTER-1', 2]
              ]

'''
Manually specify other networks/servers that are authorized to send SMS to your server
'''

authorized_users = {
##    'ABC':{
##        'mode':'msg_xfer',
##        'user':'test_name',
##        'password':'passw0rd'
##        },
##    'XYZ':{
##        'mode':'msg_xfer',
##        'user':'test_name',
##        'password':'passw0rd'
##        }
}

'''
List of external servers/networks or external applications that your users can access. The list below can be used in conjunction
with or instead of the public list.
'''

local_systems = {
# Shortcut used in SMS message
##    'XYZ':{
        # Mode of transfer, this case, message transfer
##        'mode':'msg_xfer',
        # Public or Private auth
##        'auth_type':'public',
        # Name of the server/network
##        'network_name':'My HBlink Server',
        # URL to the dashboard of the server/network
##        'url':'http://example.net/',
        # Username and password given to you by network operator
##        'user':'test_name',
##        'password':'passw0rd'
##        },
    # Shortcut used in SMS message
##    'BBD':{
        # Mode for application, operates differently than msg_xfer
##        'mode':'app',
        # Name of external application
##        'app_name':'Multi Network Bulletin Board',
        # Endpoint URL of API
##        'url':'http://hbl.ink/bb/post',
        # Website for users to get info
##        'website':'http://hbl.ink',
##        },
}




#################### Function used to build bridges for PROXY stanzas, leave alone ####################
def build_bridges():
    import sms_aprs_config, random
    CONFIG = sms_aprs_config.build_config(config_file)
    built_bridge = BRIDGES_TEMPLATE.copy()
    proxy_list = []
    unique = str('_' + str(random.randint(100, 999)))
    for i in CONFIG['SYSTEMS']:
        print(CONFIG['SYSTEMS'][i])
        if CONFIG['SYSTEMS'][i]['ENABLED'] == True:
            if CONFIG['SYSTEMS'][i]['MODE'] == 'PROXY':
                proxy_list.append(i + unique)
    for p in  proxy_list:
        for b in BRIDGES_TEMPLATE:
                for s in BRIDGES_TEMPLATE[b]:
                    if s['SYSTEM'] + unique in proxy_list:
                        n_systems = CONFIG['SYSTEMS'][p[:-4]]]['INTERNAL_PORT_STOP'] - CONFIG['SYSTEMS'][p[:-4]]]['INTERNAL_PORT_START']
                        n_count = 0
                        while n_count < n_systems:
                           built_bridge[b].append({'SYSTEM': s['SYSTEM'] + '-' + str(n_count), 'TS': s['TS'], 'TGID': s['TGID'], 'ACTIVE': s['ACTIVE'], 'TIMEOUT': s['TIMEOUT'], 'TO_TYPE': s['TO_TYPE'], 'ON': s['ON'], 'OFF': s['OFF'], 'RESET': s['RESET']})
                           n_count = n_count + 1
                        built_bridge[b].remove(s)
    return built_bridge
############################################################################################################33

'''
This is for testing the syntax of the file. It won't eliminate all errors, but running this file
like it were a Python program itself will tell you if the syntax is correct!
'''

if __name__ == '__main__':
    from pprint import pprint
    pprint(BRIDGES)
    pprint(EXCLUDE_FROM_UNIT)
