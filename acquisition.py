
import datajoint as dj
schema = dj.schema(dj.config['FIXME'], locals())
'''
class deps/inheretance notes from Alyx.data.models
- BaseExperimenalData
  - Dataset
  - DataCollection
    - TimeSeries (DataCollection + timescale & timestamps)
    - EventSeries (DataCollection + timescale & timestamp id)
  - IntervalSeries (DataCollection + timescale & timestamp id)
# examples of subclasses from other Alyx modules:
  - OptogeneticStimulus -> Dataset
  - ExtracellularRecording -> {DataCollection, Timescale, TimeSeries}

Method (for now): modeling DataCollection, etc directly -
and client tables will refer here - not a very natively dj construction,
but somewhat preserves upstream notions of provenance, etc.
and preserves notion that reference.Note should apply to objects,
even if it doesn't apply to datajoint direcly.

TODO: Narrowing of relations to make keys fit?
 ... or alternate approach overall..
'''


@schema
class DataRepositoryType(dj.Lookup):
    # <class 'data.models.DataRepositoryType'>
    # TODO: Some default values please?
    # XXX: repository_type is referred elsewhere - attribute name ok?
    definition = """
    repository_type:		varchar(255)		# name
    ---
    json:			varchar(255)		# json
    """


@schema
class DataRepository(dj.Manual):
    # <class 'data.models.DataRepository'>
    definition = """
    -> DataRepositoryType
    data_repository_name:	varchar(255)		# data repository name
    ---
    path:			varchar(255)		# path
    json:			varchar(255)		# json
    """


@schema
class DatasetType(dj.Lookup):
    # <class 'data.models.DatasetType'>
    definition = """
    dataset_type_name:		varchar(255)		# name
    ---
    json:			varchar(255)		# json
    """


@schema
class DataDescription(dj.Manual):
    # <class 'data.models.BaseExperimentalData> # Abstract
    definition = """
    -> Session
    -> User
    datadescription_id:		char(32)		# data id
    created:			datetime		# created
    generating_software:	varchar(255)		# generating software
    provenance_directory:	varchar(255)		# provenance directory
    """


@schema
class Dataset(dj.Manual):
    # <class 'data.models.Dataset'>
    definition = """
    -> DataDescription
    ---
    -> DatasetType
    name:			varchar(255)		# name
    md5:			char(32)		# md5
    json:			varchar(255)		# json
    """

    class FileRecord(dj.Part):
        # <class 'data.models.FileRecord'>
        # ''' "Normally specified by a path within an archive" '''
        definition = """
        -> Dataset
        file_record_id:		char(32)		# dataset id
        ---
        -> DataRepository
        relative_path:		varchar(255)		# relative path
        json:			varchar(255)		# json
        """


@schema
class DataCollection(dj.Manual):
    # <class 'data.models.DataCollection'>
    definition = """
    -> DataDescription
    """

    class DataMember(dj.Part):
        definition = """
        -> DataCollection
        -> Dataset
        """


@schema
class Timescale(dj.Manual):
    # <class 'data.models.Timescale'>
    # original spec makes session mandatory and series/experiment optional
    definition = """
    timescale_id:		char(32)		# id
    ---
    timescale_name:		varchar(255)		# name
    nominal_start:		datetime		# nominal start
    nominal_time_unit:		float			# nominal time unit
    final:			boolean			# final
    info:			varchar(255)		# info
    json:			varchar(255)		# json
    """


@schema
class TimeSeries(dj.Manual):
    # <class 'data.models.TimeSeries'>
    definition = """
    -> DataDescription
    -> Timescale
    -> Dataset						# timestamps
    """


@schema
class EventSeries(dj.Manual):
    # <class 'data.models.EventSeries'>
    definition = """
    -> DataDescription
    -> Timescale
    -> Dataset						# event times
    """


@schema
class IntervalSeries(dj.Manual):
    # <class 'data.models.IntervalSeries'>
    definition = """
    -> DataDescription
    -> Timescale
    -> Dataset						# intervals
    """
