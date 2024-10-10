from opentrons import protocol_api
# metadata
metadata = {'protocolName': 'LoCost Protocol, Part 1 of 4','author': 'JM','description': 'Amplicon Dilution',
    'apiLevel': '2.10'}
def run(protocol: protocol_api.ProtocolContext):
    
    # labware and pipettes
    TAG1 = protocol.load_labware('nest_96_wellplate_2ml_deep', '6', 'TAG1')
    pool_1 = protocol.load_labware('nest_96_wellplate_2ml_deep', '8', 'Pool 1')
    pool_2 = protocol.load_labware('nest_96_wellplate_2ml_deep', '9', 'Pool 2')
    trough = protocol.load_labware('agilent_1_reservoir_290ml', '7', 'trough')
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '10', '200 tips')
    wastetiprack =protocol.load_labware('opentrons_96_filtertiprack_200ul', '3', '200 waste')
    left = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack])
    
    # commands
    # Transfer water from trough to wells without removing tips

    # Transfer water from trough and DNA amplicons from primer pool 1 and primer pool 2 into dilution plate

    wells = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12']

    for well in wells:
        left.pick_up_tip(tiprack[well])
        left.aspirate(30, trough['A1'])
        left.aspirate(10, pool_1[well])
        left.aspirate(10, pool_2[well])
        left.dispense(50, TAG1[well])
        left.speed.aspirate = 50
        left.speed.dispense = 50
        left.mix(8, 30)
        left.speed.aspirate = 10
        left.speed.dispense = 10
        left.drop_tip(wastetiprack[well])