import datajoint as dj

schema = dj.schema(dj.config['names.%s' % __name__], locals())


@schema
class ProcedureType(dj.Manual):
    # <class 'actions.models.ProcedureType'>
    definition = """
    procedure_id:		id                      # procedure id
    ---
    name:			varchar(255)		# name
    description:		varchar(255)		# description
    """


@schema
class Weighing(dj.Manual):
    # <class 'actions.models.Weighing'>
    definition = """
    -> Subject
    -> Appliance.WeighingScale
    weighing_id:                id                      # weighing id
    ---
    -> User
    date_time:			datetime		# date time
    weight:			float			# weight
    """


@schema
class WaterAdministration(dj.Manual):
    # <class 'actions.models.WaterAdministration'>
    # TODO: hydrogel=NULL default, nullable boolean
    definition = """
    -> User
    -> Subject
    water_administration_id:	int     		# water admin. id
    ---
    date_time:			datetime		# date time
    water_administered:		float			# water administered
    hydrogel=NULL:		[nullable] boolean	# hydrogel
    """


# XXX: OOFIXME
@schema
class BaseAction(dj.Manual):
    definition = """
    -> Subject
    -> LabLocation
    action_id:			int     	# action id
    ---
    start_time:			datetime	# start time
    end_time:			datetime	# end time
    narrative:			varchar(255)	# narrative
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
class VirusInjection(dj.Manual):
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
    definition = """
    -> BaseAction
    -> BrainLocation
    ---
    outcome_type:		varchar(255)	# outcome type
    """


@schema
class Session(dj.Manual):
    # <class 'actions.models.Session'>
    definition = """
    -> BaseAction
    ---
    type:			varchar(255)	# type
    number:			integer		# number
    """


@schema
class WaterRestriction(dj.Manual):
    # <class 'actions.models.WaterRestriction'>
    definition = """
    -> BaseAction
    """


@schema
class OtherAction(dj.Manual):
    # <class 'actions.models.OtherAction'>
    definition = """
    -> BaseAction
    """
