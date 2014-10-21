import inverse_index_lab

if __name__ == '__main__':
    lines = []
    index = {}
    f = open ('stories_small.txt')
    for line in f:
        lines.append(line)
    index = inverse_index_lab.makeInverseIndex(lines)
#    for key, val in sorted(index.items()):
#        print (key + ': ' + str(val))
        
    query1 = ['travelers', 'use', 'Baltimore', 'major-league', 'whether']
    res1 = inverse_index_lab.orSearch (index, query1)
    print ('Result of OR query: ' + str(res1))

    query2 = ['made', 'are']
    res2 = inverse_index_lab.andSearch (index, query2)
    print ('Result of AND query: ' + str(res2))
    
    query2 = ['the', 'in', 'use', 'times']
    res2 = inverse_index_lab.andSearch (index, query2)
    print ('Result of AND query: ' + str(res2))

# orSearch -  [\'travelers\', \'use\', \'Baltimore\', \'major-league\', \'whether\']
# andSearch - [\'made\', \'are\']
# andSearch - [\'the\', \'in\', \'use\', \'times\']