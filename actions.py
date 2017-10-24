

import datajoint as dj


schema = dj.schema(dj.config['FIXME'], locals())


@schema
class ProcedureType(dj.Manual):
    # <class 'actions.models.ProcedureType'>
    definition = """
    procedure_id:		char(32)		# procedure id
    ---
    json:			varchar(255)		# json
    name:			varchar(255)		# name
    description:		varchar(255)		# description
    """


@schema
class Weighing(dj.Manual):
    # <class 'actions.models.Weighing'>
    # XXX: is date_time name consistent with other uses?
    definition = """
    -> Subject
    -> Appliance.WeighingScale
    weighing_id:    		char(32)		# weighing id
    ---
    -> User
    date_time:			datetime		# date time
    weight:			float			# weight
    json:			varchar(255)		# json
    """


@schema
class WaterAdministration(dj.Manual):
    # <class 'actions.models.WaterAdministration'>
    # TODO: hydrogel=NULL default, nullable boolean
    definition = """
    -> User
    -> Subject
    water_administration_id:	char(32)		# water admin. id
    ---
    date_time:			datetime		# date time
    water_administered:		float			# water administered
    hydrogel:			boolean			# hydrogel
    json:			varchar(255)		# json
    """


@schema
class BaseAction(dj.Manual):
    definition = """
    -> Subject
    -> LabLocation
    action_id:			char(32)	# action id
    ---
    narrative:			varchar(255)	# narrative
    start_time:			datetime	# start time
    end_time:			datetime	# end time
    json:			varchar(255)	# json
    """

    class ActionUser(dj.Part):
        definition = """
        -> BaseAction
        -> User
        """

    class ActionProcedure(dj.Part):
        definition = """
        -> BaseAction
        -> ProcedureType
        """


@schema
class MyVirusInjection(dj.Manual):
    # <class 'actions.models.VirusInjection'>
    definition = """
    -> BaseAction
    ---
    -> VirusBatch
    injection_volume:		float		# injection volume
    rate_of_injection:		float		# rate of injection
    injection_type:		varchar(255)	# injection type
    """


@schema
class Surgery(dj.Manual):
    # <class 'actions.models.Surgery'>
    # XXX: isa BaseAction
    definition = """
    -> BaseAction
    -> BrainLocation
    ---
    outcome_type:		varchar(255)	# outcome type
    json:			varchar(255)	# json
    """


@schema
class Session(dj.Manual):
    # <class 'actions.models.Session'>
    # XXX: isa BaseAction
    definition = """
    -> BaseAction
    ---
    type:			varchar(255)	# type
    number:			integer		# number
    """


@schema
class WaterRestriction(dj.Manual):
    # <class 'actions.models.WaterRestriction'>
    # XXX: isa BaseAction
    definition = """
    -> BaseAction
    """


@schema
class OtherAction(dj.Manual):
    # <class 'actions.models.OtherAction'>
    # XXX: isa BaseAction
    definition = """
    -> BaseAction
    """
