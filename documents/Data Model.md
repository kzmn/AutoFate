##Data Model

###Game
1. Name - text
2. Setting - text
3. Issues - list of text
4. Faces - Character
5. Dials - see sheet
6. Skills - list of Skill

###Skill
1. Name - text

###Character
1. Name - text
2. Description - text
3. Refresh - int
4. Aspects - list of Aspect
5. Skills - list of CharacterSkill
6. Stunts - list of Stunt
7. Extras - ?
8. StressTracks - list of StressTrack
9. Consequence - list of Aspect

###Aspect
1. Description - text
2. FreeInvoke - bool


###CharacterSkill

###Stress Track
1. Type - Enum
2. Max - int
3. Current - int