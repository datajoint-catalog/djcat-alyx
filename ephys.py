import datajoint as dj

import actions
import equipment

schema = dj.schema(dj.config['names.%s' % __name__], locals())


@schema
class BrainLocation(dj.Manual):
    # XXX: not connected to reference.*
    # <class 'electrophysiology.models.BaseBrainLocation'>
    definition = """
    ccf_ap:			float		# ccf ap
    ccf_dv:			float		# ccf dv
    ccf_lr:			float		# ccf lr
    ---
    allen_ontology:		varchar(255)	# allen ontology
    json:			varchar(255)	# json
    """


@schema
class ExtracellularRecording(dj.Manual):
    # <class 'electrophysiology.models.ExtracellularRecording'>
    # <class 'electrophysiology.models.ProbeInsertion'>
    # <class 'electrophysiology.models.ProbeModel'>
    definition = """
    -> actions.Session
    start_time:                 datetime        # start time
    end_time:                   datetime        # end time
    ---
    -> equipment.Appliance.Amplifier
    -> equipment.Appliance.DAQ
    ground_electrode:		varchar(255)    # ground electrode
    reference_electrode:	varchar(255)    # reference electrode
    filter_info:		varchar(255)    # filter information
    lfp:                        longblob        # low-pass filtered
    impedance:                  longblob        # impedance
    gains:                      longblob        # gain
    """

    class Probe(dj.Part):
        # XXX: TODO: split by electrode x/y/z; tie to other data
        definition = """
        probe_id:               int             # probe id
        ---
        -> BrainLocation
        -> equipment.Appliance.ProbeModel
        site_positions:         blob            # probe site positions
        channel_mapping:        blob            # channel mapping
        """


@schema
class SpikeSorting(dj.Manual):
    # <class 'electrophysiology.models.SpikeSorting'>
    definition = """
    -> ExtracellularRecording
    ---
    """

    class Unit(dj.Part):
        # <class 'electrophysiology.models.SpikeSortedUnit'>
        # TODO: CLUSTER_GROUPS
        # TODO: WIDTH_CLASSES
        definition = """
        -> BrainLocation
        -> SpikeSorting
        cluster_number:         integer         # cluster number
        ---
        channel_group:          integer         # channel group
        width:                  float		# trough to peak width
        half_width:             float		# half width
        amplitude:              float		# trough to peak amplitude
        rvr:                    float		# refractory violation rate
        isolation_distance:     float		# isolation distance
        l_ratio:                float		# l ratio
        mean_firing_rate:	float		# mean firing rate
        cluster_group:          varchar(255)	# cluster group
        spike_width_class:	varchar(255)	# spike width class
        optogenetic_response:   varchar(255)	# optogenetic response
        putative_cell_type:	varchar(255)	# putative cell type
        """


@schema
class IntracellularRecording(dj.Manual):
    # <class 'electrophysiology.models.IntracellularRecording'>
    definition = """
    -> actions.Session
    -> BrainLocation
    ---
    recorded_current:           longblob        # recorded current
    current_command:            longblob        # current command
    recorded_voltage:           longblob        # recorded voltage
    voltage_command:            longblob        # voltage command
    electrode_type:             enum("W", "S")  # electrode type
    -> equipment.Appliance.PipettePuller	# pipette puller
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
    """
