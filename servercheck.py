"""Server Updates

This program creates two sets from the contents of two files by
nesting an open within a list function which is within a set
function.  While this level of nesting is not recommended, it's
good to know it actually works.

The servers set contains a master list of servers to be updated.
The updates set contains the latest set of servers that have been
updated.  The update items are submitted manually by the admin
responsible for the server.  Sometimes, they are not accurate.
"""

# updates = set(open('c:/pydata/serverupdates.txt', 'r'))
# servers = set(open('c:/pydata/servers.txt', 'r'))
updates = set(open('serverupdates.txt', 'r'))
servers = set(open('servers.txt', 'r'))
updatedservers = open('updatedservers.txt', 'wt')

def checkservers():
    #determine whether the list of updates exists in the servers lists
    if updates in servers:
        return(True)
    else:
        return(False)

def incorrectservers():
    #create a list of servers in the update list that are NOT in the master list
    incservers = updates - servers
    return(incservers)

if checkservers()==False:
    incorrectservers = incorrectservers()
    print(len(incorrectservers))
    print("Number of servers reported updated:", len(updates))
    updates = updates - incorrectservers
    print("Numbers of servers updated after incorrect names removed:", len(updates))
else:
    print("Number of servers reported updated:", len(updates))

print("Number of servers before updates:", len(servers))
updservers = servers - updates
print("Number of servers after updates:", len(updservers))

updatedservers.writelines(updservers)
