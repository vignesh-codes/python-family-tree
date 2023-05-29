The program was tested with Python 3.9.12 - (make sure to run with python3.x)


Things that are done:
- Add family member via cli 
- connect family member based on person1 -> person2 in any order with relationship
- added conditions in cli to handle for each action cases(count, add, connect)
- conditions to check if person relationship can be made
- get count related outputs in constant time
- get ancestors, next generation family members list using bfs
- get daughters, sons of given person name
- added date of birth and date of death in Person as additional entities
- added help in cli to give possible actions and examples that could be built up in future (family-tree help)
- added possible prefix in cli (only family-tree is allowed)
- added possible actions in cli in its class


- Created a seperate class for person, family-tree and cli functinalities
- Few assumptions were made: no duplicate family names were allowed(for constant lookups),
    -- spouse instead of husband and wife relation,
    -- male and female entities for each person should be assigned while adding to data structure


The heirarchy is already created from initFamily function, you can perform the cli queries for testing.


Few cli that you could try
```
>>> family-tree mother of judith
Output - mother name of  judith is:  anne hathaway

>>> family-tree children of william
Output - children of  william  are:  ['judith', 'susanna', 'hamnet']

>>> family-tree count spouse of william

>>> family-tree children of john sh

>>> family-tree ancestors of elizabeth

>>> family-tree generations of john sh

>>> family-tree count sons of mary a

>>> family-tree count children of judith

>>> family-tree add joe biden male
>>> family-tree add joe mom female
>>> family-tree connect joe mom as spouse of thomas

>>> family-tree connect joe biden as son of thomas
>>> family-tree connect joe mom as mother of joe biden
Note that the order is different the way we connect. vice versa will also work

>>> family-tree father of joe biden
>>> family-tree mother of joe biden

>>> family-tree update name thomas to president dad
Note that all objects having relations with thomas will be updated

>>> family-tree father of joe biden
>>> family-tree children of thomas quiney

>>> family-tree help

```
