
import datajoint as dj

schema = dj.schema(dj.config["FIXME"], locals())


@schema
class LabLocation(dj.Manual):
    # <class 'equipment.models.LabLocation'>
    definition = """
    lab_location:		char(32)	# lab location
    ---
    json:			varchar(255)	# json
    """


@schema
class Supplier(dj.Manual):
    # <class 'equipment.models.Supplier'>
    definition = """
    supplier_name:		char(32)	# supplier name
    ---
    description:		varchar(1024)	# description
    """


@schema
class VirusBatch(dj.Manual):
    # <class 'equipment.models.VirusBatch'>
    definition = """
    -> Supplier
    batch_id:			char(32)	# id
    ---
    description:		varchar(255)	# description
    virus_type:			varchar(255)	# virus type
    date_time_made:		datetime	# date time made
    nominal_titer:		float		# nominal titer
    json:			varchar(255)	# json
    """


@schema
class EquipmentModel(dj.Manual):
    # <class 'equipment.models.EquipmentModel'>
    definition = """
    -> Supplier
    model_id:			char(32)	# id
    ---
    model_name:			varchar(255)	# model name
    description:		varchar(255)	# description
    json:			varchar(255)	# json
    """


@schema
class Appliance(dj.Manual):
    # <class 'equipment.models.Appliance'>
    # TODO: -> ContentType
    # TODO: Should appliance types just be a lookup?
    #   currently assuming Alyx use of separate classes vs field is reasoned.
    definition = """
    -> LabLocation
    -> EquipmentModel
    appliance_id:		char(32)	# id
    ---
    serial:			varchar(255)	# serial
    description:		varchar(255)	# description
    descriptive_name:		varchar(255)	# descriptive name
    json:			varchar(255)	# json
    """

    class WeighingScale(dj.Part):
        # <class 'equipment.models.WeighingScale'>
        definition = """
        -> Appliance
        """

    class LightSource(dj.Part):
        # <class 'equipment.models.LightSource'>
        definition = """
        -> Appliance
        """

    class Amplifier(dj.Part):
        # <class 'equipment.models.Amplifier'>
        definition = """
        -> Appliance
        """

    class PipettePuller(dj.Part):
        # <class 'equipment.models.PipettePuller'>
        definition = """
        -> Appliance
        """

    class DAQ(dj.Part):
        # <class 'equipment.models.DAQ'>
        definition = """
        -> Appliance
        """
