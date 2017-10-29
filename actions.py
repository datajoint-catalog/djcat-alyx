import datajoint as dj


import reference
import subject
import equipment

schema = dj.schema(dj.config['names.%s' % __name__], locals())

#
# New
#
# Refactor questions w/r/t old objs:
# - <class 'actions.models.ProcedureType'>: SKIPPED
#   What does this do aside from provide a description?
#   should be inclued for e.g. steps, etc?
# - <class 'actions.models.BaseAction'>: SKIPPED
#   Other than key info, does this provide anything other than 'narritive'?
#   if so, needed?
#


@schema
class Weighing(dj.Manual):
    # <class 'actions.models.Weighing'>
    definition = """
    -> subject.Subject
    weighing_time:		datetime		# date time
    ---
    weight:			float			# weight
    -> equipment.Appliance.WeighingScale
    -> reference.User
    """


@schema
class WaterAdministration(dj.Manual):
    # <class 'actions.models.WaterAdministration'>
    definition = """
    -> subject.Subject
    administration_time:	datetime		# date time
    ---
    water_administered:		float			# water administered
    hydrogel=NULL:		boolean                 # hydrogel
    -> reference.User
    """


@schema
class VirusInjection(dj.Manual):
    # <class 'actions.models.VirusInjection'>
    # XXX: user was m2m field in django
    definition = """
    -> subject.Subject
    -> equipment.VirusBatch
    injection_time:		datetime        	# injection time
    ---
    injection_volume:		float   		# injection volume
    rate_of_injection:		float                   # rate of injection
    injection_type:		varchar(255)    	# injection type
    -> equipment.LabLocation
    -> reference.User
    """


@schema
class Surgery(dj.Manual):
    # <class 'actions.models.Surgery'>
    definition = """
    -> subject.Subject
    -> reference.BrainLocation
    surgery_start_time:		datetime        # surgery start time
    ---
    surgery_end_time:		datetime        # surgery end time
    outcome_type:		varchar(255)	# outcome type
    narrative:			varchar(255)	# narrative
    -> equipment.LabLocation
    -> reference.User
    """


@schema
class Session(dj.Manual):
    # <class 'actions.models.Session'>
    # XXX: session_type table?
    definition = """
    -> subject.Subject
    session_number:             integer		# number
    ---
    session_start_time:         datetime	# start time
    session_end_time:           datetime	# end time
    session_type:		varchar(255)	# type
    -> equipment.LabLocation
    -> reference.User
    """


@schema
class WaterRestriction(dj.Manual):
    # <class 'actions.models.WaterRestriction'>
    definition = """
    -> subject.Subject
    restriction_start_time:     datetime	# start time
    ---
    restriction_end_time:       datetime	# end time
    -> equipment.LabLocation
    -> reference.User
    """


@schema
class OtherAction(dj.Manual):
    # <class 'actions.models.OtherAction'>
    definition = """
    -> subject.Subject
    other_action_start_time:    datetime	# start time
    ---
    other_action_end_time:      datetime	# end time
    descrption:                 varchar(255)    # description
    -> equipment.LabLocation
    -> reference.User
    """
