from opentrons import protocol_api
# metadata
metadata = {'protocolName': 'Post Tagmentation Cleanup','author': 'JM','description': 'Amplicon Dilution',
    'apiLevel': '2.10'}
def run(protocol: protocol_api.ProtocolContext):
    
    # labware and pipettes
    Index = protocol.load_labware('nest_96_wellplate_2ml_deep', '5', 'Index Adapters')
    EPM = protocol.load_labware('agilent_1_reservoir_290ml', '3', 'EPM')
    
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '6', '200 tips')
    tiprackEPM = protocol.load_labware('opentrons_96_filtertiprack_200ul', '7', '200 tips EPM')
    tiprack_index = protocol.load_labware('opentrons_96_filtertiprack_200ul', '8', '200 tips index')
    wastetiprack =protocol.load_labware('opentrons_96_filtertiprack_200ul', '9', '200 waste')
    wastetiprackEPM =protocol.load_labware('opentrons_96_filtertiprack_200ul', '10', '200 waste EPM')
    wastetiprack_index = protocol.load_labware('opentrons_96_filtertiprack_200ul', '11', '200 tips index mix')

    left = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack])
    
    mag_mod = protocol.load_module('magnetic module gen2', '1' )
    TAG1 = mag_mod.load_labware('nest_96_wellplate_2ml_deep')
    

    wells = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12']


    
    mag_mod.engage(height_from_base=9)

    for well in wells:
            left.pick_up_tip(tiprack[well])
            left.speed.aspirate = 1
            left.aspirate(100, TAG1[well])
            left.drop_tip(wastetiprack[well])
            
            left.pick_up_tip(tiprackEPM[well])
            left.speed.aspirate = 10
            left.aspirate(40, EPM['A1'])
            mag_mod.disengage()
            left.dispense(40, TAG1[well])
            left.drop_tip(wastetiprackEPM[well])
            
            left.pick_up_tip(tiprack_index[well])
            left.aspirate(10, Index[well])
            left.dispense(10, TAG1[well])
            left.drop_tip(wastetiprack_index[well])
            mag_mod.engage(height_from_base=9)

    left.speed.aspirate = 50
    left.speed.dispense = 50
    
    mag_mod.disengage()
    
    for well in wells:
         
         left.pick_up_tip(wastetiprack_index[well])
         left.dispense(10, TAG1[well])
         left.mix(15, 60)
         left.drop_tip(tiprack_index[well])
    