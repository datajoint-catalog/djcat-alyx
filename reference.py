# <class 'misc.models.OrderedUser'>
# <class 'django.contrib.auth.models.User'>
# <class 'misc.models.BrainLocation'>

import datajoint as dj

schema = dj.schema(dj.config['FIXME'], locals())


@schema
class User(dj.Manual):

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

    definition = """
    id:				char(32)	# id
    ---
    json:			varchar(255)	# json
    name:			varchar(255)	# name
    stereotaxic_coordinates:	longblob	# stereotaxic coordinates
    description:		varchar(255)	# description
    allen_location_ontology:    varchar(255)	# allen location ontology
    """
