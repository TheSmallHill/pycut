import logging
from .unit import Unit


class Stock:
    # Parameters without defaults
    nominal_width = None
    nominal_length = None
    nominal_thickness = None

    actual_width = None
    actual_length = None
    actual_thickness = None

    quantity = None
    material_id = None

    # Parameters with defaults
    dimension_unit = Unit.INCHES
    grain_direction_along_length = True

    def __init__(self, n_width, n_length, n_thickness, a_width, a_length, a_thickness, quantity, material_id, dim_unit=None, grain_direction_along_length=True):
        # Handling for required inputs
        if n_width <= 0:
            raise ValueError('Nominal width cannot be less than or equal to zero')
        elif not isinstance(n_width, float):
            raise TypeError('Nominal width must be of type float')
        else:
            self.nominal_width = n_width

        if n_length <= 0:
            raise ValueError('Nominal length cannot be less than or equal to zero')
        elif not isinstance(n_length, float):
            raise TypeError('Nominal length must be of type float')
        else:
            self.nominal_length = n_length

        if n_thickness <= 0:
            raise ValueError('Nominal thickness cannot be less than or equal to zero')
        elif not isinstance(n_thickness, float):
            raise TypeError('Nominal thickness must be of type float')
        else:
            self.nominal_thickness = n_thickness

        if a_width <= 0:
            raise ValueError('Actual width cannot be less than or equal to zero')
        elif a_width > n_width:
            raise ValueError('Actual width cannot be greater than nominal width')
        elif not isinstance(a_width, float):
            raise TypeError('Actual width must be of type float')
        else:
            if a_width == n_width:
                logging.warning('Actual width given is equal to nominal width')

            self.actual_width = a_width

        if a_length <= 0:
            raise ValueError('Actual length cannot be less than or equal to zero')
        elif a_width > n_width:
            raise ValueError('Actual length cannot be greater than nominal length')
        elif not isinstance(a_length, float):
            raise TypeError('Actual length must be of type float')
        else:
            if a_length == n_length:
                logging.warning('Actual length given is equal to nominal length')

            self.actual_length = a_length

        if a_thickness <= 0:
            raise ValueError('Actual thickness cannot be less than or equal to zero')
        elif a_thickness > n_thickness:
            raise ValueError('Actual thickness cannot be greater than nominal thickness')
        elif not isinstance(a_thickness, float):
            raise TypeError('Actual thickness must be of type float')
        else:
            if a_thickness == n_thickness:
                logging.warning('Actual thickness given is equal to nominal thickness')

            self.actual_thickness = a_thickness

        if quantity <= 0:
            raise ValueError('Stock quantity cannot be less than or equal to zero')
        elif not isinstance(quantity, int):
            raise TypeError('Quantity must be of type int')
        else:
            self.quantity = quantity

        if material_id is None or not isinstance(material_id, str):
            raise TypeError('Material identifier must be given as a string')

        # Handling for optional parameters
        if dim_unit is not None:
            numeric_level = getattr(Unit, dim_unit, None)
            if not isinstance(numeric_level, int):
                raise ValueError('Invalid dimension unit: %s' % dim_unit)

            self.dimension_unit = numeric_level

        if grain_direction_along_length is not None:
            if not isinstance(grain_direction_along_length, bool):
                raise TypeError('Grain direction along length must be given as a bool')

            self.grain_direction_along_length = grain_direction_along_length
