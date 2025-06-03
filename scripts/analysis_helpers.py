import xarray as xr
import numpy as np
from scipy.signal import welch
import matplotlib.pyplot as plt

def calc_flux_spec(flux_ts):
    flux_anom = flux_ts - flux_ts.mean('time')
    flux_anom = xr.apply_ufunc(
        lambda y: y - np.polyval(np.polyfit(np.arange(len(y)), y, 1), np.arange(len(y))),
        flux_anom,
        dask='parallelized',
        output_dtypes=[float],
    )
    
    dt_years = (
        (flux_anom.time[1] - flux_anom.time[0]).values
        / np.timedelta64(1, 'D')
    ) / 365.2425
    fs = 1.0 / dt_years          # sampling frequency [yr⁻¹]
    
    nper = min(256, len(flux_anom))
    freq, psd = welch(
        flux_anom.values,           # 1-D numpy array
        fs=fs,                    # sampling frequency
        window='hann',
        nperseg=nper,
        detrend='constant',
        scaling='density',
    )
    
    spectrum = xr.DataArray(
        psd,
        coords={'frequency': freq},
        dims='frequency',
        name='volume_flux_PSD',
        attrs={
        'units': 'm⁶ s⁻² yr',  # power per frequency bin
        'long_name': 'Power spectral density of volume flux',
        'method': f'Welch; nperseg={nper}, Hann window, detrended constant',
        }
    )
    return(freq, psd, spectrum)