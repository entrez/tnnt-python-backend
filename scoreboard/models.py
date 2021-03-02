from django.db import models
from . import nh, score

"""
These sources are where the scoreboard will look for xlogfile data.
"""
class LogSource(models.Model):
    url = models.CharField(max_length=500)
    src_name = models.CharField(max_length=50)
    last_check = models.DateTimeField('last accessed')

"""
A Game record corresponds to an xlogfile record and contains all the important information about that game,
whether or not the player won. This one needs to have a lot of fields to store all the relevant fields from
the xlogfile entries. Example entry from 2020 (merged xlogfile, line-wrapped for readability):
version=3.6.6	points=87	deathlev=1	maxlvl=2	hp=0	maxhp=12	deaths=1	deathdate=20201101
birthdate=20201101	role=Hea	race=Gno	gender=Mal	align=Neu	name=thorsb	death=killed by a water demon
conduct=0x11fdfcf	turns=165	achieve=0x000	tnntachieve0=0x0000000000000000	tnntachieve1=0x0000000000000000
tnntachieve2=0x0000000000000000	tnntachieve3=0x0000000000000000	realtime=74	starttime=1604188860
endtime=1604188935	gender0=Mal	align0=Neu	server=us.hardfought.org	src=hdf-eu

Data direct from the xlogfile will be listed first, with auxiliary data such as TNNT score for that game afterwards.
Most of these will be named exactly as they are in the xlogfile itself. tnntachieveX fields will be collected into
a single field, with a list of keys to the TnntAchieve model, so the parser needs to deconvolute the bitfields.
The name field will be stored as a foreign key for a Player.


"""
class Game(models.Model):
    # birth info
    version     = models.ForeignKey(nh.Version, on_delete=CASCADE)
    role        = models.ForeignKey(nh.Role, on_delete=CASCADE)
    race        = models.ForeignKey(nh.Race, on_delete=CASCADE)
    align0      = models.ForeignKey(nh.Gender, on_delete=CASCADE)
    gender0     = models.CharField(nh.Gender, on_delete=CASCADE)
    starttime   = models.DateTimeField('game start')
    birthdate   = models.DateField('birthday')

    # death info
    points      = models.BigIntegerField(default=0)
    deathlev    = models.IntegerField(default=0)
    maxlvl      = models.IntegerField(default=0)
    hp          = models.IntegerField(default=0)
    maxhp       = models.IntegerField(default=0)
    deaths      = models.IntegerField(default=0)
    turns       = models.IntegerField(default=0)
    realtime    = models.IntegerField(default=0)
    deathlev    = models.IntegerField(default=0)
    align       = models.ForeignKey(nh.Alignment, on_delete=CASCADE)
    gender      = models.ForeignKey(nh.Gender, on_delete=CASCADE)
    endtime     = models.DateTimeField('game start')
    deathdate   = models.DateField('deathday')

    # achievements and conducts
    #achievements = models.ManyToManyField(nh.Achievement)
    #conducts     = models.ManyToManyField(nh.Conduct)
    #tnnt_achieve = models.ManyToManyField(nh.TnntAchievement)
    #bones        = models.BooleanField(default=False)
    #setseed      = models.BooleanField(default=False)
    #ascended     = models.BooleanField(default=False)
    #scummed      = models.BooleanField(default=False)
    #mode         = models.ForeignKey(nh.GameMode, on_delete=CASCADE)

    # player is determined by xlog name field
    #player = models.ForeignKey(Player, on_delete=CASCADE)

    # log source
    source = models.ForeignKey(LogSource, on_delete=CASCADE)

    # what points did the given game score,
    # is it tied to any particular trophies?
    #score_entry = models.ForeignKey(score.Game, on_delete=CASCADE)
    #trophies = models.ManyToManyField(score.Trophy)


## stub
#class Player(models.Model):