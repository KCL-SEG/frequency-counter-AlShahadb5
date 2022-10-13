"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies={}

    # Your code goes here

    newarray=[]

    counts = dict()

    for i in range(len(items)):
        items[i]= str(items[i])

    for i in items:

         counts[i] = counts.get(i, 0)+1
        
    return counts

