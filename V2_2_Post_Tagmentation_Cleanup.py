from opentrons import protocol_api
# metadata
metadata = {'protocolName': 'Post Tagmentation Cleanup','author': 'JM','description': 'Amplicon Dilution',
    'apiLevel': '2.10'}
def run(protocol: protocol_api.ProtocolContext):
    
    # labware and pipettes
    ST2 = protocol.load_labware('nest_96_wellplate_2ml_deep', '5', 'ST2')
    TWB = protocol.load_labware('agilent_1_reservoir_290ml', '3', 'TWB')
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '7', '200 tips')
    tiprackwash = protocol.load_labware('opentrons_96_filtertiprack_200ul', '8', '200 tips wash')
    wastetiprack =protocol.load_labware('opentrons_96_filtertiprack_200ul', '10', '200 waste')
    wastetiprackwash =protocol.load_labware('opentrons_96_filtertiprack_200ul', '11', '200 waste')
    left = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack])
    
    mag_mod = protocol.load_module('magnetic module gen2', '1' )
    TAG1 = mag_mod.load_labware('nest_96_wellplate_2ml_deep')
    

    wells = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']

    left.speed.aspirate = 50
    left.speed.dispense = 50


    for well in wells:
            left.pick_up_tip(tiprack[well])
            left.aspirate(10, ST2['A1'])
            left.dispense(20, TAG1[well])
            left.mix(10, 70)
            left.drop_tip(wastetiprack[well])
    
    protocol.pause("Incubate for 5 minutes and refill tip rack on 7")
    mag_mod.engage(height_from_base=9)
    protocol.pause("Resume once beads are pelleted")

    for well in wells:
            left.pick_up_tip(tiprack[well])
            left.speed.aspirate = 1
            left.aspirate(70, TAG1[well])
            left.drop_tip(wastetiprack[well])
            left.pick_up_tip(tiprackwash[well])
            left.speed.aspirate = 50
            left.aspirate(100, TWB['A1'])
            mag_mod.disengage()
            left.dispense(100, TAG1[well])
            left.mix(10, 120)
            left.drop_tip(wastetiprackwash[well])
            mag_mod.engage(height_from_base=9)

    protocol.pause("refill tip racks on 7 and 8")

    for well in wells:
            left.pick_up_tip(tiprack[well])
            left.speed.aspirate = 1
            left.aspirate(100, TAG1[well])
            left.drop_tip(wastetiprack[well])
            left.pick_up_tip(tiprackwash[well])
            left.speed.aspirate = 50
            left.aspirate(100, TWB['A1'])
            mag_mod.disengage()
            left.dispense(100, TAG1[well])
            left.mix(10, 120)
            left.drop_tip(wastetiprackwash[well])
            mag_mod.engage(height_from_base=9)
        



