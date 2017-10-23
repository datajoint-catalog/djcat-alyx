# <class 'imaging.models.SVDCompressedMovie'>
# <class 'imaging.models.WidefieldImaging'>
# <class 'imaging.models.TwoPhotonImaging'>
# <class 'imaging.models.ROIDetection'>
# <class 'imaging.models.ROI'>
import datajoint as dj

schema = dj.schema(dj.config['FIXME'], locals())
'''
for refs:
class DataDescription(dj.Manual):
    # <class 'data.models.BaseExperimentalData> # Abstract
    definition = """
    -> Session
    -> User
    datadescription_id:		char(32)	# data id
    created:			datetime	# created
    generating_software:	varchar(255)	# generating software
    provenance_directory:	varchar(255)	# provenance directory
    """
'''


@schema
class SVDCompressedMovie(dj.Manual):
    definition = """
    -> DataDescription
    ---
    json:			varchar(255)	# json
    """

    class DataU(dj.Part):
        definition = """
        -> SVDCompressedMovie
        ---
        -> Dataset
        """

    class DataV(dj.Part):
        definition = """
        -> SVDCompressedMovie
        ---
        -> TimeSeries
        """


@schema
class WidefieldImaging(dj.Manual):
    definition = """
    -> DataDescription
    ---
    start_time:			datetime	# nominal start time
    end_time:			datetime	# nominal end time
    imaging_indicator:		varchar(255)	# imaging indicator
    preprocessing:		varchar(255)	# preprocessing
    description:		varchar(255)	# description
    excitation_wavelength:	float		# excitation nominal wavelength
    recording_wavelength:	float		# recording nominal wavelength
    recording_device:		varchar(255)	# recording device
    json:			varchar(255)	# json
    """

    class Raw(dj.Part):
        definition = """
        -> WidefieldImaging
        ---
        -> TimeSeries
        """

    class Compressed(dj.Part):
        definition = """
        -> WidefieldImaging
        ---
        -> SVDCompressedMovie
        """


@schema
class TwoPhotonImaging(dj.Manual):
    definition = """
    -> DataDescription
    ---
    description:                varchar(255)    # description
    json:			varchar(255)	# json
    (image_position)                            -> CoordinateTransformation
    excitation_wavelength:      float           # excitation wavelength
    recording_wavelength:       float           # recording wavelength
    """

    class Raw(dj.Part):
        definition = """
        -> TwoPhotonImaging
        ---
        -> TimeSeries
        """

    class Compressed(dj.Part):
        definition = """
        -> TwoPhotonImaging
        ---
        -> SVDCompressedMovie
        """


@schema
class ROIDetection(dj.Manual):
    definition = """
    -> DataDescription
    ---
    preprocessing:              varchar(255)            # preprocessing
    json:                       varchar(255)            # json
    """

    class TwoPhoton(dj.Part):
        definition = """
        -> ROIDetection
        ---
        -> TwoPhotonImaging
        """

    class RawFluorescence(dj.Part):
        definition = """
        -> ROIDetection
        ---
        -> TimeSeries
        """

    class RestingFluorescencea(dj.Part):
        definition = """
        -> ROIDetection
        ---
        -> TimeSeries
        """

    class Masks(dj.Part):
        definition = """
        -> ROIDetection
        ---
        -> Dataset
        """

    class Plane(dj.Part):
        definition = """
        -> ROIDetection
        ---
        -> Dataset
        """


@schema
class ROI(dj.Manual):
    definition = """
    -> DataDescription
    ---
    roi_type:			varchar(255)    # roi type
    optogenetic_response:       varchar(255)    # optogenetic response
    putative_cell_type:         varchar(255)    # putative cell type
    estimated_layer:            varchar(255)    # estimated layer
    -> ROIDetection
    json:                       varchar(255)    # json
    """
