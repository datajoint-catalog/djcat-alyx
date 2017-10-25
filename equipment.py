import datajoint as dj

schema = dj.schema(dj.config['names.%s' % __name__], locals())


@schema
class LabLocation(dj.Manual):
    # <class 'equipment.models.LabLocation'>
    definition = """
    lab_location:		int             # lab location
    ---
    name:                       varchar(255)    # name
    """


@schema
class Supplier(dj.Manual):
    # <class 'equipment.models.Supplier'>
    definition = """
    supplier_name:		int             # supplier name
    ---
    description:		varchar(1024)	# description
    """


@schema
class VirusBatch(dj.Manual):
    # <class 'equipment.models.VirusBatch'>
    definition = """
    -> Supplier
    batch_id:			int             # batch id
    ---
    description:		varchar(255)	# description
    virus_type:			varchar(255)	# virus type
    date_time_made:		datetime	# date time made
    nominal_titer:		float		# nominal titer
    """


@schema
class EquipmentModel(dj.Manual):
    # <class 'equipment.models.EquipmentModel'>
    definition = """
    -> Supplier
    model_id:			int             # model id
    ---
    model_name:			varchar(255)	# model name
    description:		varchar(255)	# description
    """


@schema
class Appliance(dj.Manual):
    # <class 'equipment.models.Appliance'>
    # TODO: Should appliances be a lookup?
    # ... assuming Alyx' separate classes vs field is reasoned.
    definition = """
    -> LabLocation
    -> EquipmentModel
    appliance_id:		int             # appliance id
    ---
    serial:			varchar(255)	# serial
    description:		varchar(255)	# description
    descriptive_name:		varchar(255)	# descriptive name
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

    class ProbeModel(dj.Part):
        # <class 'electrophysiology.models.ProbeModel'>
        definition = """
        -> Appliance
        """
