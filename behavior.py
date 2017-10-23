
import datajoint as dj

schema = dj.schema(dj.config['FIXME'], locals())

# Note:
# skipped:
#   <class 'behavior.models.EventSeries'>
#   <class 'behavior.models.IntervalSeries'>
# since these appear to be duplicatedd w.r.t data.models.* copy.


@schema
class PupilTracking(dj.Manual):
    # <class 'behavior.models.PupilTracking'>
    definition = """
    -> DataDescription
    pupil_tracking_id:		char(32)		# id
    ---
    (x_y_d)			-> TimeSeries		# x y data
    (movie)			-> TimeSeries		# movie
    eye:			varchar(255)		# eye
    description:		varchar(255)		# description
    json:			varchar(255)		# json
    """


@schema
class HeadTracking(dj.Manual):
    # <class 'behavior.models.HeadTracking'>
    definition = """
    -> DataDescription
    head_tracking_id:		char(32)		# id
    ---
    (x_y_theta)			-> TimeSeries		# x y theta
    (movie)			-> TimeSeries		# movie
    description:		varchar(255)		# description
    json:			varchar(255)		# json
    """


@schema
class OptogeneticStimulus(dj.Manual):
    # <class 'behavior.models.OptogeneticStimulus'>
    definition = """
    -> DataDescription
    -> BrainLocation
    ---
    description:		varchar(255)	# description
    -> Appliance
    light_delivery:		varchar(255)	# light delivery
    wavelength:    		float		# wavelength
    power_calculation_method:	varchar(255)	# power calculation method
    json:			varchar(255)	# json
    """

    class Time(dj.Part):
        definition = """
        -> OptogeneticStimulus
        -> Dataset				# times
        """

    class Position(dj.Part):
        definition = """
        -> OptogeneticStimulus
        -> Dataset				# positions
        """

    class Power(dj.Part):
        definition = """
        -> OptogeneticStimulus
        -> Dataset				# stimulus power
        """


@schema
class Pharmacology(dj.Manual):
    # <class 'behavior.models.Pharmacology'>
    definition = """
    -> DataDescription
    pharmacology_id:		char(32)	# pharmacology id
    ---
    drug:			varchar(255)	# drug
    administration_route:	varchar(255)	# administration route
    start_time:			float		# start time
    end_time:			float		# end time
    concentration:		varchar(255)	# concentration
    volume:			varchar(255)	# volume
    json:			varchar(255)	# json
    """
