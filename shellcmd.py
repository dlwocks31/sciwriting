from statistics import mean, median, stdev
import json
from experiment.models import User, Result

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def get_all_firstresult(uid_min=0):
    ls = list(u for u in User.objects.all() if u.firstresult and u.id > uid_min)
    data_hastime = []
    data_notime = []
    for u in ls:
        rawdata = json.loads(u.firstresult.data)
        if rawdata['mode'] == 'hastime':
            data_hastime.append({k:v for k,v in rawdata.items() if k != 'mode'})
        elif rawdata['mode'] == 'notime':
            data_notime.append({k:v for k,v in rawdata.items() if k != 'mode'})
    return data_hastime, data_notime

def analyze_average_final_time(data):
    avg = mean(int(d['answeredTime'][-1]) for d in data)
    med = median(int(d['answeredTime'][-1]) for d in data)
    std = stdev(int(d['answeredTime'][-1]) for d in data)
    return avg, med, std

def analyze_average_correct(data):
    avg = mean(mean(d['iscorrect']) for d in data)
    med = median(mean(d['iscorrect']) for d in data)
    std = stdev(mean(d['iscorrect']) for d in data)
    return avg, med, std

def analyze_question_time(data):
    qdict = dict()
    for d in data:
        for i, q in enumerate(d['questions']):
            has = q in qdict
            if has:
                qdict[q].append(d['answeredTime'][i] if i == 0 else d['answeredTime'][i]-d['answeredTime'][i-1])
            else:
                qdict[q] = [d['answeredTime'][i] if i == 0 else d['answeredTime'][i]-d['answeredTime'][i-1]]
    return {k:(mean(v), median(v), stdev(v) if len(v)>=2 else 0) for k,v in qdict.items()}

if __name__ == '__main__':
    __import__('code').interact('Sciwriting data analyze shell', local=locals())