import json
class Disaster:
    def severity_filter(data):
        return sorted(data, key=lambda x: x['severity'])
    
    def count_incidents(data):
        open = 0
        resolved = 0
        for val in data:
            if data['status'] == 'resolved':
                resolved+=1
            elif data['status'] == 'open':
                open+=1
        data['open count'] = open
        data['resolved count'] = resolved

    def available(rescue):
        available_teams = []
        for res in rescue:
            if res['status'] == 'available':
                available_teams.append(res)
        return available_teams
    
    def write_report():
        data = [
            { 'id' : 1001,
             'status': 'open',
             'severity': 4
             },
             { 'id' : 1002,
             'status': 'resolved',
             'severity': 3
             },
             { 'id' : 1003,
             'status': 'resolved',
             'severity': 5
             },
             { 'id' : 1004,
             'status': 'open',
             'severity': 3
             },
             { 'id' : 1005,
             'status': 'open',
             'severity': 2
             }
        ]
        rescue = [
            { 'id' : 101,
             'status': 'available',
             },
             { 'id' : 102,
             'status': 'not available',
             },
             { 'id' : 103,
             'status': 'available',
             },
        ]
        with open('report.txt', 'w') as f:
            f.write('Data on incidents')
            f.write('\n')
            f.write(data)
            f.write('Teams data')
            f.write('\n')
            f.write(rescue)


            

        

    
