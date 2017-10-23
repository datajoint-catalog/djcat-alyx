
import datajoint as dj

schema = dj.schema(dj.config['FIXME'], locals())


@schema
class ExtracellularRecording(dj.Manual):
    # <class 'electrophysiology.models.ExtracellularRecording'>
    # isa timeseries
    # todo: RECORDING_TYPES
    definition = """
    -> TimeSeries
    ---
    filter_info:		varchar(255)		# filter information
    ground_electrode:		varchar(255)		# ground electrode
    reference_electrode:	varchar(255)		# reference electrode
    -> Appliance.Amplifier
    -> Appliance.DAQ
    json:			varchar(255)		# json
    """

    class LFP(dj.Part):
        definition = """
        -> ExtracellularRecording
        -> TimeSeries
        """

    class Impedances(dj.Part):
        definition = """
        -> ExtracellularRecording
        -> TimeSeries
        """

    class Gains(dj.Part):
        definition = """
        -> ExtracellularRecording
        -> TimeSeries
        """


@schema
class ProbeModel(dj.Manual):
    # <class 'electrophysiology.models.ProbeModel'>
    definition = """
    -> Supplier
    ---
    probe_model:		varchar(255)		# probe model
    description:		varchar(255)		# description
    json:			varchar(255)		# json
    """

    class SitePositions(dj.Part):
        definition = """
        -> ProbeModel
        ---
        -> Dataset
        """


@schema
class ProbeInsertion(dj.Manual):
    # <class 'electrophysiology.models.ProbeInsertion'>
    definition = """
    -> ExtracellularRecording
    -> ProbeModel
    ---
    entry_point_rl:		float			# entry point rl
    entry_point_ap:		float			# entry point ap
    vertical_angle:		float			# vertical angle
    horizontal_angle:		float			# horizontal angle
    distance_advanced:		float			# distance advanced
    axial_angle:		float			# axial angle
    json:			varchar(255)		# json
    """

    class ChannelMapping(dj.Part):
        definition = """
        -> ProbeInsertion
        ---
        -> Dataset
        """


@schema
class BaseBrainLocation(dj.Manual):
    # <class 'electrophysiology.models.BaseBrainLocation'>
    definition = """
    ccf_ap:			float			# ccf ap
    ccf_dv:			float			# ccf dv
    ccf_lr:			float			# ccf lr
    ---
    allen_ontology:		varchar(255)		# allen ontology
    json:			varchar(255)		# json
    """


@schema
class RecordingSite(dj.Manual):
    # <class 'electrophysiology.models.RecordingSite'>
    definition = """
    -> BaseBrainLocation
    -> ProbeInsertion
    ---
    allen_ontology:		varchar(255)		# allen ontology
    site_no:			integer			# site no
    json:			varchar(255)		# json
    """


@schema
class SpikeSorting(dj.Manual):
    # <class 'electrophysiology.models.SpikeSorting'>
    # isa: EventSeries
    definition = """
    -> EventSeries
    ---
    json:    varchar(255) # json
    """

    class Recording(dj.Part):
        definition = """
        -> SpikeSorting
        ---
        -> ExtracellularRecording
        """

    class Probe(dj.Part):
        definition = """
        -> SpikeSorting
        ---
        -> ExtracellularRecording
        """


@schema
class SpikeSortedUnit(dj.Manual):
    # <class 'electrophysiology.models.SpikeSortedUnit'>
    # TODO: CLUSTER_GROUPS
    # TODO: WIDTH_CLASSES
    definition = """
    -> BaseBrainLocation
    -> SpikeSorting
    cluster_number:		integer		# cluster number
    ---
    channel_group:		integer		# channel group
    trough_to_peak_width:	float		# trough to peak width
    half_width:			float		# half width
    trough_to_peak_amplitude:	float		# trough to peak amplitude
    refractory_violation_rate:	float		# refractory violation rate
    isolation_distance:		float		# isolation distance
    l_ratio:			float		# l ratio
    mean_firing_rate:		float		# mean firing rate
    cluster_group:		varchar(255)	# cluster group
    spike_width_class:		varchar(255)	# spike width class
    optogenetic_response:	varchar(255)	# optogenetic response
    putative_cell_type:		varchar(255)	# putative cell type
    """


@schema
class IntracellularRecording(dj.Manual):
    # <class 'electrophysiology.models.IntracellularRecording'>
    # TODO: ELECTRODE_TYPES
    definition = """
    -> DataDescription
    -> BrainLocation
    -> Dataset
    ---
    electrode_type:		varchar(255)	# electrode type
    -> Appliance.PipettePuller			# pipette puller
    inner_diameter:		float		# inner diameter
    outer_diameter:		float		# outer diameter
    electrode_solution:		varchar(255)	# electrode solution
    cp_fast:			float		# cp fast
    cp_slow:			float		# cp slow
    cell_cap_comp:		float		# whole cell cap comp
    cell_series_resistance:	float		# whole cell series resistance
    src_bandwidth:		float		# src bandwidth
    src_correction:		float		# src correction
    src_prediction:		float		# src prediction
    pipette_cap_comp:		float		# pipette cap comp
    bridge_balance:		float		# bridge balance
    gain:			float		# gain
    json:			varchar(255)	# json
    """

    class Current(dj.Part):
        definition = """
        -> IntracellularRecording
        ---
        -> Dataset
        """

    class Voltage(dj.Part):
        definition = """
        -> IntracellularRecording
        ---
        -> Dataset
        """
