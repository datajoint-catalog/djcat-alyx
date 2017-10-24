
import datajoint as dj

# schema = dj.schema(dj.config['FIXME'], locals())


@schema
class User(dj.Manual):
    # <class 'misc.models.OrderedUser'>
    # <class 'django.contrib.auth.models.User'>
    definition = """
    username:		varchar(255)	# username
    ---
    password:		varchar(255)	# password
    email:		varchar(255)	# email address
    last_login:		datetime	# last login
    first_name:		varchar(255)	# first name
    last_name:		varchar(255)	# last name
    date_joined:	datetime	# date joined
    is_active:		boolean		# active
    is_staff:		boolean		# staff status
    is_superuser:	boolean		# superuser status
    """


@schema
class UserGroup(dj.Manual):
    TODO = True
    definition = """
    groupname:		varchar(255)	# groupname
    """

    class UserGroupMembership(dj.Part):

        definition = """
        -> UserGroup
        -> User
        """


@schema
class PermissionType(dj.Lookup):

    definition = """
    permission: varchar(30)
    """
    contents = zip(['p1', 'p2', 'p3'])


@schema
class UserPermission(dj.Lookup):

    definition = """
    -> User
    -> PermissionType
    """


@schema
class BrainLocation(dj.Manual):
    # <class 'misc.models.BrainLocation'>
    definition = """
    brain_location_id:		char(32)	# brain location id
    ---
    name:			varchar(255)	# name
    stereotaxic_coordinates:	longblob	# stereotaxic coordinates
    description:		varchar(255)	# description
    allen_location_ontology:    varchar(255)	# allen location ontology
    json:			varchar(255)	# json
    """


@schema
class Severity(dj.Lookup):
    definition = """
    severity:			tinyint			# severity
    ---
    severity_desc:		varchar(32)		# severity desc
    """
    contents = (
        (0, ''),
        (1, 'Sub-threshold'),
        (2, 'Mild'),
        (3, 'Moderate'),
        (4, 'Severe'),
        (5, 'Non-recovery'),
    )


@schema
class CoordinateTransformation(dj.Manual):
    # <class 'misc.models.CoordinateTransformation'>
    definition = """
    transform_id:		char(32)	# id
    ---
    json:			varchar(255)	# json
    name:    			varchar(255)	# name
    description:		varchar(255)	# description
    allen_location_ontology:	varchar(255)	# allen location ontology
    origin:			longblob	# origin
    transformation_matrix:    	longblob	# transformation matrix
    """


@schema
class Note(dj.Manual):
    # <class 'misc.models.Note'>
    # FIXME: allows tagging objects via django's ContentType and UUIDs
    definition = """
    -> User
    note_id:		char(32)		# id
    ---
    date_time:		datetime		# date time
    text:		varchar(255)		# text
    object_id:		char(32)		# object id
    json:		varchar(255)		# json
    """
