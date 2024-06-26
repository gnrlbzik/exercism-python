"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    
    if not temperature < 800: return False
    
    if not neutrons_emitted > 500: return False
    
    return True if temperature * neutrons_emitted < 500000 else False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    generated_power = voltage * current
    
    efficiency_level = (generated_power / theoretical_max_power) * 100

    efficiency_scale_levels = {
        '<100': 'green',
        '<80': 'orange',
        '<60': 'red',
        '<30': 'black',
    }
    
    if efficiency_level >= 80:
        return efficiency_scale_levels['<100']
    elif efficiency_level >= 60:
        return efficiency_scale_levels['<80']
    elif efficiency_level >= 30:
        return efficiency_scale_levels['<60']
    else:
        return efficiency_scale_levels['<30']


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    range = temperature * neutrons_produced_per_second
    range_to_threshold_percentage = (range / threshold) * 100
    is_range_threshold_nominal = (range - threshold) < (threshold * .1)

    if range_to_threshold_percentage < 90:
        return 'LOW'
    elif is_range_threshold_nominal:
        return 'NORMAL'
    else:
        return 'DANGER'
