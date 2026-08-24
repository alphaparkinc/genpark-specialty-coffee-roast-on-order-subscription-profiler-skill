from client import SpecialtyCoffeeRoastOnOrderSubscriptionProfilerClient

def main():
    client = SpecialtyCoffeeRoastOnOrderSubscriptionProfilerClient()
    res = client.profile_and_roast_batch('Pour-Over (V60)', 'citrus_bright')
    print('Estate: ' + res['estate_origin'] + ' (' + res['varietal'] + ')')
    print('SCA Cupping Score: ' + str(res['sca_cupping_score']) + ' pts | Roast: ' + res['roast_level'])
    print('Tasting Notes: ' + ', '.join(res['tasting_notes']) + ' (Freshness: ' + str(res['roast_to_door_freshness_hours']) + ' hrs)')

if __name__ == '__main__':
    main()
