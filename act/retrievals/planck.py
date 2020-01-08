import numpy as np


def planck(wnum=None, radiance=None, temperature=None):
    """
    Planck function to convert radiance to temperature or temperature to radiance
    given a corresponding wavenumber value.

    Parameters
    ----------
    wnum : float or list or numpy array
        wavenumber for corresponding radiance or temperature value
    radiance : float or list or numpy array
        Radiance value of corresponding wavenumber in W/m^2/sr/cm
    temperature : float or list or numpy array
        Temperature value of corresponding wavenumber in degK/cm

    References
    ----------
        This procedure was created for the AERI vs. IRT comparison from F77 code
        orginally written by Jim Liligren and passed to the DQO by the ARM IRT mentor.

    Example
    -------
    > planck(wnum=1100, temperature=300)
    81.49372361846207

    > planck(wnum=1100, radiance=81.49)
    299.9974150039702

    """

    # h = Plancks's constant
    # k = Boltzmann's constant
    # c = Speed of light in a vacuum
    # C1 = 2 h c^2, [W cm^2]
    C1 = 1.191066e-5  # For radiance in units of mW m^-2 sr^-1 /cm^-1
    # C2 = h c / k, [K cm]
    C2 = 1.438833

    if radiance is not None:
        radiance = np.array(radiance, dtype=np.float64)
        wnum = np.array(wnum, dtype=np.float64)
        return (C2 * wnum) / np.log(1.0 + (C1 * wnum**3 / radiance))

    if temperature is not None:
        temperature = np.array(temperature, dtype=np.float64)
        wnum = np.array(wnum, dtype=np.float64)
        return (C1 * wnum**3) / (np.exp(C2 * wnum / temperature) - 1.0)
