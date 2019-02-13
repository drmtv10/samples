
import pprint

# transform a json like formatted item containing nested dict, list
# into a flat list of tuples 
def flatten(cntner, pfxkeywd = ''):
    """
    input:
    cntner - container object that contains nested dictionaries, lists, etc
    pfxkeywd - pre-fix keyword to use for tuples
    output (returns):
    list of touples.
    """
    flatlist=list()
    if isinstance(cntner, dict):
        for k,v in cntner.items():
            #print k, v
            if isinstance(v, dict) or isinstance(v, list):
                flatlist += flatten(v,k)
            else:
                flatlist.append((pfxkeywd+k, v))
            #pprint.pprint(flist)
    if isinstance(cntner, list):
        for k in range(len(cntner)):
            #print k, cntner[k]
            if isinstance(cntner[k], dict) or isinstance(cntner[k], list):
                flatlist += flatten(cntner[k], str(k))
            else:
                flatlist.append((pfxkeywd+str(k), cntner[k]))
            #pprint.pprint(flist)
    return flatlist


if __name__ == '__main__':
    ijson={'k1':'v1','sd':{'k2':'v2'},'ls':['v3','v4']}
    print('input json={}'.format(ijson))
    f_ijson = flatten(ijson)
    pprint.pprint(f_ijson)

##### SAMPLE RUN and output #####
#input json={'k1': 'v1', 'ls': ['v3', 'v4'], 'sd': {'k2': 'v2'}}
#[('k1', 'v1'), ('ls0', 'v3'), ('ls1', 'v4'), ('sdk2', 'v2')]
##### ------
