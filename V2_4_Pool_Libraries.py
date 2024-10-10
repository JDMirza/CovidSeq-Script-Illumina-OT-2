from opentrons import protocol_api
# metadata
metadata = {'protocolName': 'LoCost Protocol, Part 4 of 4','author': 'JM','description': 'Pooling',
    'apiLevel': '2.10'}
def run(protocol: protocol_api.ProtocolContext):

    # labware and pipettes
    mag_mod = protocol.load_module('magnetic module gen2', '1' )
    TAG1 = mag_mod.load_labware('nest_96_wellplate_2ml_deep')
    strip = protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '3', 'strip')
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_20ul', '4', '20 tips')
    wastetiprack =protocol.load_labware('opentrons_96_filtertiprack_20ul', '10', 'waste tips')
    right = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tiprack])
    
    # commands
    # pool samples into strip tube
    mag_mod.engage(height_from_base=12)
    
    right.speed.aspirate = 1
    right.pick_up_tip(tiprack['A1'])
    right.consolidate(5, TAG1.columns(), strip.wells_by_name()['A1'], new_tip='never')
    right.drop_tip(wastetiprack['A1'])