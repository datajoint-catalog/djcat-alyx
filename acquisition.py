import datajoint as dj

schema = dj.schema(dj.config['names.%s' % __name__], locals())


# To simplify from Alyx schema,
# dropping file repositories as core parts of tables and moving
# to per-table blobs. A facility for tracking data provenance is still
# made avaialble via 'DataDescription' which can be linked into individual
# model records as a non-primary attribute.
#
# This is probably not ideal w/r/t Alyx -
# one idea would be to merge with external storage when it is available:
#
# see also: https://github.com/datajoint/datajoint-python/issues/204
#
# with example field def being:
#
#   aligned_movie :  external  # motion-aligned movie
#
# And have a separate 'phase 1' data schema,
# which is then coupled with phase 2+ for higher level data products.


# SKIPPED:
# <class 'data.models.DataRepositoryType'>
# <class 'data.models.DataRepository'>
# <class 'data.models.DatasetType'>
# <class 'data.models.Dataset'>
# <class 'data.models.FileRecord'>
# <class 'data.models.DataCollection'>
# <class 'data.models.Timescale'>
# <class 'data.models.TimeSeries'>
# <class 'data.models.EventSeries'>
# <class 'data.models.IntervalSeries'>


@schema
class DataDescription(dj.Manual):
    # FIXME: SKIPPING for now.
    # <class 'data.models.BaseExperimentalData> # Abstract
    definition = """
    -> Session
    -> User
    datadescription_id:		char(32)		# data id
    created:			datetime		# created
    generating_software:	varchar(255)		# generating software
    provenance_directory:	varchar(255)		# provenance directory
    """
