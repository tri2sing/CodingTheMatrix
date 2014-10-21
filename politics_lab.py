voting_data = list(open("voting_record_dump109.txt"))

democrats = set()
republicans = set()
independents = set()

for line in voting_data:
    parts = line.split()
    name = parts[0]
    if parts[1] == 'D': democrats.add(name)
    elif parts[1] == 'R': republicans.add(name)
    else: independents.add(name)
        
## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    parsed = {}
    for line in voting_data:
        parts = line.split()
        name = parts[0]
        votes = [int(x) for x in parts[3:]]
        parsed[name] = votes
       
    return parsed
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    list_a = voting_dict[sen_a]
    list_b = voting_dict[sen_b]
    comparison = sum([list_a[i] * list_b[i] for i in range(len(list_a))])
    return comparison


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    comparisons = {name: policy_compare (sen, name, voting_dict) for name in voting_dict if name != sen}
    maxkey = max (comparisons, key = comparisons.get)
    return maxkey
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    comparisons = {name: policy_compare (sen, name, voting_dict) for name in voting_dict if name != sen}
    minkey = min (comparisons, key = comparisons.get)
    return minkey
    
    

## Task 5
v_d = create_voting_dict()
most_like_chafee    = most_similar('Chafee', v_d)
least_like_santorum = least_similar('Santorum', v_d)

# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    return sum([policy_compare(sen, name, voting_dict) for name in sen_set])/len(sen_set)
    


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    votes = [voting_dict[sen] for sen in sen_set]
    zipped = zip(*votes)
    avg_votes = [sum(z)/len(z) for z in zipped]
    return avg_votes

average_Democrat_record = find_average_record (democrats, v_d)

dem_v_d = {name:v_d[name] for name in democrats}
dem_v_d['Average'] = average_Democrat_record

most_average_Democrat = most_similar ('Average', dem_v_d) # give the last name (or code that computes the last name)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    comparisons = {(j,k): policy_compare (j, k, voting_dict) for j in voting_dict for k in voting_dict if j != k} 
    bitterest = min (comparisons, key = comparisons.get)
    return bitterest

