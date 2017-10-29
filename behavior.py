import datajoint as dj

import actions
import reference
import equipment


schema = dj.schema(dj.config['names.%s' % __name__], locals())

'''
TODO: TimeScale items missing wrt TimeSeries items, which were:
- PupilTracking.xyd
- PupilTracking.movie
- HeadTracking.xy_theta
- HeadTracking.movie
TimeScale not yet defined
'''


@schema
class Movie(dj.Manual):
    # created to track movies
    definition = """
    movie_id:                   int             # movie id
    ---
    movie_data:                 longblob        # movie data
    """


@schema
class PupilTracking(dj.Manual):
    # <class 'behavior.models.PupilTracking'>
    definition = """
    -> actions.Session
    start_time:                 datetime        # start time
    eye:                        enum("L", "R")  # eye
    ---
    -> Movie
    x_y_d:			longblob        # x y data
    """


@schema
class HeadTracking(dj.Manual):
    # <class 'behavior.models.HeadTracking'>
    definition = """
    -> actions.Session
    start_time:                 datetime        # start time
    ---
    -> Movie
    x_y_theta:			longblob        # x y theta
    """


@schema
class OptogeneticStimulus(dj.Manual):
    # <class 'behavior.models.OptogeneticStimulus'>
    definition = """
    -> actions.Session
    -> reference.BrainLocation
    ---
    -> equipment.Appliance
    light_delivery:		varchar(255)	# light delivery
    wavelength:    		float		# wavelength
    power_calculation_method:	varchar(255)	# power calculation method
    description:		varchar(255)	# description
    """

    class Pulse(dj.Part):
        definition = """
        -> OptogeneticStimulus
        ---
        times:                  longblob        # times
        positions:              longblob        # poitions
        stimulus_power:         longblob        # stimulus power
        """


@schema
class Pharmacology(dj.Manual):
    # <class 'behavior.models.Pharmacology'>
    definition = """
    -> actions.Session
    drug:			varchar(255)	# drug
    start_time:			float		# start time
    ---
    end_time:			float		# end time
    administration_route:	varchar(255)	# administration route
    concentration:		varchar(255)	# concentration
    volume:			varchar(255)	# volume
    """
